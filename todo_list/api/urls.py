from django.urls import path

from .views import CreateToDo

urlpatterns = [
    path('tasks/', CreateToDo.as_view()),
]
