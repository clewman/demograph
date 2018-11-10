from django.core.management.base import BaseCommand
import json
import requests
from charts.models import IncomeLevel, Gender, EducationLevel, IncomeData, State, County


def get_json(url):
    return json.loads(requests.get(url).text)


class Command(BaseCommand):

    def handle(self, *args, **options):

        IncomeData.objects.all().delete()

        urls = []
        for year in range(2012,2016):
            variables = 'NAME,B17003_004E,B17003_005E,B17003_006E,B17003_007E,B17003_009E,B17003_010E,B17003_011E,B17003_012E,B17003_015E,B17003_016E,B17003_017E,B17003_018E,B17003_020E,B17003_021E,B17003_022E,B17003_023E'
            geography = 'county:*'
            dataset_name = '/acs1'
            url = f'https://api.census.gov/data/{year}{dataset_name}?get={variables}&for={geography}'

            urls.append((year, url))
            # print(url)
            # return

        for year in range(2016, 2018):
            variables = 'NAME,B17003_004E,B17003_005E,B17003_006E,B17003_007E,B17003_009E,B17003_010E,B17003_011E,B17003_012E,B17003_015E,B17003_016E,B17003_017E,B17003_018E,B17003_020E,B17003_021E,B17003_022E,B17003_023E'
            geography = 'county:*'
            dataset_name = '/acs/acs1'
            url = f'https://api.census.gov/data/{year}{dataset_name}?get={variables}&for={geography}'
            urls.append((year, url))
            # print(current_years_url)
        # return


        subsets = [
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Male', 'EducationLevel': '< High School', 'column_name': 'B17003_004E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Male', 'EducationLevel': 'High School', 'column_name': 'B17003_005E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Male', 'EducationLevel': 'Some College', 'column_name': 'B17003_006E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Male', 'EducationLevel': 'College',
             'column_name': 'B17003_007E'},

            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': '< High School',
             'column_name': 'B17003_009E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'High School', 'column_name': 'B17003_010E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'Some College',
             'column_name': 'B17003_011E'},
            {'IncomeLevel': 'Below Poverty', 'Gender': 'Female', 'EducationLevel': 'College',
             'column_name': 'B17003_012E'},

            {'IncomeLevel': 'Above Poverty', 'Gender': 'Male', 'EducationLevel': '< High School',
             'column_name': 'B17003_015E'},
            {'IncomeLevel': 'Above Poverty', 'Gender': 'Male', 'EducationLevel': 'High School', 'column_name': 'B17003_016E'},
            {'IncomeLevel': 'Above Poverty', 'Gender': 'Male', 'EducationLevel': 'Some College',
             'column_name': 'B17003_017E'},
            {'IncomeLevel': 'Above Poverty', 'Gender': 'Male', 'EducationLevel': 'College',
             'column_name': 'B17003_018E'},

            {'IncomeLevel': 'Above Poverty', 'Gender': 'Female', 'EducationLevel': '< High School',
             'column_name': 'B17003_020E'},
            {'IncomeLevel': 'Above Poverty', 'Gender': 'Female', 'EducationLevel': 'High School', 'column_name': 'B17003_021E'},
            {'IncomeLevel': 'Above Poverty', 'Gender': 'Female', 'EducationLevel': 'Some College',
             'column_name': 'B17003_022E'},
            {'IncomeLevel': 'Above Poverty', 'Gender': 'Female', 'EducationLevel': 'College',
             'column_name': 'B17003_023E'},

        ]


        for year, url in urls:
            print('loading url: ' + url)
            data_in = get_json(url)


            headers = data_in[0]
            data_in = data_in[1:]
            data_out = []
            for row_in in data_in:
                row_out = {}
                for i, header in enumerate(headers):
                    row_out[header] = row_in[i]
                data_out.append(row_out)

            for row in data_out:
                print(row)

                for subset in subsets:
                    income_level, created = IncomeLevel.objects.get_or_create(name=subset['IncomeLevel'])
                    gender, created = Gender.objects.get_or_create(name=subset['Gender'])
                    education_level, created = EducationLevel.objects.get_or_create(name=subset['EducationLevel'])
                    county_state = row['NAME'].split(', ')
                    state_name = county_state[1]
                    county_name = county_state[0]
                    state, created = State.objects.get_or_create(name=state_name)
                    county, created = County.objects.get_or_create(name=county_name, state_id=state.id)
                    population = int(row[subset['column_name']])
                    income_data = IncomeData(education_level=education_level, gender=gender, income_level=income_level, population=population, year=year, county=county)
                    income_data.save()




