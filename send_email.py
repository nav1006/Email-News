import smtplib, ssl
import os

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = '10navdeepkumar@gmail.com'
    password = os.getenv('Password_Email_Api')

    receiver = '10navdeepkumar@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context= context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)