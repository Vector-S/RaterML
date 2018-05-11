from django.urls import path
from health_manager import views

app_name = 'health_manager'

urlpatterns = [
    path(r'health/',views.health,name='health'),
]
