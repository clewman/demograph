import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import pandas as pd
import resource
plotly.tools.set_credentials_file(username='cheryllewman', api_key='FHe2FrQ6UQXs6hvv8StD')

# Create random data with numpy
import numpy as np

#import requests


df = pd.read_csv('2011_us_ag_exports.csv')
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
# df = pd.read_csv(requests.get('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv').text)

print('!!!!!!!')

for col in df.columns:
    df[col] = df[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'], \
       [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]

df['text'] = df['state'] + '<br>' + \
             'Beef ' + df['beef'] + ' Dairy ' + df['dairy'] + '<br>' + \
             'Fruits ' + df['total fruits'] + ' Veggies ' + df['total veggies'] + '<br>' + \
             'Wheat ' + df['wheat'] + ' Corn ' + df['corn']

data = [dict(
    type='choropleth',
    colorscale=scl,
    autocolorscale=False,
    locations=df['code'],
    z=df['total exports'].astype(float),
    locationmode='USA-states',
    text=df['text'],
    marker=dict(
        line=dict(
            color='rgb(255,255,255)',
            width=2
        )),
    colorbar=dict(
        title="Millions USD")
)]

layout = dict(
    title='2011 US Agriculture Exports by State<br>(Hover for breakdown)',
    geo=dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'),
)

fig = dict(data=data, layout=layout)
url = py.plot(fig, filename='d3-cloropleth-map')
print(url)


