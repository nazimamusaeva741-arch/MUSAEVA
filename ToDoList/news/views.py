from django.shortcuts import render
from rest_framework import generics
from .serializers import NewSerializer
from .models import News


class NewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = NewSerializer
    queryset = News.objects.filter(is_archaived=False)



class NewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewSerializer
    queryset = News.objects.all()



