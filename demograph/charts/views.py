
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import IncomeData, Gender, EducationLevel, IncomeLevel, SystemParameter, County, State
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

    for county in County.objects.all():
        if county.fips != '' and county.fips not in fips:
            fips.append(county.fips)
            values.append(0)

    #this makes the graph look nice but it gives weird figures
    # top_populations = list(sorted(values, reverse=True))[:20]
    # max_value = sum(top_populations) / len(top_populations) / 10

    max_value = 200000000

    colorscale = ["#f4eaef", "#ead6e0", "#e0c1d1", "#d6adc1", "#cc99b2", "#c184a3", "#b77093", "#ad5b84", "#a34775", "#993366",
                  "#892d5b", "#7a2851", "#6b2347", "#5b1e3d", "#4c1933", "#2d0f1e", "#0f050a"]
    endpts = list(np.linspace(0, max_value, len(colorscale) - 1))

    if gender_id == '':
        chart_title = 'All Genders, '
    else:
        chart_title = Gender.objects.get(pk=gender_id).name + ', '
    if year == '':
        chart_title+= 'All Years, '
    else:
        chart_title += year + ', '
    if education_level_id == '':
        chart_title += 'All Education Levels, '
    else:
        chart_title += EducationLevel.objects.get(pk=education_level_id).name + ', '
    if income_level_id =='':
        chart_title = "All Education Levels, "
    else:
        chart_title += IncomeLevel.objects.get(pk=income_level_id).name


    fig = ff.create_choropleth(
        fips=fips, values=values, scope=['usa'],
        # binning_endpoints=endpts, colorscale=colorscale,
        binning_endpoints=[1000, 2500, 5000, 10000, 15000, 25000, 50000, 100000, 150000, 200000, 300000, 500000, 1000000, 1500000, 2000000, 5000000], colorscale=colorscale,
        show_state_data=False,
        show_hover=True, centroid_marker={'opacity': 0},
        asp=2.9, title=chart_title,
        legend_title='Number of People',
    )

    # create chart counter to not allow more than 25 graphs to be made (Plotly's max for a free account)
    chart_counter = SystemParameter.objects.get(name='Chart Counter')
    counter = int(chart_counter.value)
    counter += 1
    if counter >= 24:
        counter = 0
    chart_counter.value = str(counter)
    chart_counter.save()


    url = py.plot(fig, filename='choropleth_full_usa' + str(counter), auto_open=False)
    print(url)
    return HttpResponse(url)







