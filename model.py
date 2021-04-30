"""Models for JobTracker app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Job(db.Model):
    """A job application."""

    __tablename__='jobs'

    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_name = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)

    def __repr__(self):

        return f'<id={self.job_id} name={self.job_name} company={self.company}>'


def connect_to_db(flask_app, db_uri='postgresql:///jobs', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    connect_to_db(app)