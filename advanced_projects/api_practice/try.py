import requests
res= requests.get(url='https://spotthestation.nasa.gov/tracking_map.cfm')
res.raise_for_status()
data =res.json()
print(data)
