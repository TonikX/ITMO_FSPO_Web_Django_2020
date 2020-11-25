from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsAllowedForAppUserDirect

from .models import *
from .serializers import *

# Create your views here.


class HunterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        hunters = Hunter.objects.all()
        serializer = HunterSerializer(hunters, many=True)
        return Response(serializer.data)


class FurPointView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        hunters = FurPoint.objects.all()
        serializer = FurPointSerializer(hunters, many=True)
        return Response(serializer.data)


class FurFactoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        hunters = FurFactory.objects.all()
        serializer = FurFactorySerializer(hunters, many=True)
        return Response(serializer.data)


class UsernameCheckView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        username = request.GET.get("u")

        return Response({'available': (User.objects.filter(username=username).count() == 0)})


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("u")
        password1 = request.data.get("p")
        password2 = request.data.get("c")
        role = request.data.get("r")
        if password1 != password2:
            return Response({"status": "error", "data": "Passwords don't match"})
        if role != "H" and role != "F" and role != "W":
            return Response({"status": "error", "data": "Invalid role selected"})
        user = User.objects.create_user(username, 'dev@null.no', password1)
        au = AppUser(user=user, role=role)
        au.save()
        if role == "H":
            address = request.data.get('a')
            Hunter(user=au, address=address).save()
        elif role == "F":
            name = request.data.get('a')
            FurFactory(user=au, name=name).save()
        elif role == "W":
            address = request.data.get('a')
            FurPoint(user=au, address=address).save()
        return Response({"status": "success"}, status=200)


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        au = AppUser.objects.get(user=request.user)
        role = au.role
        if role == "H":
            return Response({"status": "success", "data": HunterSerializer(Hunter.objects.get(user=au)).data})
        elif role == "F":
            return Response({"status": "success", "data": FurFactorySerializer(FurFactory.objects.get(user=au)).data})
        elif role == "W":
            return Response({"status": "success", "data": FurPointSerializer(FurPoint.objects.get(user=au)).data})
        elif role == "A":
            return Response({"status": "success", "data": {"user": AppUserSerializer(au).data}})

        return Response({"status": "error", "data": "Unknown role " + role}, status=400)

    def put(self, request):
        if request.data.get('a'):
            data = request.data.get('a')
            au = AppUser.objects.get(user=request.user)
            role = au.role
            if role == "F":
                item = FurFactory.objects.get(user=au)
                item.name = data
                item.save()
            elif role == "H":
                item = Hunter.objects.get(user=au)
                item.address = data
                item.save()
            elif role == "W":
                item = FurPoint.objects.get(user=au)
                item.address = data
                item.save()

            return Response({"status": "success"})

        password1 = request.data.get("n")
        password2 = request.data.get("c")
        old_password = request.data.get("o")
        if password1 != password2:
            return Response({"status": "error", "data": "Passwords don't match"})

        if not request.user.check_password(old_password):
            return Response({"status": "error", "data": "Invalid old password"})

        request.user.set_password(password1)
        request.user.save()
        return Response({"status": "success"})


class MeDataView(APIView):
    permission_classes = [IsAllowedForAppUserDirect]

    def get(self, request):
        au = AppUser.objects.get(user=request.user)
        role = au.role
        if role == "H":
            item = Hunter.objects.get(user=au)
            return Response({"status": "success",
                "datain": FurGatherSerializer(FurGathering.objects.filter(id_hunter=item), many=True).data,
                "dataout": FurDeliverySerializer(FurDelivery.objects.filter(id_hunter=item), many=True).data})
        elif role == "W":
            item = FurPoint.objects.get(user=au)
            return Response({"status": "success",
                "datain": FurDeliverySerializer(FurDelivery.objects.filter(id_furpoint=item), many=True).data,
                "dataout": FurShipmentSerializer(FurShipment.objects.filter(id_furpoint=item), many=True).data})
        elif role == "F":
            item = FurFactory.objects.get(user=au)
            return Response({"status": "success",
                "datain": FurShipmentSerializer(FurShipment.objects.filter(id_furfactory=item), many=True).data,
                "dataout": ()})
        elif role == "A":
            return Response({"status": "success", 
                "users": AppUserSerializer(AppUser.objects.all(), many=True).data,
                "datain": FurGatherSerializer(FurGathering.objects.all(), many=True).data,
                "dataout": FurDeliverySerializer(FurDelivery.objects.all(), many=True).data,
                "dataadm": FurShipmentSerializer(FurShipment.objects.all(), many=True).data})

        return Response({"status": "error", "data": "Unknown role " + role}, status=400)

    def post(self, request):
        au = AppUser.objects.get(user=request.user)
        role = au.role
        if role == "H":
            el = Hunter.objects.get(user=au)
            if (request.data.get("out")):
                save = FurDelivery(id_hunter=el, id_furpoint=FurPoint.objects.get(pk=request.data.get("to")), type=request.data.get("type"), sort=request.data.get("sort"), count=request.data.get("count"), price=request.data.get("price"))
                save.save()
            else:
                save = FurGathering(id_hunter=el, type=request.data.get("type"), sort=request.data.get("sort"), count=request.data.get("count"))
                save.save()

            return Response({"status": "success"})
        elif role == "W":
            el = FurPoint.objects.get(user=au)
            if (request.data.get("out")):
                save = FurShipment(id_furpoint=el, id_furfactory=FurFactory.objects.get(pk=request.data.get("to")), type=request.data.get("type"), sort=request.data.get("sort"), count=request.data.get("count"), price=request.data.get("price"))
                save.save()
            else:
                return Response({"status": "error", "data": "Invalid request"})

            return Response({"status": "success"})

        return Response({"status": "error", "data": "Unknown role " + role}, status=400)

class HuntersObjectView(APIView):
    permission_classes = [IsAllowedForAppUserDirect]

    def get(self, request, idx):
        return Response(HunterSerializer(Hunter.objects.get(pk=idx)).data)
