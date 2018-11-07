
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import IncomeData, Gender, EducationLevel, IncomeLevel
import json
from django.http import JsonResponse
import plotly.plotly as py
import plotly.figure_factory as ff

import plotly.graph_objs as go
import plotly
import pandas as pd
import resource
import numpy as np

import time


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


    # gender_id is '', so all genders
    # 23904823094, baker county, IL, male, 56
    # 23904823094, baker county, IL, female, 102

    # sum up all rows for a given county
    # start with an empty 'output' list
    # loop over all the items
    # if there already exists an item in the output list with the given county id
    # then add the population to it
    # otherwise add it

    counter = 0
    output = {}
    for item in items:
        if item.county.fips == '':
            continue

        if item.county.fips in output:
            output[item.county.fips] += item.population
        else:
            output[item.county.fips] = item.population

        if counter % 10 == 0:
            print(f'{round(counter/len(items)*100,2)}%')
        counter += 1

    fips = list(output.keys())
    values = list(output.values())

    top_populations = list(sorted(values, reverse=True))[:20]
    max_value = sum(top_populations) / len(top_populations) / 10

    colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
                  "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
                  "#08519c", "#0b4083", "#08306b"]
    endpts = list(np.linspace(0, max_value, len(colorscale) - 1))

    # fips = df_sample['FIPS'].tolist()
    # values = df_sample['Unemployment Rate (%)'].tolist()
    #
    fig = ff.create_choropleth(
        fips=fips, values=values, scope=['usa'],
        binning_endpoints=endpts, colorscale=colorscale,
        show_state_data=False,
        show_hover=True, centroid_marker={'opacity': 0},
        asp=2.9, title='USA by Unemployment %',
        legend_title='% unemployed',
    )

    url = py.plot(fig, filename='choropleth_full_usa' + str(hash(time.time())), auto_open=False)
    return HttpResponse(url)







