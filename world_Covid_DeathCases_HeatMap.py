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
covid1 = pd.json_normalize(covid1['Countries'],sep = ",")

df = pd.DataFrame(covid1) #to be able to manipulate the data
covid2 = df.drop(columns=['CountryCode','Slug','Date'], axis=1)

#code for map
m1 = folium.Map(tiles="StamenToner", min_zoom = 2)

# coordinates = pd.read_csv('https://raw.githubusercontent.com/Apurva-KIT/covid-map/master/country-coordinates-world.csv')
coordinates = pd.read_csv('https://raw.githubusercontent.com/VinitaSilaparasetty/covid-map/master/country-coordinates-world.csv')

covid_final = pd.merge(covid2,coordinates, on = 'Country')

#Heat Map
deaths = covid_final['TotalDeaths'].astype(float)
lat=covid_final['latitude'].astype(float)
lon=covid_final['longitude'].astype(float)
m1.add_child(HeatMap(zip(lat,lon,deaths),radius=0))

#Generate Circular Markers
covid_final.update(covid_final['TotalDeaths'].map('Total Deaths:{}'.format))

def plotDot(point):
    folium.CircleMarker(location=[point.latitude,point.longitude],
                        radius = 5,
                        weight = 2,
                        popup = [point.Country, point.TotalDeaths],
                        fill_color='#000000').add_to(m1)

covid_final.apply(plotDot, axis=1)
m1.save(outfile='HeatMap.html')
