"""Script to seed database with test data. This only needs to be run once."""

import os
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
    'short_desc': """<div style='float:right'><img src='/static/img/bernal_thumb.jpeg' width="160"
                    height="140" vertical-align="middle"></div>
                    <div style='float:left; height:140px; width:140px; font-size:0.88rem;'>
                    <b>Bernal Heights</b> is a primarily residential neighborhood with a commercial strip
                    and a farmer's market every Saturday.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The neighborhood is primarily residential with a commercial strip along
                    Corland Ave featuring restaurants, bars, bakeries, a fish and butchery
                    shop and more.  It's home to the open-air Alemany Farmers' Market,
                    one of the oldest extant farmers' markets in the US.  Bernal has not
                    gentrified to the extent of its neighbor Noe Valley, but gentrification
                    and property values are increasing as urban professionals replace
                    working-class home owners and renters.""",
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
    'short_desc': """<div style='float:right'><img src='/static/img/castro_thumb.jpg' width="160" height="135" vertical-align="middle"></div>
                    <div style='float:left; height:135px; width:180px; font-size:0.88rem;'>
                    The <b>Castro</b> was one of the first gay neighborhoods in the US.
                    It's currently among the most prominent symbols of lesbian, gay,
                    bisexual and transgender (LGBT) activism and events in the world.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Castro was one of the first gay neighborhoods in the US. 18th and Castro is a major intersection
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
    'short_desc': """<div style='float:right'><img src='/static/img/haight_thumb.png' width="160" height="140"></div>
                    <div style='float:left; height:140px; width:180px;font-size:0.88rem;'><b>Haight-Ashbury</b>
                    is known as a main center of the
                    hippie and counterculture of the 1960s. The 'Summer of Love'
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
    'short_desc': """<div style='float:right'><img src='/static/img/japantown_thumb.jpg' width="150" height="140"></div>
                    <div style='float:left; height:140px; width:180px;font-size:0.88rem;'>
                    <b>Japantown</b>
                    is home to Japanese restaurants, supermarkets, shopping malls,
                    hotels, banks and more. It's considered one of the largest and oldest
                    ethnic encleves in the US.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Japantown celebrates 2 major festivals every year: the Cherry Blossom Festival
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
    'short_desc': """<div style='float:right'><img src='/static/img/marina_thumb.png' width="150" height="150" vertical-align="middle"></div>
                    <div style='float:left; height:150px; width:180px;font-size:0.88rem;'>
                    The <b>Marina</b> has the highest non-Hispanic white resident percentage of any neighborhood in SF.
                    Chestnut Street is an attraction, lined with stores, restaurants, coffee shops and bars.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Marina is most famous for the Palace of Fine Arts, which is a year-round attraction
                    for tourists and locals and is used as a location for weddings and wedding-related photography.

                    The neighborhood is also noted for its demographics, which since the 1980s have shifted
                    from mostly middle-class families and pensioners to professionals in their twenties
                    and thirties. These now make up more than half of the population, although a small,
                    affluent older population remains.""",
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
                    <div style='float:left; height:120px; width:180px;font-size:0.88rem;'>
                    The <b>Mission</b> has been the center of the city's Chicano/Mexican-American community
                    and is often warmer and sunnier than other parts of the city.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Mission includes four recognized sub-districts. The northeastern
                    quadrant is known as a center for high-tech startup businesses including some
                    chic bars and restaurants. The northwest quadrant is famous for Victorian mansions
                    and the popular Dolores Park. Two main commercial zones in the south central part of
                    the Mission District are both popular destinations for their restaurants, bars,
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
    'short_desc': """<div style='float:right'><img src='/static/img/financial_thumb.jpeg' width="150" height="150"></div>
                    <div style='float:left; height:150px; width:180px;font-size:0.88rem;'>
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
                    <div style='float:left; height:115px; width:170px;font-size:0.88rem;'>
                    <b>Nob Hill</b> is known for its numerous luxury hotels and historic mansions.
                    It has historically served as a center of San Francisco's upper class.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Nob Hill is among the highest-income neighborhoods in the United States and one
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
    'short_desc': """<div style='float:right'><img src='/static/img/noe_thumb.jpeg' width="170" height="140" vertical-align="middle"></div>
                    <div style='float:left; height:140px; width:180px;font-size:0.88rem;'>
                    <b>Noe Valley</b> is home to many young professional
                    couples with children and is known as 'Stroller Valley'. Its microclimate is
                    sunnier and warmer than other neighborhoods. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Noe Valley is considered an upper-middle class/wealthy
                    neighborhood. It's home to many urban professionals, particularly young
                    couples with children. It is colloquially known as Stroller Valley
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
    'short_desc': """<div style='float:right'><img src='/static/img/north_thumb.jpg' width="150" height="150" vertical-align="middle"></div>
                    <div style='float:left; height:150px; width:180px;font-size:0.88rem;'>
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
    'short_desc': """<div style='float:right'><img src='/static/img/pac_thumb.png' width="160" height="140" vertical-align="middle"></div>
                    <div style='float:left; height:140px; width:180px;font-size:0.88rem;'>
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
    'short_desc': """<div style='float:right'><img src='/static/img/potrero_thumb.jpeg' width="150" height="135" vertical-align="middle"></div>
                    <div style='float:left; height:135px; width:180px;font-size:0.88rem;'>
                    <b>Potrero Hill</b> is known for its views of the SF Bay and city skyline,
                    its proximity to many destination spots, its sunny weather, and having
                    2 freeways and a Caltrain station. 
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Potrero Hill is one of the sunniest neighborhoods in San Francisco.
                    It's a residential neighborhood and not considered a tourist destination.
                    Although it's the most walkable neighborhood in San Francisco due to
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
    'short_desc': """<div style='float:right'><img src='/static/img/presidio_thumb.jpg' width="160" height="140" vertical-align="middle"></div>
                    <div style='float:left; height:140px; width:180px;font-size:0.88rem;'>
                    The <b>Presidio</b> is a park and former U.S. Army military fort. It's characterized
                    by wooded areas, hills, and scenic vistas overlooking the Golden Gate Bridge,
                    SF Bay, and the Pacific Ocean.
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
    'short_desc': """<div style='float:right'><img src='/static/img/richmond_thumb.png' width="150" height="135" vertical-align="middle"></div>
                    <div style='float:left; height:135px; width:180px;font-size:0.88rem;'>
                    <b>Inner Richmond</b> is known for its Chinese,
                    Cambodian, Korean, Burmese, and Russian cuisine. It's a diverse
                    area with sizable Chinese and Russian populations.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Richmond has influences from Chinese-American culture, and of its
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
    'short_desc': """<div style='float:right'><img src='/static/img/russian_thumb.jpg' width="150" height="140" vertical-align="middle"></div>
                    <div style='float:left; height:140px; width:180px;font-size:0.88rem;'>
                    Views from the top of <b>Russian Hill</b> include the Bay Bridge,
                    Marin County, and the GG Bridge. Tourists frequent the cable car
                    line along Hyde St, which is lined with restaurants and shops.
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
    'short_desc': """<div style='float:right'><img src='/static/img/soma_thumb.jpg' width="150" height="130" vertical-align="middle"></div>
                    <div style='float:left; height:130px; width:180px;font-size:0.88rem;'>
                    <b>SoMa</b> houses museums, tech companies, warehouses,
                    nightclubs, residential hotels, art spaces,
                    loft apartments, furniture showrooms and condos.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """Many major software and technology companies have headquarters and offices
                    here and the area is home to the few Big-box
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
    'short_desc': """<div style='float:right'><img src='/static/img/sunset_thumb.jpeg' width="160" height="135" vertical-align="middle"></div>
                    <div style='float:left; height:135px; width:180px;font-size:0.88rem;'>
                    The <b>Inner Sunset</b> has a variety of local businesses including restaurants,
                    bars, breweries, book stores, bakeries, ice cream parlors,
                    clothing stores, a wine bar and more.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Sunset district has a cool summer mediterranean
                    climate, albeit with an unusual annual temperature distribution.
                    The warmest days of the year occur in October and the coldest
                    nights of the year occur just two months later in December.

                    There is a year-round Sunday morning farmers' market offering
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
    'short_desc': """<div style='float:right'><img src='/static/img/tenderloin_thumb.jpg' width="160" height="125" vertical-align="middle"></div>
                    <div style='float:left; height:125px; width:180px;font-size:0.88rem;'>
                    The <b>Tenderloin</b> has a seedy character
                    and reputation for crime. Squalid conditions, homelessness, drugs and
                    prostitution are prevalent.
                    <b>Click the marker</b> to learn more.""",
    'long_desc': """The Tenderloin is a high-crime neighborhood, particularly violent street crime such
                as robbery and aggravated assault. Graffiti and art tagging are a common problem in the
                neighborhood, as are dealing and use of illicit drugs occuring on the streets. It serves as a mecca
                for the art scene in San Francisco and is home to mural work by a number of artists.""",
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
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624399300/bernal_ys8txu.jpg',
        'neighborhood_id': 'bernal'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624399391/castro_bbmxlo.jpg',
        'neighborhood_id': 'castro'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624399470/financial_final_small_f4f8ka.jpg',
        'neighborhood_id': 'financial'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624399550/haight_e9cmj3.jpg',
        'neighborhood_id': 'haight'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624399584/mission_final_small_nwhsi6.jpg',
        'neighborhood_id': 'mission'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624399623/inner_richmond_uxzsqp.jpg',
        'neighborhood_id': 'richmond'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624399703/japantown_o2fuxv.jpg',
        'neighborhood_id': 'japantown'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1622775287/rd9j5t57rapuhkrijevq.jpg',
        'neighborhood_id': 'marina'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624399736/nob_hill_final_small_jlf3xo.jpg',
        'neighborhood_id': 'nob'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624399761/noe_xknd2z.jpg',
        'neighborhood_id': 'noe'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624399951/north_beach_final_small_nxhqhi.jpg',
        'neighborhood_id': 'north'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624400037/pacific_heights_final_small_aokvaa.jpg',
        'neighborhood_id': 'pac'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624400091/potrero_hill_nsvctn.jpg',
        'neighborhood_id': 'potrero'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624400153/presidio_final_small_zrvk6a.jpg',
        'neighborhood_id': 'presidio'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624400312/russian_hill_final_small_rscrnb.jpg',
        'neighborhood_id': 'russian'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624400375/soma1_b7rypy.png',
        'neighborhood_id': 'soma'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624400415/sunset_sf9awd.jpg',
        'neighborhood_id': 'sunset'
    },
    {
        'image_name':'https://res.cloudinary.com/sana3339/image/upload/v1624400471/tenderloin_final_small_fzgq2w.jpg',
        'neighborhood_id': 'tenderloin'
    }
]

for image in images:
    image_name = image['image_name']
    neighborhood_id = image['neighborhood_id']

    crud.add_image(image_name, neighborhood_id)


#Create fake users with which to seed the db

for n in range(40):
    email = f'user{n}@test.com'
    password = 'test'

    crud.create_user(email, password)

#Create fake postings with which to seed the db

postings = [
    {
    'neighborhood_id': 'bernal',
    'user_email': 'user30@test.com',
    'date': datetime.now(),
    'title': '$2,395 / 1br - One Bedroom Unit Overlooking Precita Park',
    'desc': """Available for lease is a one-bedroom, one-bath unit on the third floor at
                the corner of Folsom Street and Bessie. The mixed use building has three
                residences along with the popular Los Yaquis restaurant. Some carpet, some
                laminate in the bedroom and living room and tile in the lone bathroom. The
                living room has views of the eastern edge of Precita Park. Schools, shopping,
                cafes, easy access to both The Mission and Highway 101, it's all right here.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622158308/bernal1_pcvvjk.jpg'
    },
    {
    'neighborhood_id': 'bernal',
    'user_email': 'user29@test.com',
    'date': datetime.now(),
    'title': '$2,995 / 1br - 652ft2 - 3264 Mission',
    'desc': """Situated on a hidden-gem-studded stretch of Mission, this building is flooded
                with sunshine from dawn to dusk. These approachable apartments are chock full
                of vintage flair; custom built ins and hardwood floors leave a lasting impression.
                The classic touches are matched only by the stainless steel appliances in the
                modern kitchen and in-unit laundry.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622158380/bernal2_vakap3.jpg'
    },
    {
    'neighborhood_id': 'castro',
    'user_email': 'user1@test.com',
    'date': datetime.now(),
    'title': '$2,795 / 1br - Bright Remodeled Top Floor Corner View Apt w/ HW! Free Rent!',
    'desc': """This unit is located in small building tucked away between Duboce Avenue and Market
            Street, very quite street. While technically in the Inner Mission District, it borders SOMA,
            Castro and Hayes Valley.  A Walker's Paradise with Destino, Pisco, Zuni Cafe and so many great
            restaurants right out your front door!  Safeway and Whole Foods all within walking distance.
            A Rider's Paradise (Transit score of 100) with so many options getting you where you need to be. """,
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622072595/castro_hiwx89.jpg'
    },
    {
    'neighborhood_id': 'castro',
    'user_email': 'user2@test.com',
    'date': datetime.now(),
    'title': '$2,595 / 1br - Remodeled Top Floor Apartment Steps from Duboce Park! ',
    'desc': """Beautifully updated 1-bedroom, 1-bathroom 1/2 floor flat located on the top floor of a
                quaint 4-unit Victorian building! Classic San Francisco details coupled with modern
                conveniences truly make this cozy apartment shine! The open south-facing living room +
                kitchen make for a wonderful place to soak in the sun and entertain guests. The living
                room boasts tall Bay windows, a sweet gas furnace with tile surround and vintage
                chandelier above. The open kitchen has been updated with brand new hardwood floors,
                ample cabinetry, large refrigerator, and gas range/oven. Gorgeous glass paneled pocket
                doors separate the living room from the bedroom retreat! The bedroom hosts multiple large
                closets and connects to a newly remodeled sleek bathroom.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622143480/castro1_lp6uxe.jpg'
    },
    {
    'neighborhood_id': 'financial',
    'user_email': 'user3@test.com',
    'date': datetime.now(),
    'title': '$2,795 / 1br - Bright Remodeled Top Floor Corner View Apt w/ HW! Free Rent!',
    'desc': """Inspired by San Francisco's famously vertical topography, the four distinctive towers
            of the Gateway define the most spacious residential neighborhood within the Financial
            District with Walk Score of 98. Our San Francisco apartments for rent offer classic
            city and bay views in all directions. Each tower offers sophisticated and inviting
            living environments.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622072738/financial_ab3znz.jpg'
    },
    {
    'neighborhood_id': 'financial',
    'user_email': 'user4@test.com',
    'date': datetime.now(),
    'title': '$3,485 / 1br - 652ft2 - Get 6 Weeks Free Rent + $1,000 Bonus Credit On This 1 Bed/1 Bath!f',
    'desc': """Luxury apartments for rent in downtown San Francisco designed for the ultimate in excellence
            and comfort in the Bay area. Each apartment has a unique layout and a view unlike any other,
            including vistas of the North Bay, Financial District, Bay Bridge, Ferry Tower and The Embarcadero.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622143985/financial_dgc0ij.jpg'
    },
    {
    'neighborhood_id': 'haight',
    'user_email': 'user5@test.com',
    'date': datetime.now(),
    'title': '$3,295 / 1br - 910ft2 - Amazing Renovated Art Deco Haight 1BR for Rent!',
    'desc': """You have just stumbled upon one of the nicest 1 bedroom apartment in San Francisco.
            The building is also unique in that we as are not only owners who rent out the building we
            also have lived in the building, so there is a lot of large and small touches we added
            over the years as this is a unit/building that has enjoyed the pride of ownership,
            not just some cheap landlord trying to squeeze every last dollar out of the rental.
            You have to see it to believe it and it is the type of thing your friends will be jealous
            of when they come over to visit you.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622072972/haight_ak0wyc.jpg'
    },
    {
    'neighborhood_id': 'haight',
    'user_email': 'user6@test.com',
    'date': datetime.now(),
    'title': '$2,695 / 1br - 602ft2 - *SPACIOUS 1 BR *Hwd *Granite *DW *Bay Windows *Lndy *Cole St',
    'desc': """LOVELY APT on 2nd floor in 16-Unit 3-Story Building. Spacious Living Room + One Bedroom.
                Bay Windows; Hardwood Floors; Bathroom features ceramic tile; shower over tub """,
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622144075/haight_qxabyb.jpg'
    },
    {
    'neighborhood_id': 'richmond',
    'user_email': 'user7@test.com',
    'date': datetime.now(),
    'title': '$2,450 / 1br - 650ft2 - LargeJunior 1BR! Top Floor! Skylights! Very Sunny! Quiet!',
    'desc': """This very large, bright and sunny junior one bedroom apartment is available now.
                New hardwood floors throughout. New window coverings. New appliances.
                The building is newly remodeled and everything is in fabulous condition.
                The main entrance to the building is open and bright with large glass panels and a glass door.
                The entire building is safe and secure with a Medeco key system.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622073082/richmond_dbx9hp.jpg'
    },
    {
    'neighborhood_id': 'richmond',
    'user_email': 'user8@test.com',
    'date': datetime.now(),
    'title': '$2,800 / 1br - 800ft2 - Spacious Unit Facing Golden Gate Park',
    'desc': """This is a large, newly remodeled unit with about 800 sq. ft.
            The unit has great light, hardwood floors throughout, large bay windows and looks on to
            Golden Gate Park. The unit has a brand new kitchen with lots of storage and
            stainless-steel appliances & granite counters. Eat-in kitchen with great space.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622144455/richmond_jebztv.jpg'
    },
    {
    'neighborhood_id': 'japantown',
    'user_email': 'user9@test.com',
    'date': datetime.now(),
    'title': '$3,495 / 3br - 1275ft2 - Japantown Shopping/3BD 1BA/Fillmore/Shared Yard/1685 Sutter St.',
    'desc': """Period Details Prevail in this High Ceiling 3 BR x 1 Bath of 2 Unit Building
            at Laguna & Sutter. 1275 Square Feet with Large LR and Bedrooms in Back for Quiet
            Enjoyment. Small Shared Yard.No utilities Included in Rent. Street Parking. Easy Walk
            to Upscale Fillmore Street Retail & Shopping Along with Fillmore Jazz District. Nearby
            Grocery Stores Include: Safeway. Super Mira. Mollie Stones. Put Some Zen in Your Den +
            Discover This Tranquil Oasis.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622073391/japantown_mnp81f.jpg'
    },
    {
    'neighborhood_id': 'japantown',
    'user_email': 'user10@test.com',
    'date': datetime.now(),
    'title': '$2,350 / 1br - Lower Pacific Heights/Japantown w/private patio',
    'desc': """This is a Lower Pacific Heights/Japantown one bedroom one bath apartment on the
            3rd floor of a 4 story elevator building. It is located on the corner of Sutter and
            jWebster St. and close to many MUNI lines and Fillmore Street shops and restaurants.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622144645/japantown_esq9e3.jpg'
    },
    {
    'neighborhood_id': 'nob',
    'user_email': 'user11@test.com',
    'date': datetime.now(),
    'title': '$3,350 / 1br - 700ft2 - PRIVATE YARD! Modern, Newly remodeled',
    'desc': """This large one bedroom is a brand new construction with modern design combined with
            a large private yard. The unit is truly high-end in every respect with tall 9 feet
            ceilings and beautiful private backyard. Nice view of the city including the new
            SalesForce tower. The apartment was completely remodeled with the latest and most
            modern appliances and tastefully decorated and furnished with the best quality of
            construction materials. In the heart of San Francisco and prestigious Nob Hill
            neighborhood, one block from Grace Cathedral, Huntington Park, and Cable Car. This
            newly remodeled unit is modern but it is inside a beautiful Victorian apartment building.
            The apartment has hardwood floor, a remodeled kitchen, and marble tiled shower with
            excellent water pressure. The setting of this unit is very cozy with lots of light.
            New Double pane windows combined with away from street, makes it very quiet!""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622073645/nob_rz2g2h.jpg'
    },
    {
    'neighborhood_id': 'nob',
    'user_email': 'user12@test.com',
    'date': datetime.now(),
    'title': '$2,295 / 1br - Furnished 1 BR on Nob Hill',
    'desc': """This is very stylish Victorian building within walking distance to Union Square,
                North Beach, Chinatown, Fisherman's Wharf. Located on top of Nob Hill,
                one block away from Grace Cathedral, 3 blocks from vibrant Polk street filled
                with funky coffee shops, bars and restaurants. Perfect for young professional or
                person in transition. I am looking to sublet my place to a single person that will
                keep it clean and organized. The building has strict pet policy, so sorry for our
                loved ones.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622144814/nob_jtox6v.jpg'
    },
    {
    'neighborhood_id': 'marina',
    'user_email': 'user13@test.com',
    'date': datetime.now(),
    'title': '$6,495 - 2 bed/ 2 bath with 3rd Room/Office - 1750 sq ft',
    'desc': """Full-floor flat (unfurnished) with direct entry, in private 3-unit building.
            Modern remodel with high-end appliances and all the charming quintessential San Francisco
            period-details like crown molding, hardwood floors, and a wood burning fireplace.
            No hiding the square footage...it’s 1750 sq ft with 2 bedrooms, 2 full bathrooms, plus a
            3rd bedroom-sized room for an office, den, or at-home gym.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622070815/marina_housing_2_tpk79b.jpg'
    },
    {
    'neighborhood_id': 'marina',
    'user_email': 'user14@test.com',
    'date': datetime.now(),
    'title': '$2,550 / 1br - 700ft2 - Boutique Building. Bright W/ dedicated parking spot',
    'desc': """This beautiful and bright 1 bedroom/1 bath unit in a boutique seven (7) unit apartment
                building that experiences low turnover. It features a spacious, north-facing living
                room with a large sliding glass door. The living room opens to the kitchen equipped
                with a dishwasher, garbage disposal, and electric range. A full bath is just off the
                bedroom. The apartment features two tone paint, recessed lights, and picture molding.
                All windows are dual pane to mitigate outside noise and maintain ambient temperature
                in the unit. There are two hallway closets with built in shelves, a hall closet off
                the bathroom, and a large closet in the master bedroom-- LOTS of storage!""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622070969/marina_housing_3_jyyjwk.jpg'
    },
    {
    'neighborhood_id': 'marina',
    'user_email': 'user15@test.com',
    'date': datetime.now(),
    'title': '$3,250 / 1br - One Bedroom with Parking Across the Street from Fort Mason',
    'desc': """1225 Bay St #6: 1 Large Bedroom with Walk In Closet, 1 Bathroom with Stall Shower, Living Room,
            Kitchen with Refrigerator, Gas Oven/Stove. Beautiful French Doors separating Living
            and Bedroom with tons of storage. Parking space included in secure garage. Available now.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622070655/marina_housing_s5jwpz.jpg'
    },
    {
    'neighborhood_id': 'mission',
    'user_email': 'user16@test.com',
    'date': datetime.now(),
    'title': '$3,395 / 1br - Mission Dolores Park/3605 20th&Valencia/Bart/Muni/W/D in unit',
    'desc': """Awesome apartment on the 5th floor with a huge balcony, rooftop, and amazing views!
                Modern appliances including a huge fridge, dishwasher, and garbage disposal.
                Concrete ceilings and walls so you don't hear your neighbors. Each floor has its own
                laundry so you're only sharing it with other units on the same floor. Building is
                equipped with fiber internet — super fast speeds via Webpass.
                Gorgeous views facing Bernal and gets tons of sunlight ALL DAY.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622071420/mission_housing_lt5f0x.jpg'
    },
    {
    'neighborhood_id': 'mission',
    'user_email': 'user17@test.com',
    'date': datetime.now(),
    'title': '$2,395 / 1br - Remodeled 1 Bed 1 Bath on Valencia Street',
    'desc': """This remodeled 1 bed 1 bath apartment is located at Valencia Street and 26th Street.
            The Mission represents the heart and soul of San Francisco and is a melting pot with taquerias
            and panaderias, pop-up galleries, boutiques, cafes and bars. A few  blocks away lies Dolores
            Park, a favorite neighborhood hangout. Public transportation is great; numerous Muni-light-rail
            and bus lines criss-cross the neighborhoods, and there are two Bart Stations within walking
            distance of this apartment.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622071653/mission_4_bs33gh.jpg'
    },
    {
    'neighborhood_id': 'noe',
    'user_email': 'user18@test.com',
    'date': datetime.now(),
    'title': '$2,495 / 1br - 530ft2 - Immaculate Apt with in-unit W/D, Great Location',
    'desc': """An excellent opportunity to rent this Dolores Street one-bedroom apartment with
                remodeled kitchen including dishwasher, gas stove/oven, and all in one washer/dryer.
                Good size bedroom with adequate closet space, calming recessed lighting and
                hardwood floors and a peaceful shared patio and all Just within a leisurely
                block walk to the MUNI J line at Church Street with a range of location advantages
                include cafes, restaurants, and the Noe Valley Whole Foods market. This lovely
                unit is available now, street parking, small pet negotiable, A smart option for
                the savvy renter!""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622144997/noe_djxkoj.jpg'
    },
    {
    'neighborhood_id': 'noe',
    'user_email': 'user19@test.com',
    'date': datetime.now(),
    'title': '$2,500 / 1br - Roof Deck! 1BR/1BA Condo NoeValley W/D',
    'desc': """This is a 1BR/1BA. The kitchen is fully equipped with a gas range and plenty of
                counterspace for all the kitchen gadgets. The living room can encompass a couch
                areas, workstations, dining table, etc. All along multiple sets of windows that
                add lots of natural light. There is a stack washer and dryer in -unit. Common areas
                include a large full roof deck with views of Bernal Heights, Downtown, Noe Valley,
                and the Mission. Easily accessible to both 101 and 280 freeways. Security Deposit
                is 1.5x month rent. Cats Okay, No Dogs.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622073992/noe_egvqdw.jpg'
    },
    {
    'neighborhood_id': 'north',
    'user_email': 'user20@test.com',
    'date': datetime.now(),
    'title': '$3,400 / 1br - Light Filled Garden Apt.-Best Location in North Beach',
    'desc': """A gorgeous sun-drenched garden apartment nestled far from the street within sight of
            the famous crooked Lombard street. The apartment is quiet, opens onto a large brick
            courtyard planted in box hedges and olive trees, plus a semi-private brick backyard
            to sun and take your coffee. The apartment has a very large remodeled kitchen with all
            the amenities, gas range, refrigerator, microwave and dishwasher; perfect for the
            aspiring chef.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622074165/north_scu1it.jpg'
    },
    {
    'neighborhood_id': 'north',
    'user_email': 'user21@test.com',
    'date': datetime.now(),
    'title': '$1,699 Beautiful Furnished Studio! Self Guided Tour Available',
    'desc': """Located at the edge of North Beach on Telegraph Hill, near Chinatown -
                two of San Francisco's most famous districts. Also nearby is Washington Square
                Park. San Francisco's Telegraph Hill district provides excellent Italian dining
                options and quaint cafes. Living in these dream San Francisco apartments also
                places you near the Financial District and the SF downtown area""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622145683/north_urzwb6.jpg'
    },
    {
    'neighborhood_id': 'pac',
    'user_email': 'user22@test.com',
    'date': datetime.now(),
    'title': '$2,595 / 1br - 1BR/1BA in Pacific Heights; Pets OK',
    'desc': """2250 Buchanan Street San Francisco, CA 94121.
            Newly renovated kitchen with quartz counter tops, white cabinets, refrigerator and electric range.
            Large living space; bright and spacious. Gray plank flooring throughout with great natural
            sunlight and a large closet.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622074315/pacific_h19fta.jpg'
    },
    {
    'neighborhood_id': 'pac',
    'user_email': 'user23@test.com',
    'date': datetime.now(),
    'title': '$3,306 / 1br - Renovated One Bedroom - Fully Furnished',
    'desc': """Located in Pacific Heights; one of San Francisco's most prestigious neighborhoods.
            You will be moments away from shops and boutiques, restaurants, and entertainment on
            Fillmore and Union Street. Close to Golden Gate Bridge and Marina District; convenient
            to public transportation and freeways. Apartment is furnished with queen size bed,
            linens, night stands, TV with stand, dining table and chairs, sofa, chair and ottoman,
            side tables and more""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622145805/pac_almxky.jpg'
    },
    {
    'neighborhood_id': 'potrero',
    'user_email': 'user24@test.com',
    'date': datetime.now(),
    'title': '$3,100 / 1br - 1334ft2 - Top floor, 20-foot ceiling, Floor-to-ceiling windows, Extra wide floor',
    'desc': """Showplace Square is a standout boutique building clad in corrugated steel, located at the base
            of Potrero Hill. Loft A8 located in the original 370 De Haro building is offered for the first
            time since its inaugural sale in 1999. (301 Rhode Island is the 2nd phase of Showplace Square.)
            Features: Top floor, 20-foot ceiling, Floor-to-ceiling windows, Extra wide floor plan,
            Lofted bedroom with catwalk, Carrara marble countertops, Exclusive-use 1 car garage parking.
            Enjoy all the amenities of the Design District and Potrero Hill's 18th Street strip including
            Philz Coffee, Market & Rye, Crossfit, Anchor Brewing Company and Jackson Playground; 1 block
            to Whole Foods, 8 minute walk to UCSF, 10 minute walk to CalTrain.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622139936/potrero_sfv2md.jpg'
    },
    {
    'neighborhood_id': 'potrero',
    'user_email': 'user25@test.com',
    'date': datetime.now(),
    'title': '$3,899 / 1br - 760ft2 - Loft, corner unit, top floor, private large patio',
    'desc': """We are excited to offer this spacious loft apartment located in a historic factory.
                Conveniently located close to cafes, coffee shops, grocery stores, parks,
                and various dining experiences.
                Working from home has never been so easy. Window walls of glazing accompanied
                with high ceilings, allow natural light to pour into the space. Privacy is
                accomplished by the use of modern window shades (included).""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622145922/potrero_mbrqx3.jpg'
    },
    {
    'neighborhood_id': 'presidio',
    'user_email': 'user26@test.com',
    'date': datetime.now(),
    'title': '$3,130 / 1br - 600ft2 - Presidio Landmark - Jr. I Bedroom',
    'desc': """Private, 600 sq. ft., secluded, junior 1-bedroom, Bosch washer and ventless dryer,
                electric appliances, south facing apartment in the lower lobby. The Presidio Landmark,
                sits in the historic and beautiful Presidio. Surrounded by walking and running trails,
                with breathtaking views of Golden Gate Park, UCSF, and Sutro Tower. Our location provides
                a very suburban feel with being moments away, "city conveniences".""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622140177/presidio_fbfnpm.jpg'
    },
    {
    'neighborhood_id': 'russian',
    'user_email': 'user28@test.com',
    'date': datetime.now(),
    'title': '$2,795 / 1br - Beautiful 1 bedroom with French Doors | Eat-in Kitchen - 1304 Lombardruss',
    'desc': """This charming 1 bedroom unit has been freshly painted throughout. Lovely French doors
            separates the spacious bedroom and living room. Both rooms have large closet. The eat-in
            kitchen has wooden cabinet features and tile flooring, black stone counters, 4-burner gas
            range, dishwasher and refrigerator. Full tub in bathroom, with tile flooring. Sorry, no pets.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622140288/russian_le9zd1.jpg'
    },
    {
    'neighborhood_id': 'russian',
    'user_email': 'user29@test.com',
    'date': datetime.now(),
    'title': '$1,990 Top Floor Bright Studio in Convenient Location! Roof Deck and Laundry',
    'desc': """This classic bright newly renovated studio is located on the top floor of the
            building and features beautiful hardwood flooring, huge walk-in closet, large windows,
            new kitchen appliances, refinished clawfoot tub, and has been fully painted. Building
            is safe, clean, well-maintained, seismically retrofitted, and includes the following
            amenities: large laundry facility, secure bike parking, security gate, and a large
            rooftop deck with spectacular views!""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622146231/russian_ays96j.jpg'
    },
    {
    'neighborhood_id': 'soma',
    'user_email': 'user30@test.com',
    'date': datetime.now(),
    'title': '$2,899 / 1br - 650ft2 - Oracle Baseball, Penthouse/Top 1BD-1BR, With Parking, Pool & Hot Tub!',
    'desc': """Quiet semi-furnished one-bedroom/one-bathroom, top, corner-floor, high-ceiling unit,
            (artist-inspired by GGLO) building located in the heart of South Beach-Mission Bay,
            right across the Oracle Park baseball stadium! The building is approximately a block away
            from the SF Caltrain station & Safeway; lots of neighborhood restaurants and bars
            (Lucky Strike Bowling just around the corner!)""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622140400/soma_irbxcz.jpg'
    },
    {
    'neighborhood_id': 'soma',
    'user_email': 'user30@test.com',
    'date': datetime.now(),
    'title': '$1,995 / 1br - 350ft2 - Last Ones Left! Roomy Hybrid Jr. 1bd/1ba',
    'desc': """OME is a new boutique SoMa community, offering modern, well-designed,
            highly efficient apartments. Designed by local David Baker Architects , OME has
            been created for you.  Features laundry onsite, package room, community room, bike room,
            BBQ and roof deck.  Cats and small dogs allowed.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622146810/soma_vimrru.jpg'
    },
    {
    'neighborhood_id': 'sunset',
    'user_email': 'user2@test.com',
    'date': datetime.now(),
    'title': '$2,400 / 1br - 550ft2suns - Bright 1bd~Pretty yard~W/D in Bldg',
    'desc': """Really Pretty Backyard~Perfect for BBQing or Enjoying a Great Book! Washer and
                Dryer in Building. Storage Included. Wonderful Inner Sunset Neighborhood!!
                Walker's Paradise with a 92 Score. Walk to Restaurants and Stores.
                1 block to N-Judah Muni Line. Close Proximity to UCSF, Judah & Irving Streets,
                and 19th Avenue~Easy Access to North & South Bay.
                Golden Gate Park & Ocean Beach are Close Byå""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622140915/sunset_gqg05c.jpg'
    },
    {
    'neighborhood_id': 'sunset',
    'user_email': 'user2@test.com',
    'date': datetime.now(),
    'title': '',
    'desc': """Comfortably furnished 3 rooms apartment (1bdr/1bath.+dining and living rooms)
                with Private Garden. Located near Ocean Beach and the Golden Gate Park
                The bedroom comes with a queen sized bed, chest of drawers. Dining room comes
                with dining set, cupboard, book shelves, desk and sleeper sofa. Living room comes
                with the couch, chaise and ottoman. Between kitchen and dining room is small
                breakfast room. Paradise for bicyclist (bicycle lane along the Ocean Beach and
                in the Golden Gate Park, heaven for fitness minded people (Bring your bicycles
                or rent one).""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622158120/sunset_joccao.jpg'
    },
    {
    'neighborhood_id': 'tenderloin',
    'user_email': 'user4@test.com',
    'date': datetime.now(),
    'title': '$2,295 / 1br - Stunning Hyde Street 1 Bedroom is the Perfect Place to WFH',
    'desc': """The monarch butterfly mural is calling you home to this beautiful building that
            friends will spot from miles away. It’s a quick walk away to the city’s best shopping
            and dining options in Union Square, Market Street, and other hotspots. This vintage
            high rise has the best amenities - hardwood floors, bay windows, in-unit laundry and
            an updated kitchen to make this apartment worthy of staycation status.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622140648/tenderloin_dd79aw.jpg'
    },
    {
    'neighborhood_id': 'tenderloin',
    'user_email': 'user5@test.com',
    'date': datetime.now(),
    'title': '$1,895 / 500ft2 - Great View, large bright, new kit, new bath, garage avail',
    'desc': """Great view! Large studio. Brand new kitchen and bath. Great closet space,
            1 walk-in and 1 other. Quiet unit. Water and garbage inc. Washer and dryer in basement.
            Garage parking available for $200 a month. Cat OK. No smoking. 1 year lease and good
            credit required. Unit is about 500 sq feet.""",
    'contact_info': 'sana.other@gmail.com',
    'image_url': 'https://res.cloudinary.com/sana3339/image/upload/v1622146625/tenderloin_q64rrv.jpg'
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
