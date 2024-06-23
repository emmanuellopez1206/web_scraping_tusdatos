from typing import List

from fastapi import APIRouter, Depends, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from config.database import Session
from controllers.scrapper import ScrapperFactory, ScrapperJudiciales
from middlewares.jwt_bearer import JWTBearer
from schemas.scrapper import ScrappingModel

scrapper_router = APIRouter()


@scrapper_router.post(
    "/scrapper",
)
def scrapper_judiciales(body: ScrappingModel):
    """
    Scrapping de datos judiciales
    """
    if body.actor_id:
        scrapper = ScrapperFactory.create_scrapper("actor", body.actor_id)
    if body.demandado_id:
        scrapper = ScrapperFactory.create_scrapper("demandado", body.demandado_id)
    judiciales = ScrapperJudiciales.get_causas(scrapper)

    informacion_juicio = ScrapperJudiciales.get_informacion_juicio(judiciales)
    incidente_judicatura = ScrapperJudiciales.get_incidente_judicatura(judiciales)

    return {"judiciales": judiciales}

