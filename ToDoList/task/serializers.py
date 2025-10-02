from rest_framework import serializers
from .models import Task
from .models import Note


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ["id","created_at"]



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = 'all'




