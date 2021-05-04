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

#Create a list of neighborhoods with which to seed the db

neighborhoods = [
    {
    'neighborhood_id': 'bernal',
    'name': 'Bernal Heights',
    'latitude': 37.7389,
    'longitude': -122.4152,
    'short_desc': """<div style='float:right'><img src='/static/img/bernal1.jpeg' width="120" 
                    height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>Bernal Heights</b> is a primarily residential neighborhood with a commercial strip 
                    and a farmer's market every Saturday.
                    <a href="/neighborhood/bernal">Click here to learn more.</a>""",
    'long_desc': """"The neighborhood is primary residential with a commercial strip along
                    Corland Ave featuring restaurants, bars, bakeries, a fish and butchery 
                    shop and more.  It's home to the open-air Alemany Farmers' Market, 
                    one of the oldest extant farmers' markets in the US.  Bernal has not 
                    gentrified to the extent of its neighbor Noe Valley, but gentrification 
                    and property values are increasing as urban professionals replace 
                    working-class home owners and renters""",
    'median_rent': 2704,
    'median_home_price': 1621000,
    'sq_ft_price': 1093,
    'walk_score': 89,
    'transit_score': 77,
    'images': '/static/img/bernal1.jpeg, /static/img/bernal2.jpg, /static/img/bernal3.jpeg'        
    },
    {
    'neighborhood_id': 'castro',
    'name': 'Castro',
    'latitude': 37.7609,
    'longitude': -122.435,
    'short_desc': """<div style='float:right'><img src='/static/img/castro1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Castro</b> was one of the first gay neighborhoods in the US.
                    It's currently among the most prominent symbols of lesbian, gay,
                    bisexual and transgender (LGBT) activism and events in the world.
                    <a href="/neighborhood/castro">Click here to learn more.</a>""",
    'long_desc': """The Castro was one of the first gay neighborhoods in the US. One of its more
                    notable features is Castro Theatre, a movie palace built in 1922 and one of 
                    San Francisco's premier movie houses. 18th and Castro is a major intersection 
                    where many historic events, marches, and protests have taken and continue to take place.
                    The Castro is a "thriving marketplace for all things gay" meaning everything 
                    in the area is catered to people who identify with LGBT culture and other associated 
                    meanings to the word gay.  There are cafes, the Castro Theater, and many businesses 
                    that cater to or openly welcome LGBT consumers. These establishments make the Castro 
                    an area of high spending and lead to high tourist traffic.""",
    'median_rent': 0,
    'median_home_price': 2645000,
    'sq_ft_price': 1265,
    'walk_score': 99,
    'transit_score': 95,
    'images': '/static/img/castro1.jpeg, /static/img/castro2.jpeg, /static/img/castro3.jpeg'         
    },
    {
    'neighborhood_id': 'haight',
    'name': 'Haight-Ashbury',
    'latitude': 37.7692,
    'longitude': -122.4481,
    'short_desc': """<div style='float:right'><img src='/static/img/haight1.jpeg' width="120" height="120"></div>
                    <div style='float:left; height:130px; width:180px;'><b>Haight-Ashbury</b> 
                    is known as a main center of the 
                    hippie and counterculture of the 1960s. The Summer of Love (1967)
                    has been synonymous with the neighborhood ever since.
                    <a href="/neighborhood/haight">Click here to learn more.</a>""",
    'long_desc': """Haight-Ashbury is known as one of the main centers of the 
                    hippie and counterculture of the 1960s. The mainstream media's 
                    coverage of hippie life in the Haight-Ashbury drew the attention 
                    of youth from all over America. The Haight-Ashbury 
                    district was sought out by hippies to constitute a community based 
                    upon counterculture ideals, drugs, and music. This neighborhood 
                    offered a concentrated gathering spot for hippies to create a social 
                    experiment that would soon spread throughout the nation""",
    'median_rent': 3094,
    'median_home_price': 3540000,
    'sq_ft_price': 1221,
    'walk_score': 97,
    'transit_score': 80,
    'images': '/static/img/haight1.jpeg, /static/img/haight2.jpeg, /static/img/haight3.jpeg'   
    }
]

for neighborhood in neighborhoods: 
    neighborhood_id = neighborhood['neighborhood_id']
    name = neighborhood['name']
    latitude = neighborhood['latitude']
    longitude = neighborhood['longitude']
    short_desc = neighborhood['short_desc']
    long_desc = neighborhood['long_desc']
    median_rent = neighborhood['median_rent']
    median_home_price = neighborhood['median_home_price']
    sq_ft_price = neighborhood['sq_ft_price']
    walk_score = neighborhood['walk_score']
    transit_score = neighborhood['transit_score']
    images = neighborhood['images']

    crud.create_neighborhood(neighborhood_id, name, latitude, longitude, 
        short_desc, long_desc, median_rent, median_home_price, sq_ft_price, walk_score, transit_score, images)
                                       