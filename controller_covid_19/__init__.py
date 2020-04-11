from bs4 import BeautifulSoup
import requests

from enum_covid_19 import covidEnumerate

class covidController:

    def __init__(self):
        pass

    def downloadAnsaInfo(self):

        try:
            print(covidEnumerate.covidEnum.URL.value)
            getAnsaInfo = requests.get(covidEnumerate.covidEnum.URL.value)
            responseAnsaInfo = BeautifulSoup(getAnsaInfo.text,"html.parser")
            print(responseAnsaInfo.text)
        except IOError:
            print("[ERROR]: network error")



        pass