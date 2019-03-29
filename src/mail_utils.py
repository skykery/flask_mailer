from mailer import Mailer
from mailer import Message

class Mail:
    def __init__(self, sender_mail, sender_password):
        self.gmail_user = sender_mail
        self.gmail_password = sender_password
        self.server = self.init_server()
        self.message = ""
    
    def init_server(self):
        return Mailer(host="smtp.gmail.com", port="465", usr=self.gmail_user, pwd=self.gmail_password, use_ssl=True)

    def init_message(self, to, subject, body):
        message = Message(From=self.gmail_user, To=to, charset="utf-8")
        message.Subject = subject
        message.Body = body
        self.message = message
    
    def send(self):
        self.server.send(self.message)
        print("mail sent")


# mail = Mail(gmail_user, gmail_password)
# mail.init_message("alin.alex.b@gmail.com", "Hello again", "Is this still working ?")
# mail.send()
