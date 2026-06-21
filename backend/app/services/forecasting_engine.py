from app.ml.forecasting_model import (
    ForecastingModel
)

from app.repositories.historical_price_repository import (
    HistoricalPriceRepository
)

from app.services.analytics_engine import (
    AnalyticsEngine
)


class ForecastingEngine:

    @staticmethod
    def stock_forecast(
        symbol: str
    ):

        data = (
            HistoricalPriceRepository
            .get_prices_by_symbol(
                symbol
            )
        )

        if not data:

            return {

                "symbol":
                    symbol,

                "current_price":
                    0,

                "predicted_price":
                    0,

                "expected_return":
                    0,

                "forecast":
                    "Neutral",

                "confidence":
                    50
            }

        prices = [

            float(
                item[
                    "close_price"
                ]
            )

            for item in data
        ]

        current_price = (
            prices[-1]
        )

        predicted_price = (
            ForecastingModel
            .predict_next_price(
                prices
            )
        )

        forecast = (
            ForecastingModel
            .detect_trend(
                prices
            )
        )

        confidence = (
            ForecastingModel
            .calculate_confidence(
                prices
            )
        )

        expected_return = 0

        if current_price > 0:

            expected_return = round(
                (
                    (
                        predicted_price -
                        current_price
                    )
                    /
                    current_price
                ) * 100,
                2
            )

        return {

            "symbol":
                symbol,

            "current_price":
                current_price,

            "predicted_price":
                predicted_price,

            "expected_return":
                expected_return,

            "forecast":
                forecast,

            "confidence":
                confidence
        }

    @staticmethod
    def market_trend(
        symbol: str
    ):

        forecast = (
            ForecastingEngine
            .stock_forecast(
                symbol
            )
        )

        return {

            "symbol":
                symbol,

            "trend":
                forecast[
                    "forecast"
                ],

            "confidence":
                forecast[
                    "confidence"
                ]
        }

    @staticmethod
    def portfolio_forecast(
        portfolio_id: str
    ):

        analytics = (
            AnalyticsEngine
            .get_portfolio_summary(
                portfolio_id
            )
        )

        current_value = (
            analytics[
                "total_market_value"
            ]
        )

        holdings = (
            analytics[
                "holdings"
            ]
        )

        growth_rates = []

        for holding in holdings:

            stock_prediction = (
                ForecastingEngine
                .stock_forecast(
                    holding[
                        "symbol"
                    ]
                )
            )

            growth_rates.append(
                stock_prediction[
                    "expected_return"
                ]
            )

        average_growth = 0

        if growth_rates:

            average_growth = (
                sum(
                    growth_rates
                )
                /
                len(
                    growth_rates
                )
            )

        predicted_value = (
            current_value *
            (
                1 +
                (
                    average_growth
                    / 100
                )
            )
        )

        return {

            "portfolio_id":
                portfolio_id,

            "current_value":
                round(
                    current_value,
                    2
                ),

            "predicted_value":
                round(
                    predicted_value,
                    2
                ),

            "expected_growth_percent":
                round(
                    average_growth,
                    2
                )
        }