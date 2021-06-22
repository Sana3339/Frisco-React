from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import requests
from model import connect_to_db
import datetime
import os
import crud
import json
import cloudinary.uploader

app = Flask(__name__)
app.secret_key = "dev"

GOOG_API_KEY = os.environ['GOOGLE_API_KEY']
CLOUDINARY_API_KEY = os.environ['CLOUDINARY_API_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    """Render the root div onto which all React components are mounted."""

    return render_template("root.html")

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

    #convert prices (integers) to strings with commas in the appropriate places to improve user readability
    median_home_price_str = '{:,}'.format(median_home_price)
    sq_ft_price_str = '{:,}'.format(sq_ft_price)
    median_rental_str = '{:,}'.format(median_rental)

    neighborhood_obj = {
        'neighborhood_id': neighborhood_id,
        'name': name,
        'long_desc': long_desc,
        'median_home_price': median_home_price_str,
        'sq_ft_price': sq_ft_price_str,
        'median_rental': median_rental_str,
        'walk_score': walk_score,
        'transit_score': transit_score,
    }

    return jsonify(neighborhood_obj)

@app.route('/api/images/<neighborhood_id>')
def show_images(neighborhood_id):
    """Given a neighborhood_id, return the corresponding images."""

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

#The route below uses the restaurant's Google Place ID to get the 'photo reference' url for the
#first photo.  We then use the photo reference to create the url that displays the photo"
@app.route('/api/photo.json/<place_id>')
def get_restaurant_photo(place_id):
    """Send restaurant id to Google Places Search API endpoint to get restaurant photo reference id.

    Use photo reference id to create photo url (to be sent to front-end to dispaly photo in restaurant results)"""

    payload = {"key": GOOG_API_KEY,
                "place_id": place_id,
                "fields": "photo" }

    res = requests.get('https://maps.googleapis.com/maps/api/place/details/json', params=payload)

    converted_res = res.json()
    first_photo = converted_res["result"]["photos"][1]
    photo_reference = first_photo["photo_reference"]

    photo_url = f"https://maps.googleapis.com/maps/api/place/photo?key={GOOG_API_KEY}&photoreference={photo_reference}&maxheight=180"

    return photo_url


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

        if i < 4:
            rest_dict = {}

            name = data[i]['name']
            formatted_address = data[i]['formatted_address']
            rating = data[i]['rating']
            place_id = data[i]['place_id']
            website = get_restaurant_website(place_id)
            photo = get_restaurant_photo(place_id)

            street_address = formatted_address.rsplit(",")[0]
            address = street_address + "," + " SF, CA"

            rest_dict = {
                'name': name,
                'address': address,
                'rating': rating,
                'website': website,
                'place_id': place_id,
                'photo': photo
            }

            restaurant_list.append(rest_dict)

            #Below we are sorting the list of restaurant dictionaries in descending order by their rating
            sorted_restaurant_list = sorted(restaurant_list, key=lambda i: i['rating'], reverse=True)

    return jsonify(sorted_restaurant_list)

@app.route('/api/housing/<neighborhood_id>')
def show_housing_postings(neighborhood_id):
    """Show housing posted for a neighborhood."""

    postings = crud.get_postings(neighborhood_id)

    posting_list = []

    for posting in postings:

        date = posting.date.strftime('%m/%d/%Y')

        post_dict = {
            'date': date,
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

        return jsonify({'message': "Account created. Please log in."})

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
    """Return all housing postings for a given user."""

    email = request.get_json()

    postings = crud.get_postings_by_user(email)

    posting_list = []

    for posting in postings:

        date = posting.date.strftime('%m/%d/%Y')

        post_dict = {
            'date': date,
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
    """Create a housing posting and save in database."""

    data = request.get_json()

    neighborhood_id = data.get('neighborhood_id')
    email = data.get('email')
    date = datetime.datetime.now()
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
    """Return the seller's email for a particular housing posting."""

    contact_info = crud.get_seller_by_id(posting_id)

    return jsonify(contact_info)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0')
