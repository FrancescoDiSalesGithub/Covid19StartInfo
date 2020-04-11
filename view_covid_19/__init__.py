from enum_covid_19 import covidEnumerate

import webbrowser
import os

class covidView:
    def __init__(self):
        pass

    def saveToFile(self,covidModel):
        fileOutput = open(covidEnumerate.covidEnum.FILENAMEOUTPUT.value,"w")
        filteredInfo = covidModel.getHrefLinks()

        for i in filteredInfo:
                fileOutput.write(str(i))
                fileOutput.write("<br/>")

        fileOutput.close()
        webbrowser.open("file://"+os.getcwd()+"/"+covidEnumerate.covidEnum.FILENAMEOUTPUT.value)

