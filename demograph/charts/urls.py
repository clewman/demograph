from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'charts'
urlpatterns = [
    path('graphs/', views.graphs, name='graphs'),
    path('get_data/', views.get_data, name='get_data'),
    path('get_plotly_url/', views.get_plotly_url, name='get_plotly_url'),
    path('get_plotly_state_url/', views.get_plotly_state_url, name='get_plotly_state_url'),
    path('get_plotly_line_url/', views.get_plotly_line_url, name='get_plotly_line_url'),
    path('', views.index, name='index'),
    path('charts/about/', views.about, name='about'),
    path('charts/morecharts/', views.morecharts, name='morecharts'),
    path('charts/chartdata', views.ChartData, name='chartdata'),
    path('charts/data/', views.get_data_test, name='api-data'),
    # url(r'^api/chart/data/$', views.ChartData.as_view(), name='api-chart-data'),
]