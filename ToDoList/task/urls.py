from django.urls import path
from .views import ListTaskAPPIView,DetailTaskAPIView
from .views import NoteAPIView

urlpatterns = [
    path('list/', ListTaskAPPIView.as_view()),
    path('list/<int:task_id>/', DetailTaskAPIView.as_view()),
    path('notes/', NoteAPIView.as_view()),
    path('notes/<int:pk>/', NoteAPIView.as_view()),
]
