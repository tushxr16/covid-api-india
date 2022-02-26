import pandas as pd
import os
import json

state='Bihar'

def getJsonofState(state):
    state = str(state)
    parentPath = os.path.abspath(os.getcwd())+'\\static\\data\\'
    listOfFiles = [x for x in os.listdir(parentPath) if (x.endswith('.csv'))]
    returnJson='Not Found'
    for idx,i in enumerate(listOfFiles):
        if i == state+'.csv':
            df = pd.read_csv('static\data\\'+i)
            df = df.T
            returnJson = df.to_json()
            return returnJson
    return returnJson

def getJsonofAllState():

    parentPath = os.path.abspath(os.getcwd())+'\\static\\data\\'
    listOfFiles = [x for x in os.listdir(parentPath) if (x.endswith('.csv'))]
    js = []
    for idx,i in enumerate(listOfFiles):
            df = pd.read_csv('static\data\\'+i)
            df = df.T
            jsonFile = os.path.abspath(os.getcwd())+'\\static\\dt.json'
            js.append(df.to_json())
    
    with open(jsonFile,'w') as outfile:
        outfile.write(json.dumps(js))

