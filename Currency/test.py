import csv
with open('rates.csv' ,newline='') as csvfile:
   
    reader = csv.DictReader(csvfile)