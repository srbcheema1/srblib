from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

def email(fromaddr, password, toaddr, body='', subject=''):
    msg = MIMEText(body, 'plain')
    msg['To'] = toaddr
    msg['Subject'] = subject

    server = SMTP('smtp.gmail.com')
    server.login(fromaddr,password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()

class Email:
    def __init__(self, fromaddr=None, password=None, toaddr=None, body='', subject=''):
        self.fromaddr = fromaddr
        self.password = password
        self.toaddr = toaddr
        self.body = body
        self.subject = subject

    def send(self):
        if(not self.toaddr):
            raise Exception('required recievers address')

        if(not self.fromaddr):
            raise Exception('required senders address')

        if(not self.password):
            raise Exception('required senders password')

        email(self.fromaddr, self.password, self.toaddr, self.body, self.subject)

