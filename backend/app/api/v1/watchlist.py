from fastapi import APIRouter

from app.schemas.watchlist import (
    WatchlistCreate
)

from app.services.watchlist_service import (
    WatchlistService
)

router = APIRouter(
    prefix="/api/v1/watchlist",
    tags=["Watchlist"]
)


@router.post("/")
def add_to_watchlist(
    data: WatchlistCreate
):

    return (
        WatchlistService
        .add_stock(
            data.dict()
        )
    )


@router.get(
    "/{investor_id}"
)
def get_watchlist(
    investor_id: str
):

    return (
        WatchlistService
        .get_watchlist(
            investor_id
        )
    )


@router.delete(
    "/{watchlist_id}"
)
def delete_watchlist(
    watchlist_id: str
):

    return {
        "deleted":
            WatchlistService
            .remove_stock(
                watchlist_id
            )
    }