from pydantic import BaseModel


class WatchlistCreate(BaseModel):

    investor_id: str
    stock_symbol: str


class WatchlistResponse(BaseModel):

    watchlist_id: str
    investor_id: str
    stock_symbol: str
    created_at: str