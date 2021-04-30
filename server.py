from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db
from datetime import datetime
import os
import crud
import json

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/")
def root():

    return render_template("root.html")

@app.route("/api/jobs.json")
def show_jobs():

    jobs = crud.get_all_jobs()

    all_jobs_list = []

    for job in jobs:
        job_name = job.job_name
        company = job.company

        job_dict = {
            'job_name': job_name,
            'company': company
            }

        all_jobs_list.append(job_dict)

    return jsonify(all_jobs_list)


@app.route("/add-job", methods=["POST"])
def add_job():
    """Add a new job to the database."""

    job_name = request.get_json().get("job_name")
    company = request.get_json().get("company")

    new_job = Job(job_name=job_name, company=company)
    db.session.add(new_job)
    db.session.commit()

    db.session.refresh(new_job)
    return {
        "success": True,
        "jobAdded": {
            "Position": new_job.job_name,
            "Company": new_job.company
        },
    }


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
