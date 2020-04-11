
from controller_covid_19 import covidController



if __name__ == "__main__":

    print("======= COVID ANSA WEB SCRAPER =========")
    print("do you want to save the results on file or print on console? (0 - file 1-console) ?")
    choice = int(input())

    mainControllerCovid = covidController()
    mainControllerCovid.downloadAnsaInfo(choice)



