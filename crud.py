import pandas as pd
Andra_Pradesh=pd.read_csv()
Arunachal_Pradesh=pd.read_csv()
Assam=pd.read_csv()
Bihar=pd.read_csv()
Chhattisgarh=pd.read_csv()
Goa=pd.read_csv()
Gujrat=pd.read_csv()
Haryana=pd.read_csv()
Himachal_Pradesh=pd.read_csv()
Jharkhand=pd.read_csv()
Karnataka=pd.read_csv()
Kerala=pd.read_csv()
Madhya_Pradesh=pd.read_csv()
Maharashtra=pd.read_csv()
Manipur=pd.read_csv()
Meghalya=pd.read_csv()
Mizoram=pd.read_csv()
Nagaland=pd.read_csv()
Odisha=pd.read_csv()
Punjab=pd.read_csv()
Rajasthan=pd.read_csv()
Sikkim=pd.read_csv()
Tamil_Nadu=pd.read_csv()
Telangana=pd.read_csv()
Tripura=pd.read_csv()
Uttar_Pradesh=pd.read_csv()
Uttarakhand=pd.read_csv()
West_Bengal=pd.read_csv()
Andaman_and_Nicobar=pd.read_csv()
Chandigarh=pd.read_csv()
Delhi=pd.read_csv()
Jammu_and_Kashmir=pd.read_csv()
Ladakh=pd.read_csv()
Lakshdweep=pd.read_csv()
Puducherry=pd.read_csv()
Daman_and_Diu=pd.read_csv()

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
