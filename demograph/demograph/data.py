

import requests
import json

#api key/token
api_key = '35cfed388d369e78f29d2be64e38f5365b7c92c9'
api_url_base = 'https://api.census.gov/data/2014/pep/cochar6/variables.json'


def get_json(url):
    print('loading ' + url + '...')
    return json.loads(requests.get(url).text)

def get_data(title, datasets):
    for dataset in datasets['dataset']:
        #print(dataset['title'])
        if dataset['title'] == title:
            variables_url = dataset['c_variablesLink']
            values_url = dataset['c_valuesLink']
            variables = get_json(variables_url)
            values = get_json(values_url + '?key=' + api_key)

            print(variables)
            print()
            print()
            print()
            print()
            print()
            print(values)


def print_dataset_names(datasets):
    names = []
    for dataset in datasets['dataset']:
        names.append(dataset['title'])
    names.sort()
    print('\n'.join(names))

datasets = get_json(api_url_base)
# print(datasets)
# print_dataset_names(datasets)
dataset_name = 'Vintage 2017 Population Estimates: Population Estimates'
# dataset_name = 'County Total Population and Components of Change'
get_data(dataset_name, datasets)






