"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa4abhp8u791gs3fh0-a",
        database="todo_app_borg",
        user="todo_app_borg_user",
        password="15s365cRlzY6ZEzHHc3I06TphNeh1e5K")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
