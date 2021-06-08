# Frisco
Frisco is an SPA (Single Page App) built in React with a Flask server and SQL Alchemy ORM.

## Introduction
San Francisco is an incredible place with each neighborhood vastly different from the next, all with their own personalities and characteristics.  I was the first in my network to move to SF over 10 years ago and I remember how difficult it was to figure out which neighborhood was best suited for me.  

I built Frisco to help other young professionals looking to move to the City by the Bay to have the most pertinent information of the most popular/well-known neighborhoods in one place (along with a sampling of restaurants in each neighborhood).  I also included functionality that allows sellers to post housing for rent to these potential buyers and functionality for the buyers to email the sellers directly through the app.

## About the Author
I'm a former Googler with 9+ years of experience spanning across program management, technical recruiting and human resources ([see Linkedin here](https://www.linkedin.com/in/sanaahmad/)).

## Contents
* [Technologies](#tech-stack)
* [APIs](#apis)
* [Features](#features)
* [Installation](#installation)

## <a name="tech-stack"></a>Technologies
* React
* React Router
* Javascript
* Python
* Flask
* PostgreSQL
* SQLAlchemy ORM
* React Bootstrap
* Material Design Bootstrap

## <a name="apis"></a>APIs
* Google Maps Javascript API
* Google Places API
* EmailJS SendGrid API
* Cloudinary API

## <a name="features"></a>Features

#### Homepage
Users are welcomed to the site with the homepage below. The navigation bar conditionally renders elements based on whether the user is logged in.


![alt text](https://res.cloudinary.com/sana3339/image/upload/v1623187769/samples/Frisco%20App%20Images/Homepage_yeguel.png "homepage")

#### Explore Neighborhoods
Users can hover over the map markers to see a short description and image of neighborhoods before choosing which neighborhood's marker to click on to dive in further.  This functionality is enabled via Google Maps Javascript API.

![alt text](https://github.com/Sana3339/Frisco-React/blob/master/static/img/neighborhoods.gif "explore neighborhoods")

#### Discover Neighborhood Details
When a user clicks on a marker, they're taken to the neighborhood details page where they can see a more in-depth description of the neighborhood along with stats about the median rental price, median home price, median sq.foot price, walk score and transit score. 

Users are also provided with a sampling of 4 restaurants in the neighborhood.  The restaurants, their websites and photos are supplied by Google Places API.  Clicking on the website link will open a new tab with the restaurant's website.

![alt text](https://res.cloudinary.com/sana3339/image/upload/v1623188724/samples/Frisco%20App%20Images/Neighborhood_details_dyxygk.png "neighborhood details")

#### Explore Neighborhood Housing/ Send Emails to Sellers of Housing Postings
When users click on the "Find Housing" button in the neighborhood details page, they are taken to a list of available housing posted for that particular neighborhood.  

If users are interested in a posting, clicking on the "Contact Seller" page takes them to a form where they can anonymously email the seller who posted the housing.  This functionality is enabled via the EmailJS SendGrid API.

#### Login/ Create Account
From the Neighborhood Details page, if a user clicks on the "Post Housing" button, Frisco checks whether the user is logged in, and if they're not, they are redirected to the login page via a React Protected Route. 

If the user doesn't have an account, there is a link in the login page as well as the navigation bar to route them to the page where they can create one.

#### Post Housing
Once a user is logged in, they may post housing.  The post housing form allows users to upload an image via the Cloudinary API.

#### Profile
Once users submit the posting form, their post is visible on their profile page as well as under the neighborhood page that they posted the housing in.  Other users can anonymously email them if they are interested in the posting (per the 'send email to sellers' functionality described above).




