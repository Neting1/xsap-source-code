import smtplib
import ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings


class EmailService:

    @staticmethod
    def send_email(
        recipient,
        subject,
        body
    ):

        try:

            message = MIMEMultipart()

            message["From"] = (
                settings.SMTP_EMAIL
            )

            message["To"] = recipient

            message["Subject"] = subject

            message.attach(
                MIMEText(
                    body,
                    "plain"
                )
            )

            context = (
                ssl.create_default_context()
            )

            server = smtplib.SMTP_SSL(
                settings.SMTP_SERVER,
                settings.SMTP_PORT,
                context=context
            )

            server.login(
                settings.SMTP_EMAIL,
                settings.SMTP_PASSWORD
            )

            server.sendmail(
                settings.SMTP_EMAIL,
                recipient,
                message.as_string()
            )

            server.quit()

            return {
                "success": True,
                "message": (
                    "Email sent successfully"
                )
            }

        except Exception as e:

            return {
                "success": False,
                "error": "SMTP Error",
                "details": str(e)
            }