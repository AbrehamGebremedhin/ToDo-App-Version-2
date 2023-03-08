from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http.response import JsonResponse

# Local files
from .serializer import TaskSerializer
from .models import Task


class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class TaskList(APIView):
    def get(self, req):
        movies = Task.objects.all()
        serializer = TaskSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
