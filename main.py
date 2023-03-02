# Select multiple points on a map and find the average distance between any two points
# Then generate a map showing the midpoint and the distances between each point

import folium
import geopy.distance

# Create template map, centered on US
bMap = folium.Map(location=[39.8283,-98.5795], zoom_start=5)
folium.TileLayer('stamenwatercolor').add_to(bMap)

cds = [] # Coordinate array
for j in range(2):
    ptLat = float(input("Enter the lattitude: "))
    ptLong = float(input("Enter the longitude: "))
    cds.append((ptLat,ptLong))


cumulDist = [] # distance between each nC2 points

for index in range(len(cds)):
    folium.CircleMarker(cds[index]).add_to(bMap)
    # TODO: add text on screen listing the coords and the avg distance
    for i in range(len(cds)):
        #print(cds[index],cds[i])
        cumulDist.append(geopy.distance.geodesic(cds[index],cds[i]).miles)
        folium.PolyLine(locations=(cds[index],cds[i]),color="red",opacity=0.2).add_to(bMap)