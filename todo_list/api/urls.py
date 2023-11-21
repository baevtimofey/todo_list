from django.urls import path

from .views import ToDoCreateListView

urlpatterns = [
    path('tasks/', ToDoCreateListView.as_view()),
]
