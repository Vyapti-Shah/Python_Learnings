#Working with CSV and JSON files in Python
import csv
rows = [['Name', 'Age'],
        ['Vyapti', 20],
        ['Sejal', 35]]
with open('Working_with_CSV.csv', mode='w', newline='') as csv_file: #newline='' to avoid blank lines between rows in Windows
    writer = csv.writer(csv_file)
    writer.writerows(rows)
   
data_csv = [{'Name': 'Vyapti', 'Age': 20, 'City': 'Los Angeles'},
        {'Name': 'Sejal', 'Age': 35, 'City': 'New York'}]
with open('Working_with_CSV.csv', mode='a', newline='') as csv_file: #Append mode to add more rows
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()  #Write header only once
    for row in data_csv:
        writer.writerow(row) 

import json
data = {'name': 'Vyapti', 'age': 20, 'city': 'Los Angeles'},{'name': 'Sejal', 'age': 35, 'city': 'New York'}
with open('Working_with_JSON.json', 'w') as json_file:
    json.dump(data, json_file,indent=4) #dump() method writes a Python object into a JSON file
                                        #indent=4 for formatting the JSON file with an indentation of 4 spaces
