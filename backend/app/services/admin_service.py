from collections import Counter

from app.core.firebase import db


class AdminService:

    @staticmethod
    def get_system_statistics():

        investors = list(
            db.collection(
                "users"
            ).stream()
        )

        portfolios = list(
            db.collection(
                "portfolios"
            ).stream()
        )

        transactions = list(
            db.collection(
                "transactions"
            ).stream()
        )

        holdings = list(
            db.collection(
                "holdings"
            ).stream()
        )

        alerts = list(
            db.collection(
                "alerts"
            ).stream()
        )

        return {

            "total_investors":
                len(investors),

            "total_portfolios":
                len(portfolios),

            "total_transactions":
                len(transactions),

            "total_holdings":
                len(holdings),

            "total_alerts":
                len(alerts)
        }

    @staticmethod
    def get_all_investors():

        docs = db.collection(
            "users"
        ).stream()

        investors = []

        for doc in docs:

            investor = doc.to_dict()

            investor["uid"] = doc.id

            investors.append(
                investor
            )

        return investors

    @staticmethod
    def suspend_investor(
        uid: str
    ):

        db.collection(
            "users"
        ).document(
            uid
        ).update(
            {
                "status":
                    "suspended"
            }
        )

        return {
            "message":
                "Investor suspended successfully"
        }

    @staticmethod
    def activate_investor(
        uid: str
    ):

        db.collection(
            "users"
        ).document(
            uid
        ).update(
            {
                "status":
                    "active"
            }
        )

        return {
            "message":
                "Investor activated successfully"
        }

    @staticmethod
    def get_most_traded_stocks():

        docs = db.collection(
            "transactions"
        ).stream()

        counter = Counter()

        for doc in docs:

            transaction = doc.to_dict()

            symbol = transaction.get(
                "stock_symbol"
            )

            quantity = transaction.get(
                "quantity",
                0
            )

            if symbol:

                counter[symbol] += quantity

        return [

            {
                "symbol":
                    symbol,

                "volume":
                    volume
            }

            for symbol, volume
            in counter.most_common(10)
        ]

    @staticmethod
    def get_most_active_investors():

        docs = db.collection(
            "transactions"
        ).stream()

        counter = Counter()

        for doc in docs:

            transaction = doc.to_dict()

            investor_id = transaction.get(
                "investor_id"
            )

            if investor_id:

                counter[investor_id] += 1

        return [

            {
                "investor_id":
                    investor,

                "transactions":
                    count
            }

            for investor, count
            in counter.most_common(10)
        ]

    @staticmethod
    def get_total_market_value():

        docs = db.collection(
            "holdings"
        ).stream()

        total = 0

        for doc in docs:

            holding = doc.to_dict()

            total += holding.get(
                "market_value",
                0
            )

        return {

            "total_market_value":
                round(
                    total,
                    2
                )
        }

    @staticmethod
    def get_system_health():

        investors = len(
            list(
                db.collection(
                    "users"
                ).stream()
            )
        )

        portfolios = len(
            list(
                db.collection(
                    "portfolios"
                ).stream()
            )
        )

        transactions = len(
            list(
                db.collection(
                    "transactions"
                ).stream()
            )
        )

        holdings = len(
            list(
                db.collection(
                    "holdings"
                ).stream()
            )
        )

        return {

            "status":
                "healthy",

            "investors":
                investors,

            "portfolios":
                portfolios,

            "transactions":
                transactions,

            "holdings":
                holdings
        }