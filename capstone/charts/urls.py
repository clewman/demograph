
from . import views
from django.urls import  path

app_name = 'charts'
urlpatterns = [
    path('charts/', views.chart_one, name='chart_one'),
    path('charts/', views.user_choice, name='user_choice'),
    # path('charts/', views.index, name='index')
]


