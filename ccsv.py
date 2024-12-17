import csv

with open('info.csv', 'r', newline="") as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
    print(type(line)) 