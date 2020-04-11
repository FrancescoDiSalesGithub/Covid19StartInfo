from controller_covid_19 import covidController



if __name__ == "__main__":

    print("======= COVID ANSA WEB SCRAPER =========")


    mainControllerCovid = covidController()
    mainControllerCovid.downloadAnsaInfo()