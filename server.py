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
        job_id = job.job_id
        job_name = job.job_name
        company = job.company

        job_dict = {
            'job_id': job_id,
            'job_name': job_name,
            'company': company
            }

        all_jobs_list.append(job_dict)

    return jsonify(all_jobs_list)


@app.route("/api/add-job", methods=["POST"])
def add_job():
    """Add a new job to the database."""

    data = request.get_json(force=True) 

    job_name = data['job_name']
    company = data['company']

    crud.create_job(job_name, company)
    
    return jsonify("Success")

@app.route("/api/get-job-id")
def get_job_id(job_name, company):

    job_id = crud.get_job_id

    return jsonify(job_id)

@app.route("/api/delete-job", methods=["POST"])
def delete_job():
    """Delete job from database."""

    job_id = request.get_json(force=True) 

    crud.delete_job(job_id)

    return jsonify("Success")

@app.route("/api/login", methods=["POST"])
def handle_login():

    data - request.get_json(force=True)

    email = data['email']
    password = data['password']

    #need to query db to see if user is in db



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
