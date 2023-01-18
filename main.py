# Select multiple points on a map and find the average distance between any two points
# Then generate a map showing the midpoint and the distances between each point

import folium
import geopy.distance

bMap = folium.Map(location=[39.8283,-98.5795], zoom_start=5)
folium.TileLayer('stamenwatercolor').add_to(bMap)