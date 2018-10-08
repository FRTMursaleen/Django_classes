from rest_framework import serializers
from .models import *


class PostSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'


class PostSerializerData(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Todo