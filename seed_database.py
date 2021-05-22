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
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The neighborhood is primary residential with a commercial strip along
                    Corland Ave featuring restaurants, bars, bakeries, a fish and butchery 
                    shop and more.  It's home to the open-air Alemany Farmers' Market, 
                    one of the oldest extant farmers' markets in the US.  Bernal has not 
                    gentrified to the extent of its neighbor Noe Valley, but gentrification 
                    and property values are increasing as urban professionals replace 
                    working-class home owners and renters""",
    'median_rent': 2500,
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
    'short_desc': """<div style='float:right'><img src='/static/img/castro_thumb.jpg' width="150" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Castro</b> was one of the first gay neighborhoods in the US.
                    It's currently among the most prominent symbols of lesbian, gay,
                    bisexual and transgender (LGBT) activism and events in the world. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Castro was one of the first gay neighborhoods in the US. One of its more
                    notable features is Castro Theatre, a movie palace built in 1922 and one of 
                    San Francisco's premier movie houses. 18th and Castro is a major intersection 
                    where many historic events, marches, and protests have taken and continue to take place.
                    The Castro is a "thriving marketplace for all things gay" meaning everything 
                    in the area is catered to people who identify with LGBT culture and other associated 
                    meanings to the word gay.  There are cafes, the Castro Theater, and many businesses 
                    that cater to or openly welcome LGBT consumers. These establishments make the Castro 
                    an area of high spending and lead to high tourist traffic.""",
    'median_rent': 2697,
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
    'short_desc': """<div style='float:right'><img src='/static/img/haight_thumb.png' width="150" height="110"></div>
                    <div style='float:left; height:120px; width:180px;'><b>Haight-Ashbury</b> 
                    is known as a main center of the 
                    hippie and counterculture of the 1960s. The Summer of Love (1967)
                    has been synonymous with the neighborhood ever since. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Haight-Ashbury is known as one of the main centers of the 
                    hippie and counterculture of the 1960s. The mainstream media's 
                    coverage of hippie life in the Haight-Ashbury drew the attention 
                    of youth from all over America. The Haight-Ashbury 
                    district was sought out by hippies to constitute a community based 
                    upon counterculture ideals, drugs, and music. This neighborhood 
                    offered a concentrated gathering spot for hippies to create a social 
                    experiment that would soon spread throughout the nation.""",
    'median_rent': 2595,
    'median_home_price': 3540000,
    'sq_ft_price': 1221,
    'walk_score': 97,
    'transit_score': 80,
    'images': '/static/img/haight1.png, /static/img/haight2.jpeg, /static/img/haight3.jpeg'   
    },
      {
    'neighborhood_id': 'japantown',
    'name': 'Japantown',
    'latitude': 37.7854,
    'longitude': -122.4294,
    'short_desc': """<div style='float:right'><img src='/static/img/japantown_thumb.png' width="150" height="110"></div>
                    <div style='float:left; height:120px; width:180px;'>
                    <b>Japantown</b> 
                    is home to Japanese restaurants, supermarkets, indoor shopping malls,
                    hotels, banks and more. It's considered one of the largest and oldestest
                    ethnic encleves in the US.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Japantown celebrates 2 major festivals every year: The Cherry Blossom Festival 
                    and the Nihonmaschi Street Fair. Its focal point is the Japan Center and is the 
                    site of 3 Japanese-oriented shopping centers. The area is within the SF Unified
                    School District and Rosa Parks Elementary School is located nearby.""",
    'median_rent': 2400,
    'median_home_price': 875000,
    'sq_ft_price': 987,
    'walk_score': 96,
    'transit_score': 89,
    'images': ''   
    },
    {
    'neighborhood_id': 'marina',
    'name': 'Marina',
    'latitude': 37.8037,
    'longitude': -122.4368,
    'short_desc': """<div style='float:right'><img src='/static/img/marina_thumb.png' width="150" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Marina</b> has the highest non-Hispanic white resident percentage of any neighborhood in SF. 
                    Chestnut Street is an attraction, lined with stores, restaurants, coffee shops and bars.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Marina is most famous for the Palace of Fine Arts, which is a year-round attraction
                    for tourists and locals and is used as a location for weddings and wedding-related photography.

                    The neighborhood is also noted for its demographics, which since the 1980s have shifted 
                    from mostly middle-class families and pensioners to professionals in their twenties 
                    and thirties. These now make up more than half of the population, although a small, 
                    affluent older population remains""",
    'median_rent': 2925,
    'median_home_price': 4296000,
    'sq_ft_price': 1394,
    'walk_score': 98,
    'transit_score': 75,
    'images': '/static/img/marina1.jpeg, /static/img/marina2.jpeg, /static/img/marina3.jpeg'
    },
    {
    'neighborhood_id': 'mission',
    'name': 'Mission',
    'latitude': 37.7599,
    'longitude': -122.4148,
    'short_desc': """<div style='float:right'><img src='/static/img/mission_thumb.png' width="160" height="110" vertical-align="middle"></div>
                    <div style='float:left; height:120px; width:180px;'>
                    The <b>Mission</b> has been the center of the city's Chicano/Mexican-American community
                    and is often warmer and sunnier than other parts of the city. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Mission includes four recognized sub-districts. The northeastern 
                    quadrant is known as a center for high tech startup businesses including some 
                    chic bars and restaurants. The northwest quadrant is famous for Victorian mansions
                    and the popular Dolores Park. Two main commercial zones in the south central part of 
                    the Mission District are both popular destinationsfor their restaurants, bars, 
                    galleries and street life.""",
    'median_rent': 2500,
    'median_home_price': 1765000,
    'sq_ft_price': 967,
    'walk_score': 99,
    'transit_score': 85,
    'images': '/static/img/mission1.jpg, /static/img/mission2.jpeg, /static/img/mission3.jpeg'        
    },
    {
    'neighborhood_id': 'financial',
    'name': 'Financial District',
    'latitude': 37.7946,
    'longitude': -122.3999,
    'short_desc': """<div style='float:right'><img src='/static/img/financial_thumb.jpeg' width="150" height="120"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Financial District</b> serves as SF's main business district, housing 
                    the city's largest concentration of corporate headquarters, law firms,
                    real estate firms and other financial institutions.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Financial District is home to numerous corporate headquarters including
                    6 Fortune 500 companies.  The area is marked by a cluster of high-rise towers 
                    and several shopping malls including the Ferry Building Marketplace where a 
                    farmer's market is held every Saturday.  

                    The Financial District is served by more than two dozen Muni bus and rail lines, 
                    including one cable car line, as well as Montgomery Street Station and 
                    Embarcadero Station in the BART system.""",
    'median_rent': 3293,
    'median_home_price': 1599000,
    'sq_ft_price': 1283,
    'walk_score': 99,
    'transit_score': 100,
    'images': '/static/img/financial1.jpeg, /static/img/financial2.jpeg, /static/img/financial3.jpeg'     
    },
    {
    'neighborhood_id': 'nob',
    'name': 'Nob Hill',
    'latitude': 37.7930,
    'longitude': -122.4161,
    'short_desc': """<div style='float:right'><img src='/static/img/nob_thumb.jpeg' width="150" height="110" vertical-align="middle"></div>
                    <div style='float:left; height:115px; width:170px;'>
                    <b>Nob Hill</b> is known for its numerous luxury hotels and historic mansions.
                    It has historically served as a center of San Francisco's upper class.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Nob Hill is among the highest-income neighborhoods in the US and one
                    of the most desirable and expensive real estate markets in the country. 
                    It's a luxury destination in San Francisco, owing to its numerous
                    Michelin-starred restaurants, boutiques, cultural institutions, art galleries,
                    and historic landmarks. It's home to many of the city's upper class families
                    as well as a large young urban professional population and a growing Chinese
                    immigrant population from Chinatown to the east.""",
    'median_rent': 2500,
    'median_home_price': 1280000,
    'sq_ft_price': 1149,
    'walk_score': 99,
    'transit_score': 100,
    'images': '/static/img/nob1.jpeg, /static/img/nob2.webp, /static/img/nob3.jpg'    
    },
    {
    'neighborhood_id': 'noe',
    'name': 'Noe Valley',
    'latitude': 37.7502,
    'longitude': -122.4337,
    'short_desc': """<div style='float:right'><img src='/static/img/noe1.jpg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>Noe Valley</b> is home to many young professional
                    couples with children and is known as 'Stroller Valley'. Its microclimate is 
                    sunnier and warmer than other neighborhoods. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Noe Valley started is considered an upper-middle class/wealthy 
                    neighborhood. It's home to many urban professionals, particularly young 
                    couples with children. It is colloquially known as Stroller Valley, 
                    for the many strollers in the neighborhood. 
                    One of the attractions of Noe Valley is that the adjacent 
                    Twin Peaks partly blocks the coastal fog and cool winds from the 
                    Pacific, making the microclimate usually sunnier and warmer than 
                    surrounding neighborhoods.""",
    'median_rent': 2495,
    'median_home_price': 2800000,
    'sq_ft_price': 1383,
    'walk_score': 92,
    'transit_score': 73,
    'images': '/static/img/noe1.jpg, /static/img/noe2.jpeg, /static/img/noe3.jpeg'      
    },
    {
    'neighborhood_id': 'north',
    'name': 'North Beach',
    'latitude': 37.8061,
    'longitude': -122.4103,
    'short_desc': """<div style='float:right'><img src='/static/img/north_thumb.jpg' width="150" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>North Beach</b> has many Italian restaurants
                    and is one of SF's main nightlife districts as well as a 
                    residential neighborhood populated with young urban professionals, 
                    families, and Chinese immigrants. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """North Beach is San Francisco's "Little Italy" and has historically been home to a
                large Italian American population. It still has many Italian restaurants, although many other
                ethnic groups currently live in the neighborhood. It was also the historic center of beatnik
                subculture and has become one of San Francisco's main nightlife districts.

                The North Beach Festival street fair held annually in June is considered the city's oldest
                and largest street fair.
                """,
    'median_rent': 2600,
    'median_home_price': 1285000,
    'sq_ft_price': 1196,
    'walk_score': 99,
    'transit_score': 95,
    'images': '/static/img/north1.jpeg, /static/img/north2.jpg, /static/img/north3.jpeg'    
    },
    {
    'neighborhood_id': 'pac',
    'name': 'Pacific Heights',
    'latitude': 37.7925,
    'longitude': -122.4382,
    'short_desc': """<div style='float:right'><img src='/static/img/pac_thumb.png' width="160" height="110" vertical-align="middle"></div>
                    <div style='float:left; height:120px; width:180px;'>
                    <b>Pacific Heights</b> has panoramic views of the Golden Gate Bridge, 
                    San Francisco Bay, the Palace of Fine Arts and the Presidio.
                    It's SF's most expensive neighborhood. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """If Pacific Heights had its own zip code, it would be one of the most expensive
                    places to live in the United States.  The area is famous for its billionaire 
                    residents and record-breaking prices.   

                    It features two parks, Lafayette and Alta Plaza, and boasts fantastic
                    views. Visible to the north are the Golden Gate Bridge, the Marin Headlands, 
                    and Alcatraz Island. Visible to the south are Twin Peaks and the Sutro Tower.""",
    'median_rent': 2895,
    'median_home_price': 5600000,
    'sq_ft_price': 1620,
    'walk_score': 96,
    'transit_score': 89,
    'images': '/static/img/pac1.jpg, /static/img/pac2.webp, /static/img/pac3.jpeg'    
    },
    {
    'neighborhood_id': 'potrero',
    'name': 'Potrero Hill',
    'latitude': 37.7605,
    'longitude': -122.4009,
    'short_desc': """<div style='float:right'><img src='/static/img/potrero1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>Potrero Hill</b> is known for its views of the San Francisco Bay and city skyline, 
                    its proximity to many destination spots, its sunny weather, and having 
                    two freeways and a Caltrain station. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Potrero Hill is one of the sunniest neighborhoods in San Francisco.
                    It's a residential neighborhood and not considered a tourist destination. 
                    Although it's most walkable neighborhood in San Francisco due to 
                    its hills, it's generally considered a convenient location due to its 
                    proximity to offices, shopping, dining, entertainment, 
                    freeways and a Caltrain station. Despite being surrounded by busy 
                    neighborhoods, Potrero Hill is generally quiet and sleepy.""",
    'median_rent': 3047,
    'median_home_price': 1898000,
    'sq_ft_price': 1101,
    'walk_score': 89,
    'transit_score': 75,
    'images': '/static/img/potrero1.jpeg, /static/img/potrero2.jpeg, /static/img/potrero3.jpeg'     
    },
    {
    'neighborhood_id': 'presidio',
    'name': 'Presidio',
    'latitude': 37.7989,
    'longitude': -122.4662,
    'short_desc': """<div style='float:right'><img src='/static/img/presidio_thumb.jpg' width="150" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Presidio</b> is a park and former U.S. Army military fort. It's characterized 
                    by wooded areas, hills, and scenic vistas overlooking the Golden Gate Bridge, 
                    San Francisco Bay, and the Pacific Ocean. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Presidio is a park and former U.S. Army military fort and is part of 
                    the Golden Gate National Recreation Area. A major planned component of the Presidio's 
                    park attractions is the Tunnel Tops project, which would construct a 14-acre park 
                    slated to be openfor public use in 2021.  It houses several visitors centers and 
                    Crissy Field Center, an urban environmental education center with programs 
                    for schools, public workshops, after-school programs, summer camps, and more.""",
    'median_rent': 2990,
    'median_home_price': 3600000,
    'sq_ft_price': 1200,
    'walk_score': 41,
    'transit_score': 59,
    'images': '/static/img/presidio1.jpeg, /static/img/presidio2.jpeg, /static/img/presidio3.gif'   
    },
    {
    'neighborhood_id': 'richmond',
    'name': 'Inner Richmond',
    'latitude': 37.7781,
    'longitude': -122.4673,
    'short_desc': """<div style='float:right'><img src='/static/img/richmond_thumb.png' width="150" height="110" vertical-align="middle"></div>
                    <div style='float:left; height:120px; width:180px;'>
                    <b>Inner Richmond</b> is known for its Chinese, 
                    Cambodian, Korean, Burmese, and Russian cuisine. It's a diverse
                    area with sizable Chinese and Russian populations. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Richmond has influences from the Chinese-American culture and of its 
                    three commercial strips, Clement Street, is sometimes called the second 
                    Chinatown due to the high concentration 
                    of Chinese establishments.  The Richmond also has deep Irish and 
                    Russian roots and has many Catholic and Orthodox churches.""",
    'median_rent': 2400,
    'median_home_price': 2305000,
    'sq_ft_price': 1016,
    'walk_score': 94,
    'transit_score': 77,
    'images': '/static/img/richmond1.jpg, /static/img/richmond2.jpeg, /static/img/richmond3.jpeg'   
    },
    {
    'neighborhood_id': 'russian',
    'name': 'Russian Hill',
    'latitude': 37.8011,
    'longitude': -122.4194,
    'short_desc': """<div style='float:right'><img src='/static/img/russian_thumb.jpg' width="150" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    Views from the top of <b>Russian Hill</b> include the Bay Bridge, 
                    Marin County, and the Golden Gate Bridge. Tourists frequent the cable car 
                    line along Hyde Street, which is lined with restaurants and shops.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Russian Hill is one of San Francisco's original "Seven Hills."
                    At the northern foot of the hill is Ghiradelli Square, Aquatic Park, and
                    Fisherman's Wharf, a popular tourist area.
                    It's most famous for Lombard St, a one-way street 
                    in which the roadway has eight sharp turns that have earned 
                    the street the distinction of being "the crookedest street in the world". 
                    Because of the steepness of the hill, many streets are staircases.""",
    'median_rent': 2800,
    'median_home_price': 3850000,
    'sq_ft_price': 1408,
    'walk_score': 97,
    'transit_score': 93,
    'images': '/static/img/russian1.jpeg, /static/img/russian2.jpeg, /static/img/russian3.jpeg'   
    },
    {
    'neighborhood_id': 'soma',
    'name': 'SoMA',
    'latitude': 37.7785,
    'longitude': -122.4056,
    'short_desc': """<div style='float:right'><img src='/static/img/soma.jpg' width="140" height="100" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    <b>SoMa</b> houses museums, technology companies, warehouses, 
                    auto repair shops, nightclubs, residential hotels, art spaces, 
                    loft apartments, furniture showrooms and condominiums.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Many major software and technology companies have headquarters and offices 
                    here and the area is home to The area is also home to the few Big-box 
                    stores in San Francisco such as Costco, REI, Nordstrom Rack, and Best Buy.
                    SOMA is home to many of San Francisco's museums, including SFMOMA, the Yerba 
                    Buena Center for the Arts and more.""",
    'median_rent': 2800,
    'median_home_price': 1122500,
    'sq_ft_price': 917,
    'walk_score': 97,
    'transit_score': 100,
    'images': '/static/img/soma1.png, /static/img/soma2.jpeg, /static/img/soma3.jpeg'   
    }, 
    {
    'neighborhood_id': 'sunset',
    'name': 'Inner Sunset',
    'latitude': 37.7602,
    'longitude': -122.4703,
    'short_desc': """<div style='float:right'><img src='/static/img/sunset1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Inner Sunset</b> has a variety of local businesses including restaurants, 
                    bars, breweries, book stores, bakeries, ice cream parlors, 
                    clothing stores, a tattoo parlor, a wine bar and more.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Sunset district has a cool summer mediterranean 
                    climate, albeit with an unusual annual temperature distribution. 
                    The warmest days of the year occur in October and then the coldest 
                    nights of the year occur just two months later in December.

                    There is a year-round, Sunday morning farmers' market offering 
                    California-grown produce, fish, eggs, and meat, as well as local food 
                    vendors and artisans.  It also includes Stern Grove, a heavily wooded park 
                    and amphitheater, known for its annual summer festival.""",
    'median_rent': 2395,
    'median_home_price': 1850000,
    'sq_ft_price': 1033,
    'walk_score': 95,
    'transit_score': 72,
    'images': '/static/img/sunset1.jpeg, /static/img/sunset2.jpeg, /static/img/sunset3.jpeg'  
    },
    {
    'neighborhood_id': 'tenderloin',
    'name': 'Tenderloin',
    'latitude': 37.7847,
    'longitude': -122.4145,
    'short_desc': """<div style='float:right'><img src='/static/img/tenderloin1.jpeg' width="120" height="120" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;'>
                    The <b>Tenderloin</b> has resisted gentrification, maintaining a seedy character
                    and reputation for crime. Squalid conditions, homelessness, drugs and 
                    prostitution are prevalent.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Tenderloin is a high-crime neighborhood, particularly violent street crime such
                as robbery and aggravated assault. Graffiti and art tagging are a common problem in the 
                neighborhood, as are dealing and use of illicit drugs occuring on the streets. It serves as a mecca
                for the art scene in SF and is home to mural work by a number of artists.""",
    'median_rent': 1895,
    'median_home_price': 970000, 
    'sq_ft_price': 957,
    'walk_score': 99,
    'transit_score': 100,
    'images': ''  
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
                                       

#Add images to neighborhooods

images = [
    {
        'image_name':'haight1.png',
        'neighborhood_id': 'haight'
    },
    {
        'image_name':'soma1.png',
        'neighborhood_id': 'soma'
    },
    {
        'image_name':'nob1.jpg',
        'neighborhood_id': 'nob'
    }
]

for image in images:
    image_name = image['image_name']
    neighborhood_id = image['neighborhood_id']

    crud.add_image(image_name, neighborhood_id)


#Create fake users with which to seed the db

for n in range(10):
    email = f'user{n}@test.com' 
    password = 'test'

    crud.create_user(email, password)

#Create fake postings with which to seed the db

postings = [
    {
    'neighborhood_id': 'marina',
    'user_email': 'user1@test.com',
    'date': datetime.now(),
    'title': 'Beautiful room by the Palace of Fine Arts',
    'desc': 'Gorgeous panoramic views.  Youll be living in a house with 2 other girls.',
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1620836686/sp46yz9ltklqlt5wj20c.jpg'
    },
    {
    'neighborhood_id': 'mission',
    'user_email': 'user2@test.com',
    'date': datetime.now(),
    'title': 'Room available immediately in 2b/2b',
    'desc': 'Great location right by Valencia street with lots of restaurants',
    'contact_info': 'sanaahmad393@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1620836601/vgq5mlbxqdhfzxgejy1z.gif'
    }
]

for posting in postings:

    neighborhood_id = posting['neighborhood_id']
    user_email = posting['user_email']
    title = posting['title']
    desc = posting['desc']
    contact_info = posting['contact_info']
    image_url = posting['image_url']
    date = posting['date']

    crud.create_posting(neighborhood_id, user_email, date, title, desc, contact_info, image_url)

