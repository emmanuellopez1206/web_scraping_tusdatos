from fastapi import APIRouter, BackgroundTasks
from controllers.scrapper import ScrapperFactory, ScrapperJudiciales
from schemas.scrapper import ScrappingModel
from services.scrapper import SaveDataJudicial

scrapper_router = APIRouter()


@scrapper_router.post(
    "/scrapper",
)
def scrapper_judiciales(body: ScrappingModel, background_tasks: BackgroundTasks):
    """
    Scrapping de datos judiciales
    """
    if body.actor_id:
        scrapper = ScrapperFactory.create_scrapper("actor", body.actor_id)
    if body.demandado_id:
        scrapper = ScrapperFactory.create_scrapper("demandado", body.demandado_id)
    judiciales = ScrapperJudiciales.get_causas(scrapper)

    background_tasks.add_task(SaveDataJudicial.save, judiciales)

    return {"judiciales": judiciales}
