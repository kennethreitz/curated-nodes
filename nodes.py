# -*- coding: utf-8 -*-

import os
from datetime import datetime

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import HSTORE


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

class BaseModel(object):
    def save(self):
        db.session.add(self)
        return db.session.commit()

class Expression(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    content = db.Column(db.Text())
    title = db.Column(db.String(140))
    link = db.Column(db.String(280))
    draft = db.Column(db.Boolean, default=True)
    style = db.Column(db.String(80))
    meta = db.Column(HSTORE())
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Expression %r>' % self.slug

class Experiment(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    content = db.Column(db.Text())
    title = db.Column(db.String(140))
    link = db.Column(db.String(280))
    draft = db.Column(db.Boolean, default=True)
    style = db.Column(db.String(80))
    status = db.Column(db.String(80))
    log = db.Column(db.Text())
    meta = db.Column(HSTORE())
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now)
    graduated = db.Column(db.String(280))

    def __repr__(self):
        return '<Experiment %r>' % self.slug

class Exposure(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    content = db.Column(db.Text())
    title = db.Column(db.String(140))
    link = db.Column(db.String(280))
    draft = db.Column(db.Boolean, default=True)
    style = db.Column(db.String(80))
    meta = db.Column(HSTORE())
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Exposure %r>' % self.slug


@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()