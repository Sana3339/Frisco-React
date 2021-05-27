"""CRUD operations."""

from model import db, connect_to_db, Neighborhood, Posting, User, Image

def create_neighborhood(neighborhood_id, name, latitude, longitude,
                        short_desc, long_desc, median_rent, median_home_price,
                        sq_ft_price, walk_score, transit_score,images):
    """Create a new neighborhood."""

    neighborhood = Neighborhood(neighborhood_id=neighborhood_id,
                                name=name,
                                latitude=latitude,
                                longitude=longitude,
                                short_desc=short_desc,
                                long_desc=long_desc,
                                median_rent=median_rent,
                                median_home_price=median_home_price,
                                sq_ft_price=sq_ft_price,
                                walk_score=walk_score,
                                transit_score=transit_score,
                                images=images)

    db.session.add(neighborhood)
    db.session.commit()

def add_image(image_name, neighborhood_id):
    """Add image and its neighborhood_id to db"""

    image = Image(image_name = image_name,
                neighborhood_id = neighborhood_id)

    db.session.add(image)
    db.session.commit()

def get_all_neighborhoods():
    """Return details of all neighborhoods in db"""

    neighborhoods = Neighborhood.query.all()

    return neighborhoods

def get_neighborhood_by_id(neighborhood_id):
    """Provided a neighborhood_id, return the neighborhood object."""

    neighborhood = Neighborhood.query.get(neighborhood_id)

    return neighborhood

def get_images_by_id(neighborhood_id):
    """Provided a neighborhood_id, return the associated images."""

    images = Image.query.filter(Image.neighborhood_id == neighborhood_id).all()

    return images

def create_posting(neighborhood_id, email, date, title, desc, contact_info, image_url):
    """Create a housing posting."""
    
    posting = Posting(neighborhood_id=neighborhood_id,
                        user_email=email,
                        date=date,
                        title=title,
                        desc=desc,
                        contact_info=contact_info,
                        image_url=image_url
                        )

    db.session.add(posting)
    db.session.commit()

def create_user(email, password):
    """Create a new user in the database."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

def get_postings(neighborhood_id):
    """Get all housing postings for a particular neighborhood."""

    postings = Posting.query.filter_by(neighborhood_id=neighborhood_id).all()
    
    return postings

def get_user_by_email(email):
    """Given an email, return the user."""

    return User.query.filter(User.email == email).first()

def get_postings_by_user(email):
    """Return all housing posted by a user."""

    return Posting.query.filter(Posting.user_email == email).all()

def delete_posting(posting_id):
    """Delete a housing posting from database."""

    posting = Posting.query.get(posting_id)
    if posting is not None:
        db.session.delete(posting)
        db.session.commit()

def get_seller_by_id(posting_id):
    """Get seller email for a particular housing posting."""

    posting = Posting.query.filter_by(posting_id=posting_id).first()
    contact_info = posting.contact_info

    return contact_info

if __name__ == '__main__':
    from server import app
    connect_to_db(app)