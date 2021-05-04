"""Models for JobTracker app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Neighborhood(db.Model):
    """A neighborhood."""

    __tablename__='neighborhoods'

    neighborhood_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    latitude = db.Column(db.Float, nullable=False, unique=True)
    longitude = db.Column(db.Float, nullable=False, unique=True)
    short_desc = db.Column(db.Text, nullable=False)
    long_desc = db.Column(db.Text, nullable=False)
    median_rent = db.Column(db.Integer, nullable=False)
    median_home_price = db.Column(db.Integer, nullable=False)
    sq_ft_price = db.Column(db.Integer, nullable=True)
    walk_score = db.Column(db.Integer, nullable=True)
    transit_score = db.Column(db.Integer, nullable=True)
    images = db.Column(db.Text, nullable=True)

    def __repr__(self):

        return f'<id={self.neighborhood_id} name={self.name}>'



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