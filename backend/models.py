from sqlalchemy import ForeignKey
from . import db
from flask_login import UserMixin
import datetime as dt
import os
import base64
import onetimepass


class firstUsers(db.Model, UserMixin):
    __tablename__ = 'firstusers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    unique_token = db.Column(db.String(6))
    token_used = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        super(firstUsers, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, username, password, unique_token, token_used):
        self.username = username
        self.password = password
        self.unique_token = unique_token
        self.token_used = token_used
        db.session.commit()


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    first_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(64))

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()
