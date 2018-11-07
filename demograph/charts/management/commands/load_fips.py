
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

        # for i in range(len(fips)):
        #     print(f'{state_abbrs[i]} {county_names[i]} {fips[i]}')


        acs_counties = []
        for e in County.objects.all():
            acs_counties.append(e.name)
        # print(acs_counties)

        fips_index = []
        for x in county_names:
            if x in acs_counties:
                fips_index.append(f'{county_names.index(x)} + {x}')
            else:
                pass
        # print(fips_index)
        # I think the loop above goes through countynames, if it exists in acscounties, it
        # returns the index position. Then prints the index position with the countyname(x)
        # associated with it.

        # x =set(acs_counties) & set(county_names)
        # print(x)
                # if not County.objects.filter(fips=fips).exists():
                #     fips = County(fips=fips)
                #     fips.save()
                            # county, created = County.objects.get_or_create(fips=fips)

        # loop over the instances of County
        # for each County, loop over the records in fips
        # if the County and state abbreviation match
        # set the fips on the County and save it

                # state, created = State.objects.get_or_create(name=state_name)


