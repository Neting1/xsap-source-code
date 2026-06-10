import smtplib
import ssl

try:

    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        context=context
    )

    server.login(
        "infotech.peadato@gmail.com",
        "zpqyubjxoxcwumws"
    )

    print("LOGIN SUCCESS")

    server.quit()

except Exception as e:

    print(type(e))
    print(e)