"""CRUD operations."""

from model import db, connect_to_db, Job

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


if __name__ == '__main__':
    from server import app
    connect_to_db(app)