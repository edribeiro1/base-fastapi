from typing import List, Union

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Query, Response, status
from sqlalchemy.orm.session import Session

from src.infrastructure.config.database import get_db
from src.infrastructure.repository.proposta_repository import \
    PropostaRepository
from src.input_model.create_proposta import CreateProposta, InputProposta
from src.response_model.show_proposta import ShowProposta

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
    summary='Listagem paginada de propostas',
    description='Listagem paginada de propostas',
    status_code=status.HTTP_200_OK,
    response_model=List[ShowProposta],
    tags=['Proposta'],
)
async def pagination(
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
    summary='Pegar proposta',
    description='Pegar os detalhes da proposta por id',
    status_code=status.HTTP_200_OK,
    response_model=ShowProposta,
    tags=['Proposta'],
)
async def find_by_id(id_proposta: int, db: Session = Depends(get_db)):
    proposta = await PropostaRepository.find_by_id(db, id_proposta)
    if not proposta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Proposta não encontrada',
        )
    return proposta


@app.post(
    path='/',
    summary='Criar proposta',
    description='Criar uma proposta',
    # response_class=Response,
    status_code=status.HTTP_201_CREATED,
    response_model=ShowProposta,
    tags=['Proposta'],
)
async def create(input_proposta: InputProposta, db: Session = Depends(get_db)):
    create_proposta = CreateProposta.parse_obj(input_proposta)
    proposta = await PropostaRepository.create(db, create_proposta)
    if not proposta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Não foi possível criar a proposta',
        )
    return proposta


if __name__ == '__main__':
    uvicorn.run('__main__:app', host='0.0.0.0', port=8080, reload=True)
