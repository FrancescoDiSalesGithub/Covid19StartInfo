from controller_covid_19 import covidController

from model_covid_19 import covidModel
from view_covid_19 import covidView


if __name__ == "__main__":

    print("======= COVID ANSA WEB SCRAPER =========")

    modelCovid = covidModel(None)
    viewCovid = covidView()
    mainControllerCovid = covidController(modelCovid,viewCovid)

    mainControllerCovid.downloadAnsaInfo()