from typing import List
import socketio
import websockets
import uuid
import time
import json
import re

from fastapi_socketio import SocketManager

from fastapi import Depends, FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session


import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
sm = SocketManager(app=app, cors_allowed_origins=[])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.sio.on('connect')
async def handle_connect(sid, *args, **kwargs):
    """
        function  that is executed when our frontend client 
        connects to the server socket
    """

    await app.sio.emit('lobby', 'User joined')


@app.post("/api/v1.0/transactions/", response_model=schemas.Transaction)
async def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    """
        Create Transaction endpoint: endpoint that we call when
        we want to create a new tranaction.

        Request and response data format can all be found 
        on the the OpenAPI docs at http://127.0.0.1:8000/docs
    """

    transaction_id = str(uuid.uuid1())
    db_transaction = crud.get_transaction(db, transaction_id)
    if db_transaction:
        return {"data": "ID already exist"}
    transaction = crud.create_transaction(db, transaction, transaction_id)
    await sm.emit('create_transaction', jsonable_encoder(transaction))
    return transaction


@app.get("/api/v1.0/transactions/", response_model=List[schemas.Transaction])
def get_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
        Get Transaction endpoint: endpoint that we use to get all 
        available tranasctions in the database

        Request and response data format can all be found 
        on the the OpenAPI docs at http://127.0.0.1:8000/docs
    """

    transactions = crud.get_transactions(db, skip=skip, limit=limit)
    
    return transactions


@app.get("/api/v1.0/transactions/{transaction_id}", response_model=schemas.Transaction)
async def get_transaction(transaction_id: str, db: Session = Depends(get_db)):
    """
        Create Transaction by Id endpoint: endpoint to get transaction from db 
        by specifying a transaction ID

        Request and response data format can all be found 
        on the the OpenAPI docs at http://127.0.0.1:8000/docs
    """

    transaction = crud.get_transaction(db, transaction_id=transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.patch("/api/v1.0/transactions/{transaction_id}", response_model=schemas.Transaction)
def update_transaction(transaction_id: str, transaction: schemas.TransactionUpdate, db: Session = Depends(get_db)):
    """
        Update Transaction by Id endpoint: endpoint to get update Tranaction 
        items in system by specifying the ID and passing the value and attribute
        to change

        Request and response data format can all be found 
        on the the OpenAPI docs at http://127.0.0.1:8000/docs
    """

    transaction = crud.update_transaction(db, transaction_id, transaction)
    return transaction


@app.get("/api/v1.0/transactions/", response_model=List[schemas.Transaction])
def get_transactions_in_range(start_time: str, end_time: str, db: Session = Depends(get_db)):
    """
        Get transaction in specified Time range: endpoint to get transaction 
        in a specified time range

        Request and response data format can all be found 
        on the the OpenAPI docs at http://127.0.0.1:8000/docs
    """

    transaction = crud.update_transaction(db, transaction_id, start_time, end_time)
    return transaction

@app.get("/api/v1.0/transactions/search/", response_model=List[schemas.Transaction])
def search_transactions(search_word: str, db: Session = Depends(get_db)):
    """
        Search transaction: endpoint to search for transactions
        by passing a phrase

        Request and response data format can all be found 
        on the the OpenAPI docs at http://127.0.0.1:8000/docs
    """
    if isint(search_word):
        value = int(search_word)
    else:
        value = 0
    transactions = crud.search_transactions(db, search_word, value)
    return transactions

def isint(value):
  try:
    int(value)
    return True
  except ValueError:
    return False