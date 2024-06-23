import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import select

from config.database import Session, engine
from middlewares.error_handler import ErrorHandler
from models.models import Base, TipoActor
from routers.scrapper import scrapper_router
from routers.user import user_router

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"
app.add_middleware(ErrorHandler)
app.include_router(scrapper_router)
app.include_router(user_router)

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def initialize_data():
    session = Session()
    try:
        if session.execute(select(TipoActor)).first() is None:
            nombres = ["Actor_ofendido", "Demandado_procesado"]
            for nombre in nombres:
                tipo_actor = TipoActor(nombre=nombre)
                session.add(tipo_actor)
                session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error al inicializar datos: {e}")
    finally:
        session.close()

initialize_data()
@app.get("/", tags=["home"])
def message() -> HTMLResponse:
    return "API Judiciales"
