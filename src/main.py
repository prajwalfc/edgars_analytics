import sys
import csv
from functools import reduce


#####--------------------------HOFs Start ----------------#########################

def selectedFieldsOnly(row):
    return{"ip":row['ip'],row['ip']:(row['date'],row['time'],row['cik'],row['accession'],row['extention'])}

def reduceByIp(x,row):
    ip = row['ip']
    y=0
    #x[ip] = tuple()
    x[ip] = x.get(ip,tuple()) +(row[ip],)
    return x

def evluaterMapper(ip_body):
    ip,body = ip_body
    return (ip,len(body))

def

#####--------------------------HOFs Start ----------------#########################


if __name__ == "__main__":
    fileName = "../input/test.csv"
    with open(fileName, 'r') as fi:
        reader = csv.DictReader(fi)
        select_columns = list(map(selectedFieldsOnly,reader))
        groupByIp = reduce(reduceByIp,select_columns,{})
        evaluateForEachIp  = list(map(evluaterMapper,groupByIp.items()))

    print(evaluateForEachIp)