from bs4 import BeautifulSoup
import requests
import re

from enum_covid_19 import covidEnumerate


class covidController:

    __covidModel = None
    __covidView = None

    def __init__(self,covidModel,covidView):
        self.__covidModel = covidModel
        self.__covidView = covidView
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
                    if(str(j).find("class")<0):
                        editHref = str(j).replace('/sito', covidEnumerate.covidEnum.URL.value + "sito")
                        filteredList.append(editHref)

            self.__covidModel.setHrefLinks(filteredList)
            self.__covidView.saveToFile(self.__covidModel)

        except IOError:
            print("[ERROR]: network error")



