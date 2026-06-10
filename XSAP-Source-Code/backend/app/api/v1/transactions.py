from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.transaction import (
    TransactionCreate
)

from app.services.transaction_service import (
    TransactionService
)

router = APIRouter(
    prefix="/api/v1/transactions",
    tags=["Transactions"]
)


@router.post("/")
def create_transaction(
    transaction: TransactionCreate
):

    return TransactionService.create_transaction(
        transaction.dict()
    )


@router.get("/")
def get_transactions():

    transactions = (
        TransactionService.get_all_transactions()
    )

    return {
        "total_transactions":
        len(transactions),
        "transactions":
        transactions
    }


@router.get("/{transaction_id}")
def get_transaction(
    transaction_id: str
):

    transaction = (
        TransactionService.get_transaction(
            transaction_id
        )
    )

    if not transaction:

        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction


@router.delete("/{transaction_id}")
def delete_transaction(
    transaction_id: str
):

    TransactionService.delete_transaction(
        transaction_id
    )

    return {
        "message":
        "Transaction deleted successfully"
    }