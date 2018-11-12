from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'charts'
urlpatterns = [
    path('graphs/', views.graphs, name='graphs'),
    path('get_data/', views.get_data, name='get_data'),
    path('get_plotly_url/', views.get_plotly_url, name='get_plotly_url'),
    path('get_plotly_state_url/', views.get_plotly_state_url, name='get_plotly_state_url'),
    path('', views.index, name='index'),
    path('charts/about/', views.about, name='about'),
    path('charts/morecharts/', views.morecharts, name='morecharts'),

]