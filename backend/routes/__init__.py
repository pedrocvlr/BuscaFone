from flask import Flask

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://wajxbion:7anzpnxZJb12nwmw-sHqg3sQBWUNT4TX@tuffi.db.elephantsql.com:5432/wajxbion'

