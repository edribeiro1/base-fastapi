from sqlalchemy.orm import Session

from src.infrastructure.schema.proposta_schema import PropostaSchema
from src.input_model.create_proposta import CreateProposta


class PropostaRepository:
    @staticmethod
    async def count(db: Session):
        return db.query(PropostaSchema).count()

    @staticmethod
    async def pagination(db: Session, limit: int, offset: int):
        return db.query(PropostaSchema).offset(offset).limit(limit).all()

    @staticmethod
    async def find_by_id(db: Session, id_proposta: int):
        return (
            db.query(PropostaSchema)
            .filter(PropostaSchema.cod_idt_prpt == id_proposta)
            .first()
        )

    @staticmethod
    async def create(db: Session, create_proposta: CreateProposta):
        proposta_schema = PropostaSchema(**create_proposta.dict())
        db.add(proposta_schema)
        db.commit()
        db.refresh(proposta_schema)
        return proposta_schema
