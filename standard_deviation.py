import csv
import math

with open("data.csv", newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    totall_enteries=len(data)
    totall=0
    for i in data:
        totall=totall+int(i)
    mean=totall/totall_enteries
    return mean

squared_list=[]
for j in data:
    a=int(j)-mean(data)
    a=a**2
    squared_list.append(a)

sum=0
for h in squared_list:
    sum=sum+h

result=sum/(len(data)-1)
standard_deviation=math.sqrt(result)
print(standard_deviation)