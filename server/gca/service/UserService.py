import smtplib
from smtplib import SMTP
from email.message import EmailMessage
from flask import url_for
import os


def send_activation_email(user):
    msg = EmailMessage()
    url = os.environ['SITE_URL']+"/user/activate/"+user.code
    msg.set_content(
        f"We\'re glad you\'re here! Click <a href=\"{url}\">here</a > to activate your account.")

    msg['Subject'] = "Welcome to Get Crypto Alerts!"
    msg['to'] = user.email
    msg['from'] = "support@getcryptoalerts.com"

    smtp = smtplib.SMTP(host="127.0.0.1", port=1025, timeout=30)
    #smtp.login(None, None)
    smtp.set_debuglevel(False)
    smtp.send_message(msg)
    smtp.quit()
    return True


def send_forgot_password_email(user):
    msg = EmailMessage()
    msg.set_content('Click <a href="http://localhost:5000' +
                    url_for('user.update_password', code=user.code)+'/">here</a> to reset your password.')
    msg['Subject'] = "Get Crytp Alerts: Forgotten Password"
    msg['to'] = user.email
    msg['from'] = "support@getcryptoalerts.com"

    smtp = smtplib.SMTP(host="127.0.0.1", port=1025, timeout=30)
    #smtp.login(None, None)
    smtp.set_debuglevel(False)
    smtp.send_message(msg)
    smtp.quit()
    return True
