import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash tutorials'),
    dcc.Graph(id='example',
              figure ={
                  'data': [
                      {'x': [1,2,3,4], 'y':[5,6,7,1], 'type':'line', 'name':'boats'},
                      {'x': [1, 5, 3, 43], 'y': [5, 11, 7, 1], 'type': 'bar', 'name': 'boats'},
                          ],
                  'layout': {
                      'title': 'Dash test graph'
                  }


              })
    ])

if __name__ == '__main__':
    app.run_server(debug=True)