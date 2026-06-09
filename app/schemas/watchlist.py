from pydantic import BaseModel


class WatchlistCreate(BaseModel):
    user_id: str
    stock_symbol: str


class WatchlistResponse(BaseModel):
    watchlist_id: str
    user_id: str
    stock_symbol: str
    created_at: str