from flask import Flask
import os
app = Flask(__name__)

host = os.getenv("POSTGRESQL_HOST")
database = os.getenv("POSTGRESQL_DATABASE")
username = os.getenv("POSTGRESQL_USERNAME")
password = os.getenv("POSTGRESQL_PASSWORD")

app.config[
    'SQLALCHEMY_DATABASE_URI'
] = f'postgresql://{username}:{password}@{host}:5432/{database}'

