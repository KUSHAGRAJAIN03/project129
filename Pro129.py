import pandas as pd
import csv
data= []
data2 = []
with open ("project127.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
with open ("project128.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data2.append(row)
radius_list = list(data)
h1 = data[0]
h2 =data2[0]
headers = h1+h2
remaining_data = data[1:]
remaining_data2 = data2[1:]
for i in remaining_data:
    radius = i[4]
    if radius.lower() == "unknown":
        radius.remove(i)
        continue
    else :
        radius_value = float(radius)*0.102763
        i[4] = radius_value
        data[4].append(i[4])
    mass = i[3]
    if mass.lower() == "unknown":
        mass.remove(i)
        continue
    else:
        mass = i[3]
        mass_value = float(mass)*0.000954588
        i[3] = mass_value
        data[3].append(i[3])

for i in remaining_data2:
    radius2 = i[4]
    if radius2.lower() == "unknown":
        radius2.remove(i)
        continue
    else :
        radius_value2 = float(radius2)*0.102763
        i[4] = radius_value2
        data2[4].append(i[4])
    mass2 = i[3]
    if mass2.lower() == "unknown":
        mass2.remove(i)
        continue
    else:
        mass_value2 = float(mass2)*0.000954588
        i[3] = mass_value2
        data2[3].append(i[3])
        print(i[3])
data_final = []
for index,data_row in enumerate(data):
    data_final.append(data[index]+data2[index])

with open ("Project129.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(data_final)
    
