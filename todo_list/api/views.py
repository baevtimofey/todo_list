from django.http import Http404 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ToDoModelSerializer
from .models import ToDo


class ToDoCreateListView(APIView):
    """ Creating and display tasks """
    
    def get(self, request):
        tasks = ToDo.objects.all()
        serializer = ToDoModelSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ToDoModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'id': serializer.data['id']},
                            status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors,
                        status=status.HTTP_404_NOT_FOUND)


class ToDoDetailView(APIView):
    """ Detail task """
    
    def get_object(self, pk):
        try:
            return ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return Http404
    
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = ToDoModelSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = ToDoModelSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
