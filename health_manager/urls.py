from django.urls import path
from health_manager import views

urlpatterns = [
    path(r'health/',views.health,name='health'),
]
