"""CRUD operations."""

from model import db, connect_to_db, Job, Neighborhood

def create_job(job_name, company):
    """Create a job application"""

    job = Job(job_name=job_name, company=company)

    db.session.add(job)
    db.session.commit()

def get_all_jobs():

    jobs = Job.query.all()

    return jobs

def create_job(job_name, company):
    
    job = Job(job_name=job_name,
              company=company
              )

    db.session.add(job)
    db.session.commit()

def delete_job(job_id):

    job = Job.query.get(job_id)
    if job is not None:
        db.session.delete(job)
        db.session.commit()

def get_job_id(job_name, company):

    job_id = job.query.filter("job_name"==job_name, "company"==company).first()
    return job_id

#********************************************************************************

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

def get_all_neighborhoods():
    """Return details of all neighborhoods in db"""

    neighborhoods = Neighborhood.query.all()

    return neighborhoods


if __name__ == '__main__':
    from server import app
    connect_to_db(app)