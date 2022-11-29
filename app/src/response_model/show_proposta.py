from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class ShowProposta(BaseModel):
    cod_idt_prpt: int = Field(
        example=10, description='Id da proposta', alias='id_proposta'
    )
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
    dat_prpt: datetime = Field(
        example='2022-11-28 21:28:22',
        description='Data da inclusão',
        alias='data_hora_inclusao',
    )

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda date_to_str: date_to_str.strftime(
                '%Y-%m-%d %H:%M:%S'
            )
        }
