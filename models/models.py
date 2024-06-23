from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from config.database import Base


class TipoActor(Base):
    __tablename__ = "tipo_actor"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)


class InformacionJuicio(Base):
    __tablename__ = "informacion_juicio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_actor = Column(Integer, ForeignKey("tipo_actor.id"))
    idJuicio = Column(Integer)
    estadoActual = Column(String)
    idMateria = Column(Integer)
    idProvincia = Column(Integer)
    idCanton = Column(Integer)
    idJudicatura = Column(Integer)
    nombreDelito = Column(String)
    fechaIngreso = Column(String)
    nombre = Column(String)
    cedula = Column(Integer)
    idEstadoJuicio = Column(Integer)
    nombreMateria = Column(String)
    nombreEstadoJuicio = Column(String)
    nombreJudicatura = Column(String)
    nombreTipoResolucion = Column(String)
    nombreTipoAccion = Column(String)
    fechaProvidencia = Column(String)
    nombreProvidencia = Column(String)
    nombreProvincia = Column(String)
    iedocumentoAdjunto = Column(String)


class IncidenteJudicaturaCompleto(Base):
    __tablename__ = "incidente_judicatura_completo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    informacion_juicio_id = Column(Integer, ForeignKey("informacion_juicio.id"))
    idJudicatura = Column(Integer)
    nombreJudicatura = Column(String)
    ciudad = Column(String)
    idJuicio = Column(Integer)


class ActuacionJudicial(Base):
    __tablename__ = "actuacion_judicial"
    id = Column(Integer, primary_key=True, autoincrement=True)
    idIncidenteJudicaturaCompleto = Column(
        Integer, ForeignKey("incidente_judicatura_completo.id")
    )
    codigo = Column(Integer)
    idJudicatura = Column(Integer)
    idJuicio = Column(Integer)
    fecha = Column(String)
    tipo = Column(String)
    actividad = Column(String)
    visible = Column(String)
    origen = Column(String)
    idMovimientoJuicioIncidente = Column(Integer)
    ieTablaReferencia = Column(String)
    ieDocumentoAdjunto = Column(String)
    escapeOut = Column(Boolean)
    uuid = Column(String)
    alias = Column(String)
    nombreArchivo = Column(String)
    tipoIngreso = Column(String)
    ieTablaReferencia = Column(String)


class ListaIncidenteJudicatura(Base):
    __tablename__ = "lista_incidente_judicatura"

    id = Column(Integer, primary_key=True, autoincrement=True)
    idIncidenteJudicaturaCompleto = Column(
        Integer, ForeignKey("incidente_judicatura_completo.id")
    )
    idIncidenteJudicatura = Column(Integer)
    idMovimientoJuicioIncidente = Column(Integer)
    idJudicaturaDestino = Column(Integer)
    fechaCrea = Column(String)
    incidente = Column(Integer)
    litiganteActor = Column(String)
    litiganteDemandado = Column(String)


class ListaLitiganteActor(Base):
    __tablename__ = "lista_litigante_actor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    idListaIncidenteJudicatura = Column(
        Integer, ForeignKey("lista_incidente_judicatura.id")
    )
    tipoLitigante = Column(String)
    nombresLitigante = Column(String)
    representadoPor = Column(String)
    idLitigante = Column(Integer)


class ListaLitiganteDemandado(Base):
    __tablename__ = "lista_litigante_demandado"

    id = Column(Integer, primary_key=True, autoincrement=True)
    idListaIncidenteJudicatura = Column(
        Integer, ForeignKey("lista_incidente_judicatura.id")
    )
    tipoLitigante = Column(String)
    nombresLitigante = Column(String)
    representadoPor = Column(String)
    idLitigante = Column(Integer)
