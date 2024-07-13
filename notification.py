import smtplib


def send_email_notification(address, message, my_email, my_password):
    pass
    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.set_debuglevel(1)
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=address, msg=message)
    except Exception as e:
        print(e)
