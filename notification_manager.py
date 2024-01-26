from twilio.rest import Client
import smtplib

TWILIO_SID = "ACd5857045c8cbb5f8229fa6fe83ce0816"
TWILIO_AUTH_TOKEN = "3eefd764b7b533b423ea71644821048e"
TWILIO_VIRTUAL_NUMBER = "+19164720348"
TWILIO_VERIFIED_NUMBER = "+77472775850"
EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "mukhtar.sarsenbay@nu.edu.kz"
MY_PASSWORD = "rbnb jxon xxxl nrqs"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
