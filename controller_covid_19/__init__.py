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

    def downloadAnsaInfo(self):

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

            self.__covidView.printToConsole(self.__covidModel)

        except IOError:
            print("[ERROR]: network error")



