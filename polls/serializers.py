from rest_framework import serializers

from polls.models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('id', 'name', 'category', 'price')

    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.save()
    #     return instance
