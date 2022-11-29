from sqlalchemy import (JSON, BigInteger, Boolean, Column, DateTime,
                        ForeignKey, String)
from sqlalchemy.orm import relationship

from src.infrastructure.config.database import Base


class PropostaSchema(Base):
    __tablename__ = 'prpt'

    cod_idt_prpt = Column(BigInteger, primary_key=True, index=True)
    dsc_prpt = Column(String)
    det_prpt = Column(JSON)
    dat_prpt = Column(DateTime)
