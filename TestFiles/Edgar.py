import json
import requests
from urllib.request import urlopen

border='======================================'
cik='0001883889'
url = requests.get("https://data.sec.gov/submissions/CIK0001883889.json")
text = url.text
print(type(text))
data = json.loads(text)
print(type(data))
# request = urlopen(url)
# # djson= request.read()
# # data = json.loads(djson) 
# print(request)
""" description = json.get("weather")[0].get("description")
tempmin = json.get("main").get("temp_min")
tempmax = json.get("main").get("temp_max")
tempfeel = json.get("main").get("feels_like")

print ("Today's forecast is", description)
print ("The temperature in "+city+" will be between", tempmin, " and", tempmax, "but it will feel like", tempfeel)
print(border)
print("What would you like to do next") """