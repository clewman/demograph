
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# from .models import Book
# from django.db import models

def chart_one(request):
    return render(request, 'charts/chart1.html', {})

def user_choice(request):

    user_input = request.POST['Chart_Type']
    user_choice = Chart_Type(user_choice=user_choice)
    user_choice.save()
    return render(request, 'charts/chart1.html', {})

def python_test(request):
    print('Hello, I am working')
    # import plotly.plotly as py
    # import plotly.graph_objs as go
    #
    # data = [go.Bar(
    #     x=['giraffes', 'orangutans', 'monkeys'],
    #     y=[20, 14, 23]
    # )]
    #
    # py.iplot(data, filename='basic-bar')

    return render(request, 'charts/chart1.html', {})

#
# def index(request):
#     return render(request, 'charts/index.html', {})




#
# def chart1(request):
#     # return render(request, 'charts/chart1.html', {})
#     return render(request, 'charts/chart1.html', {})
#
