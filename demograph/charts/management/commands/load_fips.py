
from django.core.management.base import BaseCommand

import pandas as pd
from charts.models import State, County


class Command(BaseCommand):

    def handle(self, *args, **options):

        df_sample = pd.read_csv('./charts/management/commands/laucnty16.csv')
        df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
        df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
        df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']

        # County Name/State Abbreviation
        fips = df_sample['FIPS'].tolist()

        print(fips)
        # i dont think those are my fips


        county_names = []
        state_abbrs = []
        county_data = df_sample['County Name/State Abbreviation'].tolist()
        for i in range(len(county_data)):
            state_abbrs.append(county_data[i][len(county_data[i]) - 2:])
            county_names.append(county_data[i][:len(county_data[i]) - 4])

        # compares county names from two lists and returns the fips
        for county in County.objects.all():
            for i in range(len(fips)):
                if county.state.abbr == state_abbrs[i] and county.name == county_names[i]:
                    county.fips = fips[i]
                    county.save()
                    break


        # checks for county names that didn't make it into the above'
        # for county in County.objects.all():
        #     if county.fips.strip() == '':
        #         print(f'{county.id} {county.state.abbr} {county.name}')

