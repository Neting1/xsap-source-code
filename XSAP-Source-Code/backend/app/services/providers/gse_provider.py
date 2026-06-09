import requests

from app.services.providers.base_provider import (
    MarketDataProvider
)


class GSEProvider(MarketDataProvider):

    BASE_URL = (
        "https://dev.kwayisi.org/apis/gse"
    )

    def get_stock(
        self,
        symbol
    ):

        response = requests.get(
            f"{self.BASE_URL}/equities/{symbol}"
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error":
            f"Unable to fetch {symbol}"
        }

    def get_all_stocks(self):

        response = requests.get(
            f"{self.BASE_URL}/equities"
        )

        if response.status_code == 200:
            return response.json()

        return []