from gc import get_objects

from django.core.serializers import serialize
from django.template.defaulttags import querystring
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions, status
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from .models import Note
from .serializers import NoteSerializer

class ListTaskAPPIView(APIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self,request,*args,**kwargs):
        task = Task.objects.all()
        serializer = TaskSerializer(task,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class DetailTaskAPIView(APIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self,request,task_id,*args,**kwargs):
        task = get_object_or_404(Task,pk=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, pk=task_id)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NoteAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            note = get_object_or_404(Note, pk=pk)
            serializer = NoteSerializer(note)
        else:
            notes = Note.objects.all()
            serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

