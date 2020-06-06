import requests
import smtplib
import json
from email.message import EmailMessage
from twilio.rest import Client
from twilio.rest.api.v2010.account.message import MessageInstance
from validation import isMailPusherId, isEmail


class Notify:
    def __init__(self):
        self.body = None
        self.subject = None
        self.required = []

    def setSubject(self, subject: str):
        if not subject:
            raise Exception("Invalid Subject")
        self.subject = subject
        return True

    def setBody(self, body: str):
        if not body:
            raise Exception("Invalid Body")
        self.body = body
        return True

    def validate(self) -> bool:
        for attr in self.__dict__:
            if getattr(self, attr) is None:
                raise Exception(f"{attr} is undefined")
        return True


class SMS(Notify):
    def __init__(self):
        super().__init__()
        self.service = None
        self.to_phone_number = None
        self.from_phone_number = None
        self.supported_services = ["twilio"]
        self.twilio_auth_token = None
        self.twilio_account_sid = None
        self.subject = ""

    def setToPhoneNumber(self, phone_number: str) -> bool:
        if not phone_number:
            raise Exception('Invalid To Phone Number')
        self.to_phone_number = phone_number
        return True

    def setFromPhoneNumber(self, phone_number: str) -> bool:
        if not phone_number:
            raise Exception('Invalid From Phone Number')
        self.from_phone_number = phone_number
        return True

    def setService(self, service: str):
        if service != "twilio":
            raise Exception("Invalid Service")
        self.service = service
        return True

    def setTwillioAuth(self, auth_token: str, account_sid: str) -> bool:
        if not auth_token or not account_sid:
            raise Exception
        self.twilio_auth_token = auth_token
        self.twilio_account_sid = account_sid
        return True

    def send(self) -> MessageInstance:
        self.validate()
        client = Client(self.twilio_account_sid, self.twilio_auth_token)
        return client.messages.create(
            to=self.to_phone_number,
            from_=self.from_phone_number,
            body=self.body
        )


class Email(Notify):

    def __init__(self):
        super().__init__()
        self.from_ = None
        self.to = None
        self.smtp_hostname = None
        self.smtp_username = ""
        self.smtp_password = ""
        self.smtp_port = 587
        self.smtp_timeout = 30
        self.smtp_debug = False

    def setSmtpHostName(self, hostname):
        if not hostname:
            raise Exception("Invalid Hostname")
        self.smtp_hostname = hostname
        return True

    def setSmtpHostPort(self, port: int) -> bool:
        if not isinstance(port, int) or port < 1:
            raise Exception("Invalid Port")
        self.smtp_port = port
        return True

    def setSmtpTimeout(self, timeout: int) -> bool:
        if not isinstance(timeout, int):
            raise Exception("Invalid Timeout")
        self.smtp_timeout = timeout
        return True

    def setSmtpLogin(self, login: str) -> None:
        self.smtp_login = login
        return True

    def setSmtpPassword(self, password: str) -> None:
        self.smtp_password = password
        return True

    def setDebugLevel(self, debug: bool) -> bool:
        if not isinstance(debug, bool):
            raise Exception("Invalid Debug")
        self.smtp_debug = debug
        return True

    def setFrom(self, email: str) -> None:
        if isEmail(email) is False:
            raise Exception('Invalid Email Address')
        self.from_ = email
        return True

    def setTo(self, email: int) -> bool:
        if isEmail(email) is False:
            raise Exception('Invalid Email Address')
        self.to = email
        return True

    def send(self) -> bool:
        self.validate()
        msg = EmailMessage()
        msg.set_content(self.body)
        msg['Subject'] = self.subject
        msg['From'] = self.from_
        msg['To'] = self.to
        try:
            smtpobj = smtplib.SMTP(
                host=self.smtp_hostname, port=self.smtp_port, timeout=self.smtp_timeout)
            if len(self.smtp_username) and len(self.smtp_password):
                smtpobj.login(self.smtp_username, self.smtp_password)
            smtpobj.set_debuglevel(self.smtp_debug)
            smtpobj.send_message(msg)
            smtpobj.quit()
            return True
        except smtplib.SMTPException:
            raise Exception


class WirePusher(Notify):

    def __init__(self):
        super().__init__()
        self.endpoint = "https://wirepusher.com/send"
        self.wirepusher_id = None

    def setId(self, string: str) -> bool:
        if isMailPusherId(string) is False:
            raise Exception
        self.wirepusher_id = string
        return True

    def send(self) -> bool:
        self.validate()
        response = requests.post(
            url=f"{self.endpoint}",
            data={
                "id": self.wirepusher_id,
                "title": self.subject,
                'message': self.body,
                "type": ""
            }
        )
        if response.status_code != 200:
            raise Exception
        content = json.loads(response.text)
        if content["errors"]:
            raise Exception
        return True
