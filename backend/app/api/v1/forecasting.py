from fastapi import APIRouter

from app.services.forecasting_engine import (
    ForecastingEngine
)

router = APIRouter(
    prefix="/api/v1/forecast",
    tags=["Forecasting"]
)


@router.get(
    "/stock/{symbol}"
)
def stock_forecast(
    symbol: str
):

    return (
        ForecastingEngine
        .stock_forecast(
            symbol
        )
    )


@router.get(
    "/trend/{symbol}"
)
def market_trend(
    symbol: str
):

    return (
        ForecastingEngine
        .market_trend(
            symbol
        )
    )


@router.get(
    "/portfolio/{portfolio_id}"
)
def portfolio_forecast(
    portfolio_id: str
):

    return (
        ForecastingEngine
        .portfolio_forecast(
            portfolio_id
        )
    )