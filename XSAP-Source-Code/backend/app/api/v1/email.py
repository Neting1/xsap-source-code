from fastapi import APIRouter

from app.core.config import settings

from app.schemas.email import (
    EmailRequest,
    AlertEmailRequest
)

from app.services.email_service import (
    EmailService
)

router = APIRouter(
    prefix="/api/v1/email",
    tags=["Email"]
)


@router.get("/smtp-debug")
def smtp_debug():

    return {
        "smtp_server":
        settings.SMTP_SERVER,

        "smtp_port":
        settings.SMTP_PORT,

        "smtp_email":
        settings.SMTP_EMAIL
    }


@router.post("/test")
def send_test_email(
    data: EmailRequest
):

    return EmailService.send_email(
        data.email,
        "XSAP Today Stock Update",
        (
            "Congratulations.\n\n"
            "Your XSAP email service "
            "is working successfully."
        )
    )


@router.post("/send-alert")
def send_alert_email(
    data: AlertEmailRequest
):

    return EmailService.send_email(
        data.email,
        "XSAP Price Alert",
        (
            f"{data.stock_symbol} "
            f"has reached "
            f"GHS {data.current_price}"
        )
    )