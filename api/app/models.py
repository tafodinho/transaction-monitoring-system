from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Computed, Index
from sqlalchemy.sql import func
from sqlalchemy.types import TypeDecorator

from database import Base

class Transaction(Base):
    """
        Transaction Model that is used to specify a schema 
        of how a transaction table should be created and how
        the records will look like with their specific times
    """

    __tablename__ = "transactions"

    id = Column(String, primary_key=True, nullable=False)
    value = Column(Integer, nullable=False)
    receiver = Column(String, nullable=False)
    confirmed = Column(Boolean, default=False)
    sender = Column(String, nullable=False)
    timestamp = Column(DateTime, default=func.now())