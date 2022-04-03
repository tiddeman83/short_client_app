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
    otp_secret = db.Column(db.String(16))

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)

        if self.otp_secret is None:
            self.otp_secret = base64.b32encode(os.urandom(10)).decode('utf-8')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_id(self):
        return self.id

    def get_totp_uri(self):
        return 'otpauth://totp/VWWBD-oek:{0}?secret={1}&issuer=DevBoss_VwWBD'.format(self.username, self.otp_secret)

    def verify_totp(self, token):
        return onetimepass.valid_totp(self.otp_secret, token)
