
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

        county_names = []
        state_abbrs = []
        county_data = df_sample['County Name/State Abbreviation'].tolist()
        for i in range(len(county_data)):
            state_abbrs.append(county_data[i][len(county_data[i]) - 2:])
            county_names.append(county_data[i][:len(county_data[i]) - 4])

        # loop over the county names
        # check if a county with that fips
        # if it doesn't, create it and save it




        for i in range(len(county_names)):
            # print(state_abbrs[i])
            state_abbrs[i] = state_abbrs[i].upper()
            state = State.objects.get(abbr=state_abbrs[i])
            if not County.objects.filter(fips=fips[i], state_id=state.id, name=county_names[i]).exists():
                county = County(name=county_names[i], fips=fips[i], state=state)
                county.save()

