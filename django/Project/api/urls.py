from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData,name='api'),
    
    path('/addi/',views.addItem,name='addi'),
    
]
