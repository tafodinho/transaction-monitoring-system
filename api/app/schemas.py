from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class TransactionBase(BaseModel):
    """
        Schema base of how a request body and response body 
        should look like. It provides auto formating for both
        the request and response too
    """
    value: int
    receiver: str
    sender: str

class TransactionCreate(TransactionBase):
    """
        Schema to be used for the create transaction request
        body
    """
    pass

class Transaction(TransactionBase):
    """
        Schema to be used for every transaction response body
    """
    id: str
    confirmed: bool
    timestamp: datetime

    class Config:
        orm_mode = True

class TransactionUpdate(BaseModel):
    """
        Schema to be used for the update request body
    """
    confirmed: bool