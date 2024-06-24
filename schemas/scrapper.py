from pydantic import BaseModel, model_validator
from pydantic import BaseModel


class ScrappingModel(BaseModel):
    actor_id: str = None
    demandado_id: str = None

    @model_validator(mode="after")
    def validate_model_scrapping(self) -> "ScrappingModel":
        """
        Valida el campo service_type, si no se encuentra en la lista de opciones
        """
        if self.actor_id is None and self.demandado_id is None:
            raise ValueError(
                "Se necesita el actor_id or demandado_id para realizar el scrapping"
            )
        return self
