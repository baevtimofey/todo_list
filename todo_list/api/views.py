from .serializers import ToDoCreateSerializer, ToDoListSerializer
from .models import ToDo

from rest_framework.views import APIView
from rest_framework.response import Response


class ToDoCreateListView(APIView):
    """ Creating and display tasks """
    
    def get(self, request):
        tasks = ToDo.objects.all()
        serializer = ToDoListSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        new_task = ToDo.objects.create(
            title=request.data['title'],
            description=request.data['description']
        )
        serializer = ToDoCreateSerializer(new_task)
        return Response(serializer.data)
    