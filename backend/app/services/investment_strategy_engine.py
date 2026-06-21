from app.services.risk_profile_engine import (
    RiskProfileEngine
)


class InvestmentStrategyEngine:

    @staticmethod
    def generate_strategy(
        investor_id: str
    ):

        profile = (
            RiskProfileEngine
            .assess_investor(
                investor_id
            )
        )

        risk_profile = (
            profile[
                "risk_profile"
            ]
        )

        strategy = (
            profile[
                "recommended_strategy"
            ]
        )

        allocation_plan = {}
        investment_horizon = ""
        expected_risk = ""
        expected_return = ""

        if (
            risk_profile
            == "Conservative"
        ):

            allocation_plan = {
                "Banking": 40,
                "Insurance": 35,
                "Telecom": 15,
                "Cash": 10
            }

            investment_horizon = (
                "5-10 Years"
            )

            expected_risk = (
                "Low"
            )

            expected_return = (
                "5% - 10%"
            )

        elif (
            risk_profile
            == "Moderate"
        ):

            allocation_plan = {
                "Banking": 30,
                "Insurance": 20,
                "Telecom": 35,
                "Manufacturing": 15
            }

            investment_horizon = (
                "3-7 Years"
            )

            expected_risk = (
                "Medium"
            )

            expected_return = (
                "8% - 15%"
            )

        else:

            allocation_plan = {
                "Telecom": 40,
                "Energy": 30,
                "Manufacturing": 20,
                "Cash": 10
            }

            investment_horizon = (
                "3-5 Years"
            )

            expected_risk = (
                "High"
            )

            expected_return = (
                "12% - 25%"
            )

        return {

            "investor_id":
                investor_id,

            "risk_profile":
                risk_profile,

            "recommended_strategy":
                strategy,

            "allocation_plan":
                allocation_plan,

            "investment_horizon":
                investment_horizon,

            "expected_risk":
                expected_risk,

            "expected_return_range":
                expected_return
        }