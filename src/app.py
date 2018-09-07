from views import MailView
from flask import Flask

app = Flask(__name__)
app.add_url_rule('/mail/', view_func=MailView.as_view('mail'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9505")