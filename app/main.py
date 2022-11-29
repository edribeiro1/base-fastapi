from typing import List, Union

import uvicorn
from fastapi import Depends, FastAPI, Query, status
from sqlalchemy.orm.session import Session

from src.config.db import get_db
from src.repository.proposta_repository import PropostaRepository
from src.schema.proposta_schema import ShowProposta

app = FastAPI(
    title='Propostas',
    description="""<b>Documentação do ECS de Proposta</b>""",
    openapi_url='/api/v1/openapi.json',
    contact={
        'description': 'PLDKYX',
        'email': 'edson.a.ribeiro@itau-unibanco.com.br',
    },
    redoc_url=None,
    # docs_url=None
)


@app.get(
    path='/',
    status_code=status.HTTP_200_OK,
    summary='Pegar todas as propostas',
    description='Pegar todas as propostas',
    response_model=List[ShowProposta],
    tags=['Proposta'],
)
async def get_all(
    limit: int = Query(default=10, ge=1, le=1000),
    offset: int = Query(default=0, ge=0, le=1000),
    status_analise: Union[str, None] = None,
    search: Union[str, None] = None,
    db: Session = Depends(get_db),
):
    propostas = await PropostaRepository.get_propostas(db, limit, offset)
    return propostas


@app.get(
    path='/{id_proposta}',
    status_code=status.HTTP_200_OK,
    response_model=ShowProposta,
    summary='Pegar proposta',
    description='Pegar os detalhes da proposta por id',
)
async def get_by_id(id_proposta: int, db: Session = Depends(get_db)):
    proposta = await PropostaRepository.get_proposta(db, id_proposta)
    return proposta


if __name__ == '__main__':
    uvicorn.run('__main__:app', host='0.0.0.0', port=8080, reload=True)
