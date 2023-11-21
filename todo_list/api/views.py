from .serializers import ToDoSerializer
from .models import ToDo

from rest_framework import generics


class CreateToDo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    