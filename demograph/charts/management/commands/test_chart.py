



from django.core.management.base import BaseCommand

import pandas as pd
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

from charts.models import State, County, IncomeData


class Command(BaseCommand):

    def handle(self, *args, **options):
        GET = {'gender_id': 1, 'year': 2012}
        gender_id = GET.get('gender_id', '')
        education_level_id = GET.get('education_level_id', '')
        income_level_id = GET.get('income_level_id', '')
        year = GET.get('year', '')

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

            if counter%10 == 0:
                print(f'{round(counter/len(items)*100,2)}%')
            counter += 1

        fips = list(output.keys())
        values = list(output.values())

        top_populations = list(sorted(values, reverse=True))[:20]
        max_value = sum(top_populations)/len(top_populations)/10

        colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
                      "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
                      "#08519c", "#0b4083", "#08306b"]
        endpts = list(np.linspace(0, max_value, len(colorscale) - 1))

        print(endpts)
        # fips = df_sample['FIPS'].tolist()
        # values = df_sample['Unemployment Rate (%)'].tolist()
        #
        fig = ff.create_choropleth(
            fips=fips, values=values, scope=['usa'],
            binning_endpoints=endpts, colorscale=colorscale,
            show_state_data=False,
            show_hover=True, centroid_marker={'opacity': 0},
            asp=2.9, title='USA by Unemployment %',
            legend_title='% unemployed'
        )
        url = py.plot(fig, filename='choropleth_full_usa')
