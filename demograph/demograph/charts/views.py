
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import IncomeData, Gender, EducationLevel, IncomeLevel
import json
from django.http import JsonResponse


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
    return HttpResponse({'data': data})







