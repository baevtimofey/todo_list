from django.urls import path

from .views import ToDoCreateView

urlpatterns = [
    path('tasks/', ToDoCreateView.as_view()),
]
