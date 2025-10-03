from django.urls import path
from .views import NewListCreateAPIView, NewDetailAPIView

urlpatterns = [
    path('news/', NewListCreateAPIView.as_view()),
    path('news/<int:pk>/', NewDetailAPIView.as_view()),
]


