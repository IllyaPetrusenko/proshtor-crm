from app import db
from datetime import datetime


class pr_users(db.Model):
    prus_id = db.Column(db.Integer, primary_key=True)
    prus_name = db.Column(db.String(64), index=True, unique=False)
    prus_email = db.Column(db.String(120), index=True, unique=True)
    prus_password_hash = db.Column(db.String(128))
    prus_phone = db.Column(db.String(128))
    prus_role_id = db.Column(db.Integer)
    prus_tel_chat_id = db.Column(db.Integer)
    prus_date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    prus_date_modified = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class pr_roles(db.Model):
    prro_id = db.Column(db.Integer, primary_key=True)
    prro_role_name = db.Column(db.String(64), index=True, unique=True)


class pr_orders(db.Model):
    pror_id = db.Column(db.Integer, primary_key=True)
    pror_us_id = db.Column(db.Integer, db.ForeignKey('pr_users.prus_id'))
    pror_state_id = db.Column(db.Integer)
    pror_comment = db.Column(db.String(255))
    pror_date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    pror_date_modified = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class pr_orders_state(db.Model):
    pros_id = db.Column(db.Integer, primary_key=True)
    pros_name = db.Column(db.String(64), index=True, unique=True)

