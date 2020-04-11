from model_covid_19 import covidModel
import webbrowser
import os

class covidView:
    def __init__(self):
        pass

    def printToConsole(self,covidModel):
        filteredInfo = covidModel.getHrefLinks()

        for i in filteredInfo:
            print(i)

    def saveToFile(self,covidModel):
        fileOutput = open("result.html","w")
        filteredInfo = covidModel.getHrefLinks()

        for i in filteredInfo:
                fileOutput.write(str(i))
                fileOutput.write("<br/>")

        fileOutput.close()
        webbrowser.open("file://"+os.getcwd()+"/result.html")

