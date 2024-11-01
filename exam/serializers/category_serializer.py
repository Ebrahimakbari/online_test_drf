from rest_framework import serializers
from ..models import Category,FavoriteCategory
from django.contrib.auth import get_user_model

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class FavoriteListRetrieveSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='Category.title')
    
    class Meta:
        model = FavoriteCategory
        fields = ['id','category']

class FavoriteListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCategory
        fields = ['category']
        
    def create(self, validated_data):
        return FavoriteCategory.objects.create(
            **validated_data,
            student_id = self.context['user_id']
            )