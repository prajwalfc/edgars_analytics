import sys
import csv
from functools import reduce

#####--------------------------HOFs Start ----------------#########################

def convertTimeToInteger(timeString):
    hour,min,sec = timeString.split(":")
    #return timeString
    return (int(hour)*3600 + int(min)*60+int(sec))

def selectedFieldsOnly(row):
    return{"ip":row['ip'],row['ip']:(row['date'],convertTimeToInteger(row['time']),row['cik'],row['accession'],row['extention'])}

def reduceByIp(x,row):
    ip = row['ip']
    y=0
    #x[ip] = tuple()
    x[ip] = x.get(ip,tuple()) +(row[ip],)
    return x

def evluaterMapper(ip_body):
    ip,body = ip_body

    if ip == '117.91.2.iji':
        for row in body:
            print(row[1])
    return (ip,len(body))


#####--------------------------HOFs end ----------------#########################


if __name__ == "__main__":
    fileName = "../input/test.csv"
    with open(fileName, 'r') as fi:
        reader = csv.DictReader(fi)
        select_columns = list(map(selectedFieldsOnly,reader))
        groupByIp = reduce(reduceByIp,select_columns,{})
        evaluateForEachIp  = list(map(evluaterMapper,groupByIp.items()))

    print(evaluateForEachIp)
