import csv

with open("/home/santhosh/Documents/python projects/intermediate_projects.py/csvexercise/weather_data.csv") as data_list:
    data = csv.reader(data_list)
    temp=[]
    for row in data:
        if row[1] != "temp":
          temperature=temp.append(int(row[1]))
    print(temp)