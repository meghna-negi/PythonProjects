import smtplib
email = ""
password = ""

class NotificationManager:
    #This class sends the mail when prices are dropped
    def __init__(self) -> None:
        pass

    def send_mail(self,src,dest,price):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs="",
                msg=f"Subject:Flight price drop alert \n\n The price from flight from {src} to {dest} has dropped to {price} for tomorrow.\n\n"
            )