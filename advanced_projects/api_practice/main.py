import requests
MYLAT=51.507351
MYLON=-0.127758
parameter ={
    'lat':MYLAT,
     "lng":MYLON,
     'formatted':0,
     }

response=requests.get("https://api.sunrise-sunset.org/json",params=parameter)

response.raise_for_status()
data=response.json()
sunrise =data['results']['sunrise']
sunset =data['results']['sunset']
print(sunrise)
from datetime import datetime as dt

now=dt.now()
#print(now)
print(sunrise.split('T')[1].split(':')[0])  