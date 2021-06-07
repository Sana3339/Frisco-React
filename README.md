# Frisco
Description here

## About the Author
Sana is a former Googler with 9+ years of experience spanning across program management, technical recruiting and human resources.  She has a B.S. in Business from the University of Southern California ([see Linkedin here](https://www.linkedin.com/in/sanaahmad/)).

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

#### Explore Neighborhoods
Users can hover over the map markers to see a short description and image of neighborhoods before choosing which neighborhood's marker to click on to dive in further.  This functionality is enabled via Google Maps Javascript API.

#### Discover Neighborhood Details
When a user clicks on a neighborhood marker, they're taken to the neighborhood details page where they can see a more in-depth description of the neighborhood along with stats about the median rental price, median home price, median sq.foot price, walk score and transit score. 

Users are also provided a sampling of 4 restaurants in the neighborhood.  The restaurants, their websites and photos are supplied by Google Places API.  Clicking on the website link will open a new tab with the restaurant's website.

#### Explore Neighborhood Housing/ Send Emails to Sellers of Housing Postings
When users click on the "Find Housing" button in the neighborhood details page, they are taken to a list of available housing posted for that particular neighborhood.  

If users are interested in a posting, clicking on the "Contact Seller" page takes them to a form where they can anonymously email the seller who posted the housing.  This functionality is enabled via the EmailJS SendGrid API.

#### Login/ Create Account
From the Neighborhood Details page, if a user clicks on the "Post Housing" button, Frisco checks whether the user is logged in, and if not, they are redirected to the login page via a React Protected Route.  Once the user is logged in, they are dropped back to the post housing page for the particular neighborhood where they were originally seeking to post housing.  

If the user doesn't have an account, there is a link in the login page as well as the navigation bar to route them to the page where they can create one.

#### Post Housing
Once a user is logged in, they may post housing.  The post housing form allows users to upload an image via the Cloudinary API.

#### Profile
Once users submit the posting form, their post is visible on their profile page as well as under the neighborhood page that they posted the housing in.  Other users can anonymously email them if they are interested in the posting (per the 'send email to sellers' functionality described above).




