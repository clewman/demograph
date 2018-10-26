import re
import json
import requests
from census import Census
from us import states

census_api_key = "35cfed388d369e78f29d2be64e38f5365b7c92c9"
# open the url and the screen name
# (The screen name is the screen name of the user for whom to return results for)
url = 'https://api.census.gov/data.json'

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.loads(requests.get(url).text)

# print the result


text_data = re.findall(r'(\a)', url)
print(text_data)
# data = []


search_value = input("Enter a date with the format 00-JAN-YEAR: ")


def row_search(text_data, search_value):
    for x in text_data:
        if x[0] == search_value:
            return x[1]


row_search(text_data, search_value)
rainfall = int(row_search(text_data, search_value)) * .01

print(f'The rain on {search_value} was: {rainfall} of an inch.  ')



print(data)