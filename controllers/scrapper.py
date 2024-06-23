from abc import ABC
import requests


class ScrapperCreation(ABC):
    def __init__(self, cedula):
        self.cedula = cedula
        self.scrapping_payload_body = {
            "numeroCausa": "",
            "actor": {
                "cedulaActor": "",
                "nombreActor": "",
            },
            "demandado": {
                "cedulaDemandado": "",
                "nombreDemandado": "",
            },
            "first": 0,
            "numeroFiscalia": "",
            "pageSize": 10,
            "provincia": "",
            "recaptcha": "verdad",
        }
        self.process_execute = ""

class ScrapperActor(ScrapperCreation):
    def __init__(self, cedula: str):
        super().__init__(cedula=cedula)
        self.scrapping_payload_body["actor"]["cedulaActor"] = self.cedula
        self.process_execute = "Actor"

class ScrapperDemandado(ScrapperCreation):
    def __init__(self, cedula: str):
        super().__init__(cedula=cedula)
        self.scrapping_payload_body["demandado"]["cedulaDemandado"] = self.cedula
        self.process_execute = "Demandado"

class ScrapperFactory:
    """
    Factory para crear los scrappers
    """

    @staticmethod
    def create_scrapper(type_scrapper, cedula) -> ScrapperCreation:
        if type_scrapper == "actor":
            return ScrapperActor(cedula)
        if type_scrapper == "demandado":
            return ScrapperDemandado(cedula)


class RequestsApi:
    @staticmethod
    def get_request(url, headers, params, payload):
        """
        Realiza un request get a una url
        """
        counter = 0
        maximo = 5
        while counter < maximo:
            response = requests.get(url, headers=headers, params=params, data=payload)
            if response.status_code == 200:
                return response.json()
            counter += 1

    @staticmethod
    def post_request(url, headers, params, payload):
        """
        Realiza un request post a una url
        """
        counter = 0
        maximo = 5
        while counter < maximo:
            response = requests.post(url, headers=headers, params=params, json=payload)
            if response.status_code == 200:
                return response.json()
            counter += 1


class ScrapperJudiciales:
    @staticmethod
    def get_causas(user_scrapper: ScrapperCreation):
        """
        Obtiene la cantidad de causas
        """
        params = {"page": 1, "size": 100}
        url_buscar_causas = "https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/buscarCausas"
        all_causas = []
        while True:
            causas = RequestsApi.post_request(
                url=url_buscar_causas,
                headers={"Content-Type": "application/json"},
                params=params,
                payload=user_scrapper.scrapping_payload_body,
            )
            if not causas:
                break
            params["page"] += 1
            all_causas.extend(causas)
        return {
            "causas": all_causas,
            "total": len(all_causas),
            "proceso_user":"proceso ejecutado con exito",
            "proceso_ejecutado": user_scrapper.scrapping_payload_body,
        }

    @staticmethod
    def get_informacion_juicio(judiciales: dict):
        """
        Obtiene la informacion de un juicio
        """

        for judicial in judiciales["causas"]:
            id_juicio = judicial["idJuicio"]
            url_informacion_juicio = f"https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/getInformacionJuicio/{id_juicio}"
            informacion_juicio = RequestsApi.get_request(
                url=url_informacion_juicio,
                headers={"Content-Type": "application/json"},
                params={},
                payload={},
            )
            judicial["informacion_juicio"] = informacion_juicio
            break


    @staticmethod
    def get_incidente_judicatura(judiciales: dict):
        """
        Obtiene los datos generales
        """

        for judicial in judiciales["causas"]:
            id_juicio = judicial["idJuicio"]
            url_incidente_judicatura = f"https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-CLEX-SERVICE/api/consulta-causas-clex/informacion/getIncidenteJudicatura/{id_juicio}"
            incidente_judicatura = RequestsApi.get_request(
                url=url_incidente_judicatura,
                headers={"Content-Type": "application/json"},
                params={},
                payload={},
            )
            incidente_judicatura_completo = incidente_judicatura[0]
            incidente_judicatura_completo["idJuicio"] = id_juicio
            judicial["incidente_judicatura_completo"] = incidente_judicatura_completo

            url_actuacion_judicial = "https://api.funcionjudicial.gob.ec/EXPEL-CONSULTA-CAUSAS-SERVICE/api/consulta-causas/informacion/actuacionesJudiciales"
            actuacion_judicial = RequestsApi.post_request(
                url=url_actuacion_judicial,
                headers={"Content-Type": "application/json"},
                params={},
                payload={
                    "aplicativo": "web",
                    "idIncidenteJudicatura": incidente_judicatura_completo["lstIncidenteJudicatura"][0]["idIncidenteJudicatura"],
                    "idJudicatura": incidente_judicatura_completo["idJudicatura"],
                    "idJuicio": incidente_judicatura_completo["idJuicio"],
                    "idMovimientoJuicioIncidente": incidente_judicatura_completo["lstIncidenteJudicatura"][0]["idMovimientoJuicioIncidente"],
                    "incidente": incidente_judicatura_completo["lstIncidenteJudicatura"][0]["incidente"],
                    "nombreJudicatura": incidente_judicatura_completo["nombreJudicatura"]
                }
            )
            judicial["incidente_judicatura_completo"]["actuacion_judicial"] = actuacion_judicial

            break
