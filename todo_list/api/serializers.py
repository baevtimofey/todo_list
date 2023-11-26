from .models import ToDo

from rest_framework import serializers


class ToDoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
