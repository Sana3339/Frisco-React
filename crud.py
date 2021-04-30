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

if __name__ == '__main__':
    from server import app
    connect_to_db(app)