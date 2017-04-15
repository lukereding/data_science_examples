import os
import csv
from geopy.geocoders import Nominatim
from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Diamond, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)


# change dir
os.chdir("/Users/lukereding/Documents/art/")

# get locations
locations = []
with open("rows.csv?accessType=DOWNLOAD", "rb") as f:
    reader = csv.reader(f)
    for row in reader:
        locations.append(row[3][:-1] + " Austin TX")

# get lat and long
latitude = []
longitude = []
for x in locations:
    try:
        geolocator = Nominatim()
        location = geolocator.geocode(x)
        print(location.address)
        lat, long = location.latitude, location.longitude
        latitude.append(lat)
        longitude.append(long)
    except:
        pass


## plot

map_options = GMapOptions(lat=30.29, lng=-97.73, map_type="roadmap", zoom=11)

plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
)
plot.title.text = "Austin"

plot.api_key = os.environ['MAP_KEY'] # stored on local machine

source = ColumnDataSource(
    data=dict(
        lat=latitude,
        lon=longitude,
    )
)

circle = Diamond(x="lon", y="lat", size=15, fill_color="#E84F22", fill_alpha=0.5)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)