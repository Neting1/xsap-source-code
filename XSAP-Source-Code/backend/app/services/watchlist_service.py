from datetime import datetime

from app.repositories.watchlist_repository import (
    WatchlistRepository
)


class WatchlistService:

    @staticmethod
    def add_stock(data):

        symbol = (
            data["stock_symbol"]
            .upper()
            .strip()
        )

        existing = (
            WatchlistRepository
            .get_watchlist_item(
                data["user_id"],
                symbol
            )
        )

        if existing:

            return {
                "message":
                f"{symbol} already exists in watchlist"
            }

        data["stock_symbol"] = symbol

        data["created_at"] = (
            datetime.utcnow()
            .isoformat()
        )

        return (
            WatchlistRepository
            .create_watchlist(data)
        )

    @staticmethod
    def get_watchlist(
        user_id
    ):

        return (
            WatchlistRepository
            .get_user_watchlist(
                user_id
            )
        )

    @staticmethod
    def remove_stock(
        watchlist_id
    ):

        return (
            WatchlistRepository
            .delete_watchlist(
                watchlist_id
            )
        )