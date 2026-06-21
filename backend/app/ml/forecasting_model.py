class ForecastingModel:

    @staticmethod
    def predict_next_price(
        prices: list
    ):

        if not prices:

            return 0

        if len(prices) == 1:

            return prices[0]

        moving_average = (
            sum(prices) /
            len(prices)
        )

        momentum = (
            prices[-1] -
            prices[-2]
        )

        prediction = (
            moving_average +
            momentum
        )

        return round(
            prediction,
            2
        )

    @staticmethod
    def detect_trend(
        prices: list
    ):

        if len(prices) < 2:

            return "Neutral"

        if prices[-1] > prices[0]:

            return "Bullish"

        if prices[-1] < prices[0]:

            return "Bearish"

        return "Neutral"

    @staticmethod
    def calculate_confidence(
        prices: list
    ):

        if len(prices) < 2:

            return 50

        changes = []

        for i in range(
            1,
            len(prices)
        ):

            changes.append(
                abs(
                    prices[i] -
                    prices[i - 1]
                )
            )

        average_change = (
            sum(changes) /
            len(changes)
        )

        confidence = (
            100 -
            (average_change * 10)
        )

        confidence = max(
            50,
            min(
                95,
                confidence
            )
        )

        return round(
            confidence,
            2
        )