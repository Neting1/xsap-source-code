import requests

from app.services.providers.base_provider import (
    MarketDataProvider
)


class GSEProvider(MarketDataProvider):

    BASE_URL = "https://dev.kwayisi.org/apis/gse"

    def get_stock(
        self,
        symbol: str
    ):

        try:

            response = requests.get(
                f"{self.BASE_URL}/live/{symbol}",
                timeout=10
            )

            if response.status_code == 200:
                return response.json()

            return {
                "error":
                f"Unable to fetch stock {symbol}"
            }

        except Exception as e:

            return {
                "error":
                str(e)
            }

    def get_all_stocks(self):

        try:

            response = requests.get(
                f"{self.BASE_URL}/live",
                timeout=10
            )

            if response.status_code == 200:
                return response.json()

            return []

        except Exception:

            return []