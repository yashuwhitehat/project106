import csv
import plotly.express  as px
import numpy as np
from setuptools import setup


def getdatasource(path):
    mark=[]
    days=[]
    with open(path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in  csv_reader:
            mark.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))

    return {"x":mark,"y": days}

def findcorrelation(ds):
    c=np.corrcoef(ds["x"],ds["y"])
    print(c)
def  setup():
    path= "Student Marks vs Days Present.csv"
    ds=getdatasource(path)
    findcorrelation(ds)

setup()
