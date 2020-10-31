import requests
import math

def get_location():
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    lat_testing=data['loc'].split(',')[0]
    lon_testing=data['loc'].split(',')[1]

    lat_testing=math.radians(float(lat_testing))
    lon_testing=math.radians(float(lon_testing))
    lat_office=math.radians(28.66010)
    lon_office=math.radians(77.12705)

    dlon=abs(lon_office-lon_testing)
    dlat=abs(lat_office-lat_testing)

    R=6373.0
    a = math.sin(dlat / 2)**2 + math.cos(lat_office) * math.cos(lat_testing) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    if(distance<0.5):
        return "In Office premises"
    else:
        return "Outside Office premises"

