
class covidModel:

    __hrefLinks = []

    def __init__(self,link):
        self.__hrefLinks = link

    def setHrefLinks(self,href):
        self.__hrefLinks(href)

    def getHrefLinks(self):
        return  self.__hrefLinks