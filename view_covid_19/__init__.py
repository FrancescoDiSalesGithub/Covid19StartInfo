from model_covid_19 import covidModel

class covidView:
    def __init__(self):
        pass

    def printToConsole(self,covidModel):
        filteredInfo = covidModel.getHrefLinks()

        for i in filteredInfo:
            print(i)

