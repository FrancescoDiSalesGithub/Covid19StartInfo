from model_covid_19 import covidModel

class covidView:
    def __init__(self):
        pass

    def printToFile(self,path,covidModel):
        outputfile = open(path,"w+")
        filteredInfo = covidModel.getHrefLinks()

        for i in filteredInfo:
            outputfile.write(i)
        outputfile.close()

    def printToConsole(self,covidModel):
        hrefList = covidModel.getHrefLinks()

        for i in hrefList:
            print(i)

