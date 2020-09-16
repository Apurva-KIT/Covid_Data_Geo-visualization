import json
import folium
import requests
import mimetypes
import http.client
import pandas as pd
from folium.plugins import HeatMap
from pandas.io.json import json_normalize

conn = http.client.HTTPSConnection("api.covid19api.com")
payload = ''
headers = {}
conn.request("GET","/summary", payload,headers)
res = conn.getresponse()
data = res.read().decode('UTF-8')

covid1 = json.loads(data)
# covid1 = pd.json_normalize(covid1['Countries'],sep = ",")

# df = pd.DataFrame(covid1) #to be able to manipulate the data
# covid2 = df.drop(columns=['CountryCode','Slug','Date'], axis=1)
#
#
# #code for map
# m = folium.Map(tiles="Stamen Terrain", min_zoom = 1.5)
#
# url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
# country_shapes = f'{url}/world-countries.json'
#
#
# folium.Choropleth(
#     geo_data = country_shapes,
#     min_zoom = 3,
#     name = 'Covid-19',
#     data = covid2,
#     columns = ['Country','TotalConfirmed'],
#     key_on = 'feature.properties.name',
#     fill_color = 'OrRd',
#     nan_fill_color = 'black',
#     legend_name = 'Total Confirmed Covid Cases',
# ).add_to(m)
#
#
# #Generate Circular Markers
# covid2.update(covid2['TotalConfirmed'].map('Total Confirmed:{}'.format))
# covid2.update(covid2['TotalRecovered'].map('Total Recovered:{}'.format))
#
# coordinates = pd.read_csv('https://raw.githubusercontent.com/Apurva-KIT/covid-map/master/country-coordinates-world.csv')
# print(coordinates)
#
# covid_final = pd.merge(covid2,coordinates, on = 'Country')
#
# def plotDot(point):
#     folium.CircleMarker(location=[point.latitude, point.logitude],
#                         radius=5,
#                         weight=2,
#                         popup=[point.Country, point.TotalConfirmed, point.TotalRecovered],
#                         fill_color='#000000').add_to(m)
#
# covid_final.apply(plotDot, axis=1)
#
# m.fit_bounds(m.get_bounds())
# m.save(outfile='map.html')

print(covid1)
