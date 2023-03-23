import requests

url = 'http://localhost:5000/recommend'
r = requests.post(url,json={'rating':2, 'exp':9, 'location':6})

print(r.json())
