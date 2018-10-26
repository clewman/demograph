#Playing around with the api data


import json
import requests


def get_json(url):
    print('loading ' + url + '...')
    return json.loads(requests.get(url).text)


year = '/2015'
variables = 'NAME,B17003_002E'
geography = 'county:*'
dataset_name = '/acs1'
# url = 'https://api.census.gov/data/2014/pep/cochar6?get=SEX,STNAME,HISP,RACE6,CTYNAME,POP&for=county:*&DATE=7&AGEGRP=0'
url = 'https://api.census.gov/data' + year + dataset_name + "?get=" + variables + '&for=' + geography


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
    # print(row['STNAME'] + ' - ' + row['CTYNAME'] + ' - ' + row['POP'] + ' - ' + row['RACE6'])
    print(f"{row['NAME']} total: {row['B17003_002E']}")
