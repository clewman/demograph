
from . import views
from django.urls import  path

app_name = 'demograph'
urlpatterns = [
    path('', views.index, name='index'),


]