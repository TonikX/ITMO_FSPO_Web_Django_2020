from rest_framework import serializers

from voznesensky_app.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id",
                  "passport_id",
                  "full_name",
                  "birth_date",
                  "address_registration",
                  "address_residence",
                  "occupation",
                  "phones",
                  "gender",
                  "birth_place",
                  "discovery_info",
                  "email",
                  "comment",
                  "comment_addition",
                  "balance",
                  "permanent_discount",
                  "is_archived",
                  "archived_reason",)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.passport_id = validated_data.get('passport_id', instance.passport_id)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.address_registration = validated_data.get('address_registration', instance.address_registration)
        instance.address_residence = validated_data.get('address_residence', instance.address_residence)
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.phones = validated_data.get('phones', instance.phones)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.birth_place = validated_data.get('birth_place', instance.birth_place)
        instance.discovery_info = validated_data.get('discovery_info', instance.discovery_info)
        instance.email = validated_data.get('email', instance.email)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.comment_addition = validated_data.get('comment_addition', instance.comment_addition)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.permanent_discount = validated_data.get('permanent_discount', instance.permanent_discount)
        instance.is_archived = validated_data.get('is_archived', instance.is_archived)
        instance.archived_reason = validated_data.get('archived_reason', instance.archived_reason)
        instance.save()
        return instance


class DiscountCardSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(many=False, queryset=DiscountCard.objects.all())

    class Meta:
        model = DiscountCard
        fields = ("client", "percent")

        def create(self, validated_data):
            return DiscountCard.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.client = validated_data.get('client', instance.client)
            instance.percent = validated_data.get('percent', instance.percent)
            instance.save()
            return instance


class TransactionSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = ['client', 'change', 'date_time', 'comment']

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.change = validated_data.get('change', instance.change)
        instance.date_time = validated_data.get('date_time', instance.date_time)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("qty", "name", "price", "group")

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.qty = validated_data.get('qty', instance.qty)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.group = validated_data.get('group', instance.group)
        instance.save()
        return instance


class SoldItemSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    item = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = SoldItem
        fields = ("item", "price_actual", "client", "date", "isDiscountCardUsed")

    def create(self, validated_data):
        return SoldItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.price_actual = validated_data.get('price_actual', instance.price_actual)
        instance.date = validated_data.get('date', instance.date)
        instance.isDiscountCardUsed = validated_data.get('isDiscountCardUsed', instance.isDiscountCardUsed)
        instance.save()
        return instance


class VisitSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Visit
        fields = ("date", "isFirst", "reason", "comment", "client", "isDiscountCardUsed", "status")

    def create(self, validated_data):
        return Visit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.isFirst = validated_data.get('isFirst', instance.isFirst)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.isDiscountCardUsed = validated_data.get('isDiscountCardUsed', instance.isDiscountCardUsed)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
