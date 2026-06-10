from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Body

from app.schemas.investor import (
    InvestorCreate
)

from app.services.investor_service import (
    add_investor,
    list_investors,
    get_investor,
    update_existing_investor,
    remove_investor
)

router = APIRouter(
    prefix="/api/v1/investors",
    tags=["Investors"]
)


@router.post("/")
def create_new_investor(
    investor: InvestorCreate
):

    return add_investor(
        investor.full_name,
        investor.email,
        investor.phone,
        investor.country
    )


@router.get("/")
def get_all():

    return list_investors()


@router.get("/{investor_id}")
def get_one(
    investor_id: str
):

    investor = get_investor(
        investor_id
    )

    if not investor:

        raise HTTPException(
            status_code=404,
            detail="Investor not found"
        )

    return investor


@router.put("/{investor_id}")
def update_one(
    investor_id: str,
    data: dict = Body(...)
):

    investor = update_existing_investor(
        investor_id,
        data
    )

    if not investor:

        raise HTTPException(
            status_code=404,
            detail="Investor not found"
        )

    return investor


@router.delete("/{investor_id}")
def delete_one(
    investor_id: str
):

    deleted = remove_investor(
        investor_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Investor not found"
        )

    return {
        "message": "Investor deleted successfully"
    }