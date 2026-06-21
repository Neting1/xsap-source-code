from datetime import datetime

from app.repositories.alert_repository import (
    AlertRepository
)

from app.services.providers.gse_provider import (
    GSEProvider
)

from app.services.notification_service import (
    NotificationService
)


class AlertService:

    @staticmethod
    def create_alert(data):

        data["stock_symbol"] = (
            data["stock_symbol"]
            .upper()
            .strip()
        )

        data["status"] = "active"

        data["triggered"] = False

        data["created_at"] = (
            datetime.utcnow()
            .isoformat()
        )

        return (
            AlertRepository
            .create_alert(data)
        )

    @staticmethod
    def get_alerts(user_id):

        return (
            AlertRepository
            .get_user_alerts(
                user_id
            )
        )

    @staticmethod
    def delete_alert(alert_id):

        return (
            AlertRepository
            .delete_alert(
                alert_id
            )
        )

    @staticmethod
    def check_alerts():

        provider = GSEProvider()

        alerts = (
            AlertRepository
            .get_active_alerts()
        )

        checked = 0
        triggered = 0

        for alert in alerts:

            checked += 1

            stock = provider.get_stock(
                alert["stock_symbol"]
            )

            if "error" in stock:
                continue

            current_price = float(
                stock.get(
                    "price",
                    0
                )
            )

            target_price = float(
                alert["target_price"]
            )

            condition = (
                alert["condition"]
                .lower()
            )

            should_trigger = False

            if (
                condition == "above"
                and
                current_price >= target_price
            ):
                should_trigger = True

            elif (
                condition == "below"
                and
                current_price <= target_price
            ):
                should_trigger = True

            if should_trigger:

                AlertRepository.update_alert(
                    alert["alert_id"],
                    {
                        "status":
                            "triggered",

                        "triggered":
                            True,

                        "triggered_at":
                            datetime.utcnow()
                            .isoformat(),

                        "current_price":
                            current_price
                    }
                )

                NotificationService.create_notification(
                    {
                        "user_id":
                            alert["user_id"],

                        "title":
                            "Price Alert Triggered",

                        "message":
                            (
                                f"{alert['stock_symbol']} "
                                f"has reached "
                                f"GHS {current_price}"
                            ),

                        "type":
                            "price_alert"
                    }
                )

                triggered += 1

        return {
            "alerts_checked":
                checked,

            "alerts_triggered":
                triggered
        }