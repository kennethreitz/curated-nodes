#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager

from nodes import app, db


manager = Manager(app)

@manager.command
def syncdb():
    """Initializes the database."""
    db.create_all()


if __name__ == "__main__":
    manager.run()