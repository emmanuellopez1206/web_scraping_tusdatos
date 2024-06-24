from dateutil import parser
from controllers.scrapper import ScrapperJudiciales

from config.database import Session
from models.models import (
    IncidenteJudicaturaCompleto,
    InformacionJuicio,
    ListaIncidenteJudicatura,
    ListaLitiganteActor,
    ListaLitiganteDemandado,
    ActuacionJudicial,
)
from utils.utils import write_log


class SaveDataJudicial:
    @staticmethod
    def save(data):
        """
        Guarda los datos en la base de datos
        """
        ScrapperJudiciales.get_informacion_juicio(data)
        ScrapperJudiciales.get_incidente_judicatura(data)
        if not data:
            return
        session = Session()
        process_executed = data["process"]
        if process_executed == "Actor":
            tipo_actor = 1
        else:
            tipo_actor = 2
        write_log("Inicio de guardado de datos en la base de datos")
        for item in data["causas"]:
            try:
                fecha_ingreso = parser.isoparse(item["fechaIngreso"])
                juicio = InformacionJuicio(
                    idJuicio=item["idJuicio"],
                    tipo_actor=tipo_actor,
                    estadoActual=item["estadoActual"],
                    idMateria=item["idMateria"],
                    idProvincia=item.get("idProvincia"),
                    idCanton=item.get("idCanton"),
                    idJudicatura=item.get("idJudicatura"),
                    nombreDelito=item["nombreDelito"],
                    fechaIngreso=fecha_ingreso,
                    nombre=item.get("nombre"),
                    cedula=item.get("cedula"),
                    idEstadoJuicio=item.get("idEstadoJuicio"),
                    nombreMateria=item.get("nombreMateria"),
                )
                session.add(juicio)
                session.commit()
                session.refresh(juicio)
                juicio_id = juicio.id
                inci_judi = item.get("incidente_judicatura_completo")
                if inci_judi:
                    incidente_judicatura_completo = IncidenteJudicaturaCompleto(
                        informacion_juicio_id=juicio_id,
                        idJudicatura=inci_judi.get("idJudicatura"),
                        nombreJudicatura=inci_judi.get("nombreJudicatura"),
                        ciudad=inci_judi.get("ciudad"),
                        idJuicio=inci_judi.get("idJuicio"),
                    )
                    session.add(incidente_judicatura_completo)
                    session.commit()

                    # Refrescar la instancia para obtener el id autogenerado
                    session.refresh(incidente_judicatura_completo)
                    incidente_judicatura_completo_id = incidente_judicatura_completo.id

                    lst_inci_judi = inci_judi["lstIncidenteJudicatura"]
                    for inci in lst_inci_judi:
                        fecha_crea = parser.isoparse(inci["fechaCrea"])
                        lista_incidente_judicatura = ListaIncidenteJudicatura(
                            idIncidenteJudicaturaCompleto=incidente_judicatura_completo_id,
                            idIncidenteJudicatura=inci.get("idIncidenteJudicatura"),
                            idMovimientoJuicioIncidente=inci.get(
                                "idMovimientoJuicioIncidente"
                            ),
                            idJudicaturaDestino=inci.get("idJudicaturaDestino"),
                            fechaCrea=fecha_crea,
                            incidente=inci.get("incidente"),
                            litiganteActor=inci.get("litiganteActor"),
                            litiganteDemandado=inci.get("litiganteDemandado"),
                        )
                        session.add(lista_incidente_judicatura)
                        session.commit()

                        session.refresh(lista_incidente_judicatura)
                        lista_incidente_judicatura_id = lista_incidente_judicatura.id

                        if inci["lstLitiganteActor"]:
                            for liti_actor in inci["lstLitiganteActor"]:
                                lista_litigante_actor = ListaLitiganteActor(
                                    idListaIncidenteJudicatura=lista_incidente_judicatura_id,
                                    tipoLitigante=liti_actor.get("tipoLitigante"),
                                    nombresLitigante=liti_actor.get("nombresLitigante"),
                                    representadoPor=liti_actor.get("representadoPor"),
                                    idLitigante=liti_actor.get("idLitigante"),
                                )
                                session.add(lista_litigante_actor)
                                session.commit()
                                session.refresh(lista_litigante_actor)

                        if inci["lstLitiganteDemandado"]:
                            for liti_deman in inci["lstLitiganteDemandado"]:
                                lista_litigante_demandado = ListaLitiganteDemandado(
                                    idListaIncidenteJudicatura=lista_incidente_judicatura_id,
                                    tipoLitigante=liti_deman.get("tipoLitigante"),
                                    nombresLitigante=liti_deman.get("nombresLitigante"),
                                    representadoPor=liti_deman.get("representadoPor"),
                                    idLitigante=liti_deman.get("idLitigante"),
                                )
                                session.add(lista_litigante_demandado)
                                session.commit()
                                session.refresh(lista_litigante_demandado)

                        lst_act_judi = inci_judi["actuacion_judicial"]

                        for act_judi in lst_act_judi:
                            fecha = parser.isoparse(act_judi["fecha"])
                            actuacion_judicial = ActuacionJudicial(
                                idIncidenteJudicaturaCompleto=incidente_judicatura_completo_id,
                                codigo=act_judi.get("codigo"),
                                idJudicatura=act_judi.get("idJudicatura"),
                                idJuicio=act_judi.get("idJuicio"),
                                fecha=fecha,
                                tipo=act_judi.get("tipo"),
                                actividad=act_judi.get("actividad"),
                                visible=act_judi.get("visible"),
                                origen=act_judi.get("origen"),
                                idMovimientoJuicioIncidente=act_judi.get(
                                    "idMovimientoJuicioIncidente"
                                ),
                                ieTablaReferencia=act_judi.get("ieTablaReferencia"),
                                ieDocumentoAdjunto=act_judi.get("ieDocumentoAdjunto"),
                                escapeOut=act_judi.get("escapeOut"),
                                uuid=act_judi.get("uuid"),
                                alias=act_judi.get("alias"),
                                nombreArchivo=act_judi.get("nombreArchivo"),
                                tipoIngreso=act_judi.get("tipoIngreso"),
                                idTablaReferencia=act_judi.get("idTablaReferencia"),
                            )
                            session.add(actuacion_judicial)
                            session.commit()
                            session.refresh(actuacion_judicial)
            except Exception as e:
                write_log(f"Error al guardar datos en la base de datos: {e}")
        write_log("Fin de guardado de datos en la base de datos")
