from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import requests
from model import connect_to_db
from datetime import datetime
import os
import crud
import json
import cloudinary.uploader

app = Flask(__name__)
app.secret_key = "dev"

GOOG_API_KEY = os.environ['GOOGLE_API_KEY']
CLOUDINARY_API_KEY = os.environ['CLOUDINARY_API_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']


@app.route("/<path:path>")
@app.route("/", defaults={"path": ""})
def catch_all(path):
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

#************************************************
#This route is used to get neighborhood details from DB to the front end
#via AJAX requests in the maps JS files. The data is used to populate
#the map markers, info windows and text on the page
@app.route('/api/neighborhood-details.json')
def get_neighborhood_details():
    """Return specific neighborhood details to populate Google map markers and info windows."""

    neighborhoods_obj = crud.get_all_neighborhoods()

    all_neighborhood_details = []

    for neighborhood in neighborhoods_obj:
        neighborhood_id = neighborhood.neighborhood_id
        name = neighborhood.name
        short_desc = neighborhood.short_desc
        latitude = neighborhood.latitude
        longitude = neighborhood.longitude

        neighborhood_dict = {
            'neighborhood_id': neighborhood_id,
            'name': name,
            'short_desc': short_desc,
            'latitude': latitude,
            'longitude': longitude
        }

        all_neighborhood_details.append(neighborhood_dict)

    return jsonify(all_neighborhood_details)
    

@app.route('/api/neighborhood/<neighborhood_id>')
def show_neighborhood(neighborhood_id):
    """Show SF neighborhood details"""

    neighborhood = crud.get_neighborhood_by_id(neighborhood_id)

    name = neighborhood.name
    long_desc = neighborhood.long_desc
    median_home_price = neighborhood.median_home_price
    sq_ft_price = neighborhood.sq_ft_price
    median_rental = neighborhood.median_rent
    walk_score = neighborhood.walk_score
    transit_score = neighborhood.transit_score
    #neighborhood_images = crud.create_list_of_neighborhood_images(neighborhood_id)
    
    #restaurant_data = show_restaurant_details(neighborhood_id)

    neighborhood_obj = {
        'neighborhood_id': neighborhood_id,
        'name': name,
        'long_desc': long_desc,
        'median_home_price': median_home_price,
        'sq_ft_price': sq_ft_price,
        'median_rental': median_rental,
        'walk_score': walk_score,
        'transit_score': transit_score,
        #'restaurant_data':restaurant_data,
        #images=neighborhood_images
    }

    return jsonify(neighborhood_obj)

@app.route('/api/images/<neighborhood_id>')
def show_images(neighborhood_id):

    images = crud.get_images_by_id(neighborhood_id)

    image_list = []

    for image in images:
        image_dict = {
            'image_id': image.image_id,
            'image_name' : image.image_name,
            'neighborhood_id' : image.neighborhood_id
        }

        image_list.append(image_dict)

    return jsonify(image_list)
        
        

        

    #return jsonify(image)

@app.route('/api/website.json/<place_id>')
def get_restaurant_website(place_id):
    """Send restaurant id to Google Places Search API to get restaurant website link."""
    
    payload = {"key": GOOG_API_KEY,
                "place_id": place_id,
                "fields": "website" }

    res = requests.get('https://maps.googleapis.com/maps/api/place/details/json', params=payload)

    converted_res = res.json()
    result = converted_res["result"]
    if result.get('website')!=None:
        website = converted_res["result"]["website"]
    else:
        website = ""
    
    return website

@app.route('/api/restaurants/<neighborhood_id>')
def show_restaurant_details(neighborhood_id):
    """Show a list of restaurants for a given neighborhood_id"""

    neighborhood = crud.get_neighborhood_by_id(neighborhood_id)
    neighborhood_name = neighborhood.name

    payload = {"query": f"restaurants in {neighborhood_name} in San Francisco",
                "key": GOOG_API_KEY}

    res = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json', params=payload)

    search_results = res.json()
    data = search_results["results"]

    restaurant_list = []


    for i, restaurant in enumerate(data):
        if i < 5:
            rest_dict = {}
            
            name = data[i]['name']
            address = data[i]['formatted_address']
            rating = data[i]['rating']
            place_id = data[i]['place_id']
            website = get_restaurant_website(place_id)

            rest_dict = {
                'name': name,
                'address': address,
                'rating': rating,
                'website': website,
                'place_id': place_id
            }

            restaurant_list.append(rest_dict)
        

    #I'm creating an empty list to limit the API search results to 5. 
    #This limitation allows us to do a separate API call and add the website to our search results
    #If you don't limit it, you will get a 'key error' for the 'website' field and the page won't load
    # limited_data = []

    # for i in range(5):
    #     limited_data.append(data[i])    
    
    # # for i in range(5):
    # #     place_id = search_results["results"][i].get("place_id")
    # #     website = get_restaurant_website(place_id)
    # #     limited_data[i]["website"] = website

    return jsonify(restaurant_list)

@app.route('/api/housing/<neighborhood_id>')
def show_housing_postings(neighborhood_id):
    """Show housing posted for a neighborhood."""

    postings = crud.get_postings(neighborhood_id)

    posting_list = []

    for posting in postings:
        post_dict = {
            'date': posting.date,
            'title': posting.title,
            'desc': posting.desc,
            'contact_info': posting.contact_info,
            'posting_id': posting.posting_id,
            'image_url': posting.image_url
        }

        posting_list.append(post_dict)

    return jsonify(posting_list)

@app.route('/api/create-user',methods=["POST"])
def create_user():
    """Create a new user."""

    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = crud.get_user_by_email(email)

    if user != None:
        return jsonify ({'message': "Error - user already exists. Please log in."})

    else:
        new_user = crud.create_user(email, password)

        return jsonify({'message': "Account created. You are logged in."})

@app.route('/api/handle-login', methods=["POST"])
def login_user():
    """Check if login credentials are correct, and if so, log in user."""

    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = crud.get_user_by_email(email)

    if user == None:
        return jsonify({'message': "No account exists for that email. Please create an account."})

    if user != None:
        if user.password != password:
            return jsonify({'message': "Incorrect password."})
        else:
            return jsonify({'message': "You are now logged in.",
                            'email': email})

   
@app.route('/api/get-user-postings', methods=["POST"])
def get_user_postings():

    email = request.get_json()

    postings = crud.get_postings_by_user(email)

    posting_list = []

    for posting in postings:
        post_dict = {
            'date': posting.date,
            'title': posting.title,
            'desc': posting.desc,
            'contact_info': posting.contact_info,
            'posting_id': posting.posting_id,
            'image_url': posting.image_url
        }

        posting_list.append(post_dict)

    return jsonify(posting_list)

@app.route('/api/create-posting', methods=["POST"])
def create_posting():

    data = request.get_json()

    neighborhood_id = data.get('neighborhood_id')
    email = data.get('email')
    date = datetime.now()
    title = data.get('title')
    desc = data.get('desc')
    contact_info = data.get('contact_info')
    image_url = data.get('image_url')

    crud.create_posting(neighborhood_id, email, date, title, desc, contact_info, image_url)

    return jsonify("Success")

@app.route("/api/delete-posting", methods=["POST"])
def delete_posting():
    """Delete posting from database and from user's profile."""

    posting_id = request.get_json(force=True)
    print("POSTING ID IS:", posting_id)

    crud.delete_posting(posting_id)

    return jsonify("Success")

@app.route('/api/get-seller-email/<posting_id>')
def get_seller_by_id(posting_id):

    contact_info = crud.get_seller_by_id(posting_id)

    return jsonify(contact_info)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
