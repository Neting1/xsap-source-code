from app.repositories.investor_repository import (
    create_investor,
    get_all_investors,
    get_investor_by_id,
    update_investor,
    delete_investor
)


def add_investor(
    full_name,
    email,
    phone,
    country
):

    investor = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "country": country,
        "status": "active"
    }

    return create_investor(
        investor
    )


def list_investors():

    return get_all_investors()


def get_investor(
    investor_id
):

    return get_investor_by_id(
        investor_id
    )


def update_existing_investor(
    investor_id,
    data
):

    return update_investor(
        investor_id,
        data
    )


def remove_investor(
    investor_id
):

    return delete_investor(
        investor_id
    )