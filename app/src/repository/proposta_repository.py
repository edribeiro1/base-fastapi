from sqlalchemy.orm import Session

from src.model.proposta_model import PropostaModel


class PropostaRepository:
    @staticmethod
    async def get_propostas(db: Session, limit: int, offset: int):
        return db.query(PropostaModel).offset(offset).limit(limit).all()

    @staticmethod
    async def get_proposta(db: Session, id_proposta: int):
        return (
            db.query(PropostaModel)
            .filter(PropostaModel.cod_idt_prpt == id_proposta)
            .first()
        )
