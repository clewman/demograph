from django.conf.urls import url
from django.urls import path
from . import views

from .views import ChartData, HomeView, get_data_chartjs

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
    # path('charts/chartdata', views.ChartData, name='chartdata'),
    # test for plotly
    path('graphs/graphsline', views.graphs_line, name='graphs_line'),

    path('api/data/', get_data_chartjs, name='api-data'),
    path('api/', HomeView.as_view()),
    path('charts/chartjs', views.chartjs, name='chartjs'),
    path('api/chart/data/', ChartData.as_view()),

]