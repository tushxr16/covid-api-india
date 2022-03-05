from datetime import datetime
import requests, argparse, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Argparse to work from cmdline

parser = argparse.ArgumentParser(
    description="This program uses selenium to crawl data from the official site https://www.mygov.in/covid-19 of Covid data.",
    prog="covidCrawl",
)
parser.add_argument("-n", type=str, help="Enter name of State")
args = parser.parse_args()

# Creating class for each state with private data.


class Region:
    def __init__(
        self,
        name,
        totalCases,
        newCases,
        totalActive,
        newActive,
        totalDis,
        newDis,
        totalDeath,
        newDeath,
    ):
        self.name = name
        self.__newCase = newCases
        self.__totalCase = totalCases
        self.__totalActive = totalActive
        self.__newActive = newActive
        self.__totalDis = totalDis
        self.__newDis = newDis
        self.__totalDeath = totalDeath
        self.__newDeath = newDeath
        # self.__activeRatio = activeRatio
        # self.__deathRatio = deathRatio

    def getTotalCases(self):
        return self.__totalCase

    def getNewCases(self):
        return self.__newCase

    def getTotalActive(self):
        return self.__totalActive

    def getNewActive(self):
        return self.__newActive

    def getTotalDeaths(self):
        return self.__totalDeath

    def getNewDeaths(self):
        return self.__newDeath

    def getTotalDis(self):
        return self.__totalDis

    def getNewDis(self):
        return self.__newDis

    # def getActiveRatio(self):
    #     return self.__activeRatio
    # def getDeathRatio(self):
    #     return self.__deathRatio

    def getName(self):
        return self.name


# Extraction of data from BS4


url = "https://www.mygov.in/covid-19"
fullCont = BeautifulSoup(requests.get(url).content, "html.parser")

data = []


def country():
    cont = fullCont.find("div", class_="information_row")
    caseIndia = cont.find("div", class_="iblock_text").get_text().split()
    region = Region("India")
    data.append(region)


# Use of Selenium to perform Js functions.


def openEdge():
    driver = webdriver.Edge()
    driver.minimize_window()
    driver.get(url)
    statePlus = driver.find_element(By.CLASS_NAME, "plus_icon")
    driver.execute_script("arguments[0].click();", statePlus)
    fullCont = driver.page_source
    driver.quit()
    fullCont = BeautifulSoup(fullCont, "html.parser")
    return fullCont


def state(data, fullCont):

    states = fullCont.find("div", class_="ind-mp_info").find_all("tr")
    for state in states:
        try:
            stateCont = state.find_all("td")
            name = str(stateCont[0].get_text()).replace(" ", "")

            newCase = str(stateCont[1].find("span").get_text())
            totalCase = str(stateCont[1].find("p").get_text())
            totalCase = totalCase[0 : len(totalCase) - len(newCase)]

            newActiveCase = str(stateCont[2].find("span").get_text())
            totalActiveCase = str(stateCont[2].find("p").get_text())
            totalActiveCase = totalActiveCase[
                0 : len(totalActiveCase) - len(newActiveCase)
            ]

            newDischargedCase = str(stateCont[3].find("span").get_text())
            totalDischargedCase = str(stateCont[3].find("p").get_text())
            totalDischargedCase = totalDischargedCase[
                0 : len(totalDischargedCase) - len(newDischargedCase)
            ]

            newDeaths = str(stateCont[1].find("span").get_text())
            totalDeaths = str(stateCont[1].find("p").get_text())
            totalDeaths = totalDeaths[0 : len(totalDeaths) - len(newDeaths)]

            reg = Region(
                name,
                totalCase,
                newCase,
                totalActiveCase,
                newActiveCase,
                totalDischargedCase,
                newDischargedCase,
                totalDeaths,
                newDeaths,
            )
            data.append(reg)
        except:
            pass
    return data


def writeOnCSV(data):
    for ind, reg in enumerate(data):
        name = reg.getName()
        filename = "data/" + name + ".csv"
        # Use 'a' to append, 'w' to overwrite.
        with open(filename, 'a+', newline='') as csvfile:
            today = str(datetime.utcnow().date())
            csvfile.seek(0)
            if csvfile.read().rfind(today) == -1:
                csvwriter = csv.writer(csvfile)
                # csvwriter.writerow(['TimeStamp','TOTAL_CASES', 'TOTAL_NEW_CASES', 'ACTIVE_CASES', 'NEW_ACTIVE_CASES', 'TOTAL_DISCHARGED',
                #                    'NEW_DISCHARGED', 'TOTAL_DEATHS', 'NEW_DEATHS'])       <-- Use this to write header.
                row = [
                    datetime.utcnow(),
                    reg.getTotalCases(),
                    reg.getNewCases(),
                    reg.getTotalActive(),
                    reg.getNewActive(),
                    reg.getTotalDis(),
                    reg.getNewDis(),
                    reg.getTotalDeaths(),
                    reg.getNewDeaths(),
                ]
                csvwriter.writerow(row)
            csvfile.close()
        print("CHECKED", "\t\t", ind + 1, "\t\t", name)


# country()

try:
    fullCont = openEdge()
except:
    print("Don't run this file in virtual env.")
    exit()

try:
    state(data, fullCont)
    try:
        writeOnCSV(data)
    except:
        print("Unable to write data on CSV.")
except:
    print("Can't get the data from states. Maybe the format of site is changed.")
    exit()

if args.n != None:
    print(
        "\n\tTotal Cases In India: "
        + data[0].getTotalCases()
        + "\n\tNew Cases In India: "
        + data[0].getNewCases()
        + "\n"
    )
    found = False
    nameState = args.n
    for s in data:
        if s.getName() == nameState:
            found = True
            print(
                "\n\tTotal Cases In {}: {}\n\tNew Cases In {}: {}\n".format(
                    nameState, s.getTotalCases(), nameState, s.getNewCases()
                )
            )
            break
    if found:
        pass
    else:
        print("\n\tTry again with correct name of State.\n")

exit()
