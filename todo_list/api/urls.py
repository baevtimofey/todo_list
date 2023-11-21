from django.urls import path

from .views import (ToDoCreateListView,
                    ToDoDetailView)

urlpatterns = [
    path('tasks/', ToDoCreateListView.as_view()),
    path('task/<int:pk>/', ToDoDetailView.as_view()),
]
