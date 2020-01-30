import datetime
from peewee import *
from flask_login import UserMixin
import os
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))
else:
    DATABASE = PostgresqlDatabase('weather_app')

class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()

    class Meta:
        database = DATABASE

class City(Model):
    name = CharField()
    owner = ForeignKeyField(User, backref = 'cities')

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, City], safe=True)
    print('Tables Created')
    DATABASE.close()