import smtplib

try:
    print("Connecting...")

    server = smtplib.SMTP(
        "smtp.gmail.com",
        465,
        timeout=30
    )

    server.set_debuglevel(1)

    print("Connected")

    server.ehlo()

    print("EHLO OK")

    server.starttls()

    print("TLS OK")

    server.ehlo()

    print("EHLO 2 OK")

    server.login(
        "infotech.peadato@gmail.com",
        "zpqyubjxoxcwumws"
    )

    print("LOGIN SUCCESS")

    server.quit()

except Exception as e:
    print("ERROR:")
    print(type(e))
    print(e)