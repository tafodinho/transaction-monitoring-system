"""
    this crud file contains all the methods that are used by the main.py
    file to perform database operations. They are abstracted in this file
    and made pure functions so that they can easily be revamped and made
    reusable for other modules
 """

from sqlalchemy.orm import Session
from sqlalchemy import or_, Integer
from models import Transaction
from schemas import TransactionCreate, TransactionUpdate


def get_transaction(db: Session, transaction_id: str):
    """
        Function that runs a query to reuturn a transaction 
        with a specified id
    """

    return db.query(Transaction).filter(Transaction.id == transaction_id).first()


def get_transaction_by_date_range(db: Session, email: str, start_time: str, end_time: str):
    """
        Function that runs a query to reuturn a list of transactions
        within a specified timerange
    """

    return db.query(Transaction).filter(Transaction.timestamp >= start_time, Transaction.timestamp <= end_time).all()


def get_transactions(db: Session, skip: int = 0, limit: int = 1000):
    """
        Function that runs a query to reuturn all transactions in 
        the database
    """

    return db.query(Transaction).offset(skip).limit(limit).all()


def create_transaction(db: Session, transaction: TransactionCreate, id: str):
    """
        Function that creates a new transaction record in the database
    """

    db_transaction = Transaction(id=id, **transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def update_transaction(db: Session, transaction_id: str, transaction: TransactionUpdate):
    """
        Function that runs a query to update a transaction record in the db
        with a specified trasaction_id
    """

    db.query(Transaction).filter(Transaction.id == transaction_id).update({**transaction.dict()})
    db.commit()
    response =  db.query(Transaction).filter(Transaction.id == transaction_id).first()
    return response

def search_transactions(db: Session, search_word: str, value: Integer):
    """
        Function that runs a query to search and return for a transaction 
        that includes a particular phrase
    """

    return db.query(Transaction).filter(
        or_(
            Transaction.id.like(f"%{search_word}%"),
            # Transaction.value.match(value),
            Transaction.sender.like(f"%{search_word}%"),
            Transaction.receiver.like(f"%{search_word}%")
        )
        ).all()
    

    
