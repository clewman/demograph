
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import IncomeData, Gender, EducationLevel, IncomeLevel
import json
from django.http import JsonResponse
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import pandas as pd
import resource
import numpy as np


def index(request):
    return render(request, 'charts/index.html', {})


def about(request):
    return render(request, 'charts/about.html', {})


def graphs(request):
    # items = IncomeData.objects.filter(year='2015', gender=Gender.objects.get(pk=2), education_level=EducationLevel.objects.get(pk=1))
    items = IncomeData.objects.filter(year=2015)
    years = {income_datum.year for income_datum in IncomeData.objects.all()}
    years = list(years)
    years.sort(reverse=True)
    print(years)

    return render(request, 'charts/graphs.html', {'items': items,
                                                  'years': years,
                                                  'income_levels': IncomeLevel.objects.all(),
                                                  'education_levels': EducationLevel.objects.all(),
                                                  'genders': Gender.objects.all()})


def get_data(request):
    gender_id = request.GET['gender_id']
    education_level_id = request.GET['education_level_id']
    income_level_id = request.GET['income_level_id']
    year = request.GET['year']

    items = IncomeData.objects.all()
    if gender_id != '':
        items = items.filter(gender_id=gender_id)
    if year != '':
        items = items.filter(year=year)
    if income_level_id != '':
        items = items.filter(income_level_id=income_level_id)
    if education_level_id != '':
        items = items.filter(education_level_id=education_level_id)

    items = items[:1000]

    data = []
    for item in items:
         data.append(item.to_dictionary())
    return JsonResponse({'data': data})


def get_plotly_url(request):
    gender_id = request.GET.get('gender_id', '')
    education_level_id = request.GET.get('education_level_id', '')
    income_level_id = request.GET.get('income_level_id', '')
    year = request.GET.get('year', '')

    items = IncomeData.objects.all()
    if gender_id != '':
        items = items.filter(gender_id=gender_id)
    if year != '':
        items = items.filter(year=year)
    if income_level_id != '':
        items = items.filter(income_level_id=income_level_id)
    if education_level_id != '':
        items = items.filter(education_level_id=education_level_id)

    items = items[:1000]

    data = []
    for item in items:
        data.append(item.to_dictionary())

    # df = pd.read_csv('2011_us_ag_exports.csv')
    # for col in df.columns:
    #     df[col] = df[col].astype(str)
    #
    # scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'], \
    #        [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]
    #
    # df['text'] = df['state'] + '<br>' + \
    #              'Beef ' + df['beef'] + ' Dairy ' + df['dairy'] + '<br>' + \
    #              'Fruits ' + df['total fruits'] + ' Veggies ' + df['total veggies'] + '<br>' + \
    #              'Wheat ' + df['wheat'] + ' Corn ' + df['corn']
    #
    # data = [dict(
    #     type='choropleth',
    #     colorscale=scl,
    #     autocolorscale=False,
    #     locations=df['code'],
    #     z=df['total exports'].astype(float),
    #     locationmode='USA-states',
    #     text=df['text'],
    #     marker=dict(
    #         line=dict(
    #             color='rgb(255,255,255)',
    #             width=2
    #         )),
    #     colorbar=dict(
    #         title="Millions USD")
    # )]
    #
    # layout = dict(
    #     title='2011 US Agriculture Exports by State<br>(Hover for breakdown)',
    #     geo=dict(
    #         scope='usa',
    #         projection=dict(type='albers usa'),
    #         showlakes=True,
    #         lakecolor='rgb(255, 255, 255)'),
    # )

    fig = dict(data=data, layout=layout)
    url = py.plot(fig, filename='d3-cloropleth-map')
    # url = 'http://www.google.com'
    return HttpResponse(url)







