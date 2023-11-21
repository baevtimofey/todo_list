from .models import ToDo

from rest_framework import serializers


class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id',)


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class ToDoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'title', 'description')
