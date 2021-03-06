"""Models for Frisco app."""

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

class Posting(db.Model):
    """A posting for housing available in a neighborhood."""

    __tablename__ = 'postings'

    posting_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    neighborhood_id = db.Column(db.String, db.ForeignKey('neighborhoods.neighborhood_id'))
    user_email = db.Column(db.String, db.ForeignKey('users.email'))
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    contact_info = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String, nullable=True)

    neighborhood = db.relationship( 'Neighborhood', backref='postings')
    user = db.relationship('User', backref='postings')

    def __repr__(self):

        return f'<id={self.posting_id} date={self.date} title={self.title}, backref={self.neighborhood_id} user={self.user_email} image={self.image_url}>'


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    email = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):

        return f'<email={self.email} password={self.password}>'

class Image(db.Model):
    """Images of neighborhoods."""

    __tablename__='images'

    image_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_name = db.Column(db.String, nullable=False)
    neighborhood_id=db.Column(db.String, db.ForeignKey('neighborhoods.neighborhood_id'))


    def __repr__(self):

        return f'<id={self.image_id} image={self.image_name} neighborhood={self.neighborhood_id}>'

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