from abc import ABC
from abc import abstractmethod


class MarketDataProvider(ABC):

    @abstractmethod
    def get_stock(
        self,
        symbol
    ):
        pass

    @abstractmethod
    def get_all_stocks(
        self
    ):
        pass