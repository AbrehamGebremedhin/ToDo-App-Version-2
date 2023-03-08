from django.urls import path
from .views import CreateTask, TaskList, TaskDetail

urlpatterns = [
    path('createTask/', CreateTask.as_view(), name='Create-Task'),
    path('tasks/', TaskList.as_view(), name='Task-list'),
    path('tasks/<int:pk>', TaskDetail.as_view(), name='Task-list'),
]
