from django.urls import path
from main_app import views

urlpatterns = [
    path(r'',views.index,name='index'),
]
