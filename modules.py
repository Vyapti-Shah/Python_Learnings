#Modules: math, datetime, random, json, time, requests, numpy, pandas, matplotlib, sklearn, tensorflow, flask, django, seaborn, beautifulsoup4
from math import sqrt
a = 16
result = sqrt(a)
print("Square root of", a, "is", result)

from datetime import datetime
now = datetime.now()
print("Current date and time:", now)

import random
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

import json
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data) #dumps() method converts a Python object into a JSON string
print("JSON data:", json_data)
