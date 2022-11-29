from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class ShowProposta(BaseModel):
    id: int = Field(
        example=10, description='Id da proposta', alias='cod_idt_prpt'
    )
    descricao: str = Field(
        example='Proposta X',
        description='Descrição da proposta',
        alias='dsc_prpt',
    )
    detalhes: Optional[Dict[str, Any]] = Field(
        example='Proposta X',
        description='Detalhes da proposta',
        alias='det_prpt',
    )
    data_hora_inclusao: datetime = Field(
        example='Proposta X',
        description='Detalhes da proposta',
        alias='dat_prpt',
    )

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
