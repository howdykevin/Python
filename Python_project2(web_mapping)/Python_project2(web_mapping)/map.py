import folium
import pandas

# creating a web application in your browser using folium
# tiles parameter changes the background color of the map. Location parameter accepts longitude and latitude coord
# tiles="Mapbox Bright"(eg)
map=folium.Map(location=[-20.917574,142.702789],zoom_start=6,tiles="Stamen Terrain")
data=pandas.read_csv("Volcanoes_USA.txt")
companian_card=pandas.read_csv("companion-card.csv")

# volcanoes
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

# companion card data.Businesses registered to provide discounts to holders of Seniors Card etc
Latitude=list(companian_card["Latitude"])
Longitude=list(companian_card["Longitude"])
Category=list(companian_card["Category"])
names=list(companian_card["Name"])

# color for volcanoes
def color_producer(metres):
    if metres >3000:
        return "red"
    elif metres <=3000 and metres>=2000:
        return "orange"
    else:
        return "green"

# color for category companion card
def category_colors(type):
    if type =="Health and Fitness":
        return "red"
    elif type =="Theatre and Arts":
        return "purple"
    elif type =="Sport and Recreation":
        return "green"
    elif type =="Festivals and Shows":
        return "beige"
    elif type =="Tourist Attraction":
        return "pink"
    elif type =="Cinema":
        return "black"
    elif type =="Council":
        return "blue"
    elif type =="Entertainment":
        return "cadetblue"
    elif type =="Transport":
        return "gray"
    elif type =="Learning & Personal Development":
        return "darkgreen"

def category_icons(type):
    if type =="Health and Fitness":
        return "apple"
    elif type =="Theatre and Arts":
        return "headphones"
    elif type =="Sport and Recreation":
        return "leaf"
    elif type =="Festivals and Shows":
        return "glass"
    elif type =="Tourist Attraction":
        return "flag"
    elif type =="Cinema":
        return "film"
    elif type =="Council":
        return "user"
    elif type =="Entertainment":
        return "music"
    elif type =="Transport":
        return "road"
    elif type =="Learning & Personal Development":
        return "book"

#introducing markers in your map
# introduce featureGroup as this is the one that can hold all features you wish to add in your map
# instead of calling map.addchild for every feature you wish to add, just call the variable with FeatureGroup
# It is much cleaner
fg=folium.FeatureGroup(name="Volcanoes")
fgp=folium.FeatureGroup(name="Population")
cc=folium.FeatureGroup(name="Business_discounts")



# zip allows the iteration of 2 different lists at the same time!
# you may get a blank web page if there are quotes in el. To avoid that change the popup argument
# to popup=folium.Popup(str(el),parse_html=True)

# volcanoes
for lt,ln,el in zip(lat,lon,elev):
    # fg.add_child(folium.Marker(location=[lt,ln],popup="ELEV:"+str(el)+" m",icon=folium.Icon(color_producer(el))))
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup="Elev:"+str(el)+"m",color=color_producer(el),fill=True,fill_opacity=1))
# adding multiple markers using for loop


# businesses
# when any of your text contains ' or &, you need to use parse_html=True or else your map wont work
# folium is using 4.1 version of font-awesome. there may be some icons that are not available. include prefix="fa".
for la,lo,cat,n2 in zip(Latitude,Longitude,Category,names):
    cc.add_child(folium.Marker(location=[la,lo],popup=folium.Popup(str(cat)+": "+str(n2),parse_html=True),icon=folium.Icon(color=category_colors(cat),icon=category_icons(cat),prefix="fa")))

# cc.add_child(folium.Marker(location=[-27.494896999999998,153.015954],popup="Hi",icon=folium.Icon(color="green")))


#GeoJson is used to plot maps using data.
# json files contain values in dict mode.In the lambda expression, you are accessing the feature's(key) values
# x['properties']['POP2005'] allows you to access the values of POP2005 key within properties(key) that is contained within features(key)
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<5000000
                                                     else 'orange' if 5000000<=x['properties']['POP2005']<10000000 else 'red'} ))

# there are 3 layers now on the map. The first is the base layer which has a Mapbox Bright tiles.
# the 2nd layer consists of the circle marker
# the 3rd layer consists of the polygon which indicates the population size of each country with varying colors.red,orange and green

# Now we are adding the functionality to on/off the polygon/marker layer
# add the functionality after including the feature group
map.add_child(fg)
map.add_child(fgp)
map.add_child(cc)
map.add_child(folium.LayerControl())

map.save("Map1.html")
# print(data)
