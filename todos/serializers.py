from email.policy import default
from rest_framework import serializers
from .models import Category, Todo

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name','created_at']
class TodoSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source = 'category.name',
        read_only = True,
        allow_null = True,
        default = None 
    )
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'category', 'category_name']