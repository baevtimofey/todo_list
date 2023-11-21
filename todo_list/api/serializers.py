from .models import ToDo

from rest_framework import serializers


class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id',)
