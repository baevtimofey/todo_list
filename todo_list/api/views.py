from .serializers import ToDoCreateSerializer
from .models import ToDo

from rest_framework.views import APIView
from rest_framework.response import Response


class ToDoCreateView(APIView):
    """ Creating task """
    
    def post(self, request):
        new_task = ToDo.objects.create(
            title=request.data['title'],
            description=request.data['description']
        )
        serializer = ToDoCreateSerializer(new_task)
        return Response(serializer.data)
    