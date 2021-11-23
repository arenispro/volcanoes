import folium
import pandas

data = pandas.read_csv("JPVol.csv")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'blue'
    else:
        return 'red'

map=folium.Map(location=[36.20, 139.25],
                 zoom_start=7,
                 tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Volcanoes")


for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup =str(el) + "m",
    icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
       else 'red' if 10000000 <=x['properties']['POP2005']<20000000 else 'orange'} ))



map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("JapanVolMap.html")
