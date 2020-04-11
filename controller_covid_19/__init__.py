from bs4 import BeautifulSoup
import requests
import re

from enum_covid_19 import covidEnumerate
from model_covid_19 import covidModel
from view_covid_19 import covidView

class covidController:

    __covidModel = None
    __covidView = None

    def __init__(self):
        pass

    def downloadAnsaInfo(self,choice):

        try:
            getAnsaInfo = requests.get(covidEnumerate.covidEnum.URL.value)
            responseAnsaInfo = BeautifulSoup(getAnsaInfo.text,"html.parser")

            listTags = covidEnumerate.covidEnum.TAGS.value
            filteredList = []

            for i in listTags:
                hrefLinks = responseAnsaInfo.find_all(href=re.compile(i))
                for j in hrefLinks:
                    filteredList.append(j)

            self.__covidModel = covidModel(filteredList)
            self.__covidView = covidView()

            if choice == 0:
                print("insert path:")
                path=input()
                self.__covidView.printToFile(path,self.__covidModel)
            elif choice == 1:
                self.__covidView.printToConsole(self.__covidModel)
            else:
                raise Exception

        except IOError:
            print("[ERROR]: network error")
        except Exception:
            print("Scelta non valida ")


