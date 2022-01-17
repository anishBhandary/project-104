import csv
from collections import Counter
with open('Weight.csv', newline = '')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

data = Counter(new_data)
mode_data_for_range = {
    "50 - 60":0, 
    "60 - 70":0,
    "70 - 80":0
}

for Weight,occurence in data.items():
    if(50 < float(Weight)<60):
        mode_data_for_range["50 - 60"]+= occurence
    
    elif(60 < float(Weight)<70):
        mode_data_for_range["60 - 70"]+= occurence

    elif(70 < float(Weight)<80):
        mode_data_for_range["70 - 80"]+= occurence


mode_range,mode_occurence = 0,0
for ranges,occurence in mode_data_for_range.items():
    if(occurence > mode_occurence):
        mode_range,mode_occurence = [int(ranges.split("-")[0]),int(ranges.split("-")[1])],occurence
    
mode = float((mode_range[0]+mode_range[1])/2)

print("Mode is",mode)

    


    
