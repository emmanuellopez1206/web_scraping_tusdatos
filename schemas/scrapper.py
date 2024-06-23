from typing import List, Union
from pydantic import BaseModel, ConfigDict, EmailStr, model_validator
from pydantic import BaseModel


class ScrappingModel(BaseModel):
    actor_id: str = None
    demandado_id: str = None

    @model_validator(mode="after")
    def validate_model_scrapping(self) -> "ScrappingModel":
        """
        Validate the service_type field.
        """
        if self.actor_id is None and self.demandado_id is None:
            raise ValueError(
                "Se necesita el actor_id or demandado_id para realizar el scrapping"
            )
        return self
