"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb jobs')
os.system('createdb jobs')

model.connect_to_db(server.app)
model.db.create_all()

#Create a list of jobs with which to seed the db

jobs = [
    {
        'job_name':'Program Manager',
        'company': 'Twitter'
    },
    {
        'job_name':'Technical PgM',
        'company': 'WhatsApp'
    },
    {
        'job_name':'Technical Recruiter',
        'company': 'Palantir'
    }
]

for job in jobs:
    job_name = job['job_name']
    company = job['company']

    crud.create_job(job_name, company)