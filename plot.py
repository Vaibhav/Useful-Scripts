import plotly.plotly as py
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='ishuvaibhav', api_key='wv80v7y0b9')


data = [go.Scatter(
          x=['2013-10-04 22:23:00', '2013-11-04 22:23:00', '2013-12-04 22:23:00'],
          y=[1, 3, 6])]
py.iplot(data)
