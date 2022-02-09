import pandas as pd
import os

state='Bihar'

def getJsonofState(state):

    parentPath = os.path.abspath(os.getcwd())+'\\static\\data\\'
    listOfFiles = [x for x in os.listdir(parentPath) if (x.endswith('.csv'))]

    for idx,i in enumerate(listOfFiles):
        if i == state+'.csv':
            df = pd.read_csv('static\data\\'+i)
            df = df.T
            jsonFile = os.path.abspath(os.getcwd())+'\\static\\dt.json'
            with open(jsonFile,'a') as outfile:
                outfile.write(df.to_json())

def getJsonofAllState():

    parentPath = os.path.abspath(os.getcwd())+'\\static\\data\\'
    listOfFiles = [x for x in os.listdir(parentPath) if (x.endswith('.csv'))]

    for idx,i in enumerate(listOfFiles):
            df = pd.read_csv('static\data\\'+i)
            df = df.T
            jsonFile = os.path.abspath(os.getcwd())+'\\static\\dt.json'
            with open(jsonFile,'a') as outfile:
                outfile.write(df.to_json())

getJsonofAllState()