from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from final_app.models import Fabric, Product, Delivery, Sale
from rest_framework import serializers

# Сериалайзер для пользователей
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'date_of_birth', 'card', 'email', 'first_name', 'last_name', 'is_superuser']

# Сериалайзер для фабрик
class FabricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabric
        fields = ['id', 'address', 'name', 'country']

# Сериалайзер для продуктов
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'price', 'name', 'vendor_code', 'fabric', 'image']

# Сериалайзер для поставок
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'delivery_date', 'quantity', 'product', 'price_for_sale']

# Сериалайзер для продаж
class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'date', 'quantity', 'user', 'delivery']

# Сериалайзер для данных о продаваемых товарах
class StoreSerializer(serializers.Serializer):    
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.IntegerField()
    fabric_name = serializers.CharField()
    fabric_country = serializers.CharField()
    price_for_sale = serializers.IntegerField()
    name = serializers.CharField()
    vendor_code = serializers.CharField()
    quantity = serializers.IntegerField()
    image = serializers.CharField()

# Сериалайзер для процесса покупки
class UserSalesSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    name = serializers.CharField()
    total = serializers.IntegerField()
    date = serializers.DateTimeField()

