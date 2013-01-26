# -*- coding: utf-8 -*-

import os
from datetime import datetime

from flask import Flask, abort, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import HSTORE

from flask.ext.markdown import Markdown


STYLES = ('prose', 'audio', 'photo', 'code', 'product')

app = Flask(__name__)
app.debug = os.environ.get('DEBUG')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']


db = SQLAlchemy(app)
Markdown(app)

class BaseModel(object):
    def save(self):
        db.session.add(self)
        return db.session.commit()

class Page(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    content = db.Column(db.Text())
    title = db.Column(db.String(140))
    draft = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Page %r>' % self.slug

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


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def get_index():
    return render_template('index.html')



@app.route('/<slug>')
def get_page(slug):

    want_drafts = ('preview' in request.args)

    p = Page.query.filter_by(slug=slug, draft=want_drafts).first() or abort(404)

    return render_template('page.html', page=p)

@app.route('/exposures')
def get_exposures(filter=None):

    f = {'draft': False}
    if filter:
        f['style'] = filter

    q = Exposure.query.filter_by(**f).order_by(Exposure.id.desc()).all()

    return render_template('list.html', items=q, view='exposures', filter=filter)

@app.route('/exposures/<slug>')
def get_exposure(slug):

    want_drafts = ('preview' in request.args)

    if slug in STYLES:
        return get_exposures(filter=slug)

    e = Exposure.query.filter_by(slug=slug, draft=want_drafts).first() or abort(404)

    return render_template('post.html', post=e, view='exposure')


@app.route('/experiments')
def get_experiments(filter=None):

    f = {'draft': False}
    if filter:
        f['style'] = filter

    q = Experiment.query.filter_by(**f).order_by(Experiment.id.desc()).all()

    return render_template('list.html', items=q, view='experiments', filter=filter)

@app.route('/experiments/<slug>')
def get_experiment(slug):

    want_drafts = ('preview' in request.args)

    if slug in STYLES:
        return get_experiments(filter=slug)

    e = Experiment.query.filter_by(slug=slug, draft=want_drafts).first() or abort(404)

    return render_template('post.html', post=e, view='experiment')


@app.route('/expressions')
def get_expressions(filter=None):

    f = {'draft': False}
    if filter:
        f['style'] = filter

    q = Expression.query.filter_by(**f).order_by(Expression.id.desc()).all()

    return render_template('list.html', items=q, view='expressions', filter=filter)

@app.route('/expressions/<slug>')
def get_expression(slug):

    want_drafts = ('preview' in request.args)

    if slug in STYLES:
        return get_expressions(filter=slug)

    e = Expression.query.filter_by(slug=slug, draft=want_drafts).first() or abort(404)

    return render_template('post.html', post=e, view='expression')


if __name__ == '__main__':
    app.run()