from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class InputProposta(BaseModel):
    dsc_prpt: str = Field(
        example='Proposta X',
        description='Descrição da proposta',
        alias='descrica_proposta',
    )
    det_prpt: Optional[Dict[str, Any]] = Field(
        example={'teste': 123},
        description='Detalhes da proposta',
        alias='detalhes_proposta',
    )


class CreateProposta(InputProposta):
    dat_prpt: datetime = Field(
        alias='data_hora_inclusao', default=datetime.now()
    )

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
