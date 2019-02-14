from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'f21b8fc3902161'
app.config['MAIL_PASSWORD'] = 'dcf7cb98c5e0e3'

mail = Mail(app)
from app import views
