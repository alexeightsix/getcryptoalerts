from notify import WirePusher, Email, SMS, Notify
import pytest

# NOTIFY


def test_setSubject():
    notify = Notify()
    with pytest.raises(Exception):
        notify.setSubject("")
    assert notify.setSubject("mySubject")
    assert notify.subject == "mySubject"


def test_setBody():
    notify = Notify()
    with pytest.raises(Exception):
        notify.setBody("")
    assert notify.setBody("myBody")
    assert notify.body == "myBody"


def test_validate():
    notify = Notify()
    with pytest.raises(Exception):
        notify.validate()

# EMAIL


def test_email_setTo():
    email = Email()
    with pytest.raises(Exception):
        email.setTo("invalidEmail")

    assert email.setTo("someEmail@gmail.com")
    assert email.to == "someEmail@gmail.com"


def test_email_setFrom():
    email = Email()
    with pytest.raises(Exception):
        email.setFrom("invalidEmail")

    assert email.setFrom("someEmail@gmail.com")
    assert email.from_ == "someEmail@gmail.com"


def test_smtp_hostname():
    email = Email()
    with pytest.raises(Exception):
        email.setSmtpHostName("")
    assert email.setSmtpHostName("smtp-relay.sendinblue.com")
    assert email.smtp_hostname == 'smtp-relay.sendinblue.com'


def test_smtp_port():
    email = Email()
    with pytest.raises(Exception):
        email.setSmtpHostPort("invalidPort")
    with pytest.raises(Exception):
        email.setSmtpHostPort(0)
    assert email.setSmtpHostPort(587)
    assert email.smtp_port == 587


def test_smtp_timeout():
    email = Email()
    with pytest.raises(Exception):
        email.setSmtpTimeout("invalidTimeout")
    assert email.setSmtpTimeout(30)


def test_smtp_login():
    email = Email()
    assert email.setSmtpLogin("myLogin")
    assert email.smtp_login == 'myLogin'


def test_smtp_password():
    email = Email()
    assert email.setSmtpPassword("password")
    assert email.smtp_password == 'password'


def test_debug():
    email = Email()
    with pytest.raises(Exception):
        email.setDebugLevel("true")
    assert email.setDebugLevel(True)
    assert email.smtp_debug == True


def test_email_send():
    email = Email()
    email.setSmtpHostName("localhost")
    email.setSmtpHostPort(1025)
    email.setBody("Test")
    email.setSubject("Test")
    email.setTo("blah@gmail.com")
    email.setFrom("pytest@gmail.com")
    assert email.send()


# SMS


def test_sms_set_to_phone_number():
    sms = SMS()
    with pytest.raises(Exception):
        sms.setToPhoneNumber('')
    assert sms.setToPhoneNumber("1111111")
    assert sms.to_phone_number == "1111111"


def test_sms_set_from_phone_number():
    sms = SMS()
    with pytest.raises(Exception):
        sms.setFromPhoneNumber('')
    assert sms.setFromPhoneNumber("1111111")
    assert sms.from_phone_number == "1111111"


def test_twillio_set_auth():
    sms = SMS()
    with pytest.raises(Exception):
        sms.setTwillioAuth('', '')
    assert sms.setTwillioAuth("abc", "abc")
    assert sms.twilio_auth_token == "abc"
    assert sms.twilio_account_sid == "abc"


def test_sms_send():
    sms = SMS()
    sms.setToPhoneNumber('+1111111')
    sms.setFromPhoneNumber('+1111111')
    sms.setService('twilio')
    ##sms.setTwillioAuth(account_sid="",auth_token="")
    sms.setBody(f"asdasdasdas")
    ##assert sms.send()


# TWILIO


def test_sms_set_service():
    sms = SMS()
    with pytest.raises(Exception):
        sms.setService('aws')
    assert sms.setService("twilio")
    assert sms.service == "twilio"


# WIREPUSHER

def test_wirepusher_set_id():
    wirepusher = WirePusher()
    with pytest.raises(Exception):
        wirepusher.setId("")
    assert wirepusher.setId("asdasdasd")
    assert wirepusher.wirepusher_id == "asdasdasd"


def test_wirepusher_send():
    wirepusher = WirePusher()
    wirepusher.setId("H4z5mpnew")
    wirepusher.setSubject(f"pycharm test")
    wirepusher.setBody(f"pycharm test")
    wirepusher.send()

    with pytest.raises(Exception):
        wirepusher.setId("invalidId")
        wirepusher.send()
