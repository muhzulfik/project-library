from django.urls import path
from . import views

app_name ='pagestaff'
urlpatterns = [
    path('index/', views.index, name='staff')
]