const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
const useHistory = ReactRouterDOM.useHistory;
const useLocation = ReactRouterDOM.useLocation;

const Navbar = ReactBootstrap.Navbar;
const Nav = ReactBootstrap.Nav;
const Form = ReactBootstrap.Form;
const FormControl = ReactBootstrap.FormControl;
const Button = ReactBootstrap.Button;
const Carousel = ReactBootstrap.Carousel;
const Container = ReactBootstrap.Container;
const Row = ReactBootstrap.Row;
const Col = ReactBootstrap.Col;
const Card = ReactBootstrap.Card;
const Alert = ReactBootstrap.Alert;
const ToggleButtonGroup = ReactBootstrap.ToggleButtonGroup;
const ButtonGroup = ReactBootstrap.ButtonGroup;
const ToggleButton = ReactBootstrap.ToggleButton;
const CardDeck = ReactBootstrap.CardDeck;
const Table = ReactBootstrap.Table;
const Jumbotron = ReactBootstrap.Jumbotron;

function Homepage() {
  let history = useHistory();
  
  const redirectToMapPage = () => {
    history.push('/map');
  }

  return (
    <React.Fragment>
      <Container>
        <div className="block-center">
          <h1 id="Frisco">Frisco</h1>
          <h4 id="subheading-Frisco">Which San Francisco neighborhood should you live in?</h4>
          <Button id="button-Frisco" type="button" className="btn btn-warning btn-sm" onClick={redirectToMapPage}> Enter </Button>
        </div>
      </Container>
    </React.Fragment>
  );   
}

function MapView(){
  const options = {
    zoom:12.2,
    center:{lat:37.7822, lng:-122.4342}
    };
  const ref = React.useRef();
  const [map, setMap] = React.useState("");
  const [markerList, setMarkerList] = React.useState("");
  let history = useHistory();

  React.useEffect(() => {
    fetch("/api/neighborhood-details.json")
    .then(response => response.json())
    .then((data) => {

      const markerList = [];

      for (const neighborhood of data) {
        const markerDetails = {
          coords: {lat:neighborhood.latitude, lng:neighborhood.longitude},
          windowContent: neighborhood.short_desc,
        };
        markerList.push(markerDetails);
       }
       setMarkerList(markerList)
      })
  }, []);

  React.useEffect(() => {
    const onLoad = () => {
      const gMap = new window.google.maps.Map(ref.current, options);
      setMap(gMap);

      const addMarkers = () => 
        fetch("/api/neighborhood-details.json")
        .then(response => response.json())
        .then((data) => {

        const markerList = [];


        for (const neighborhood of data) {
          const markerDetails = {
            coords: {lat:neighborhood.latitude, lng:neighborhood.longitude},
            windowContent: neighborhood.short_desc,
            neighborhood_id: neighborhood.neighborhood_id
          };
          markerList.push(markerDetails);
         }
         setMarkerList(markerList);
          
          for (const aMarker of markerList) {

          if (aMarker.neighborhood_id === 'marina' || aMarker.neighborhood_id === 'north' || aMarker.neighborhood_id === 'russian' ||
          aMarker.neighborhood_id === 'presidio' || aMarker.neighborhood_id === 'pac' || aMarker.neighborhood_id === 'nob' ||
          aMarker.neighborhood_id === 'financial' ) {
          const infoWindow = new google.maps.InfoWindow({
            content: aMarker.windowContent,
            disableAutoPan: true,
            pixelOffset: new google.maps.Size(0,215)
            });
          
          const marker = new window.google.maps.Marker({
            position:aMarker.coords,
            animation: google.maps.Animation.DROP,
            map:gMap
            });

            marker.addListener("click", () => {
              history.push(`/neighborhood/${aMarker.neighborhood_id}`);
            })

            marker.addListener("mouseover", () => {
              infoWindow.open(gMap,marker)
              });
            
            marker.addListener("mouseout", () => {
              infoWindow.close(gMap,marker)
            });
        } else {
          const infoWindow = new google.maps.InfoWindow({
            content: aMarker.windowContent,
            disableAutoPan: true,
            });
          
          const marker = new window.google.maps.Marker({
            position:aMarker.coords,
            animation: google.maps.Animation.DROP,
            map:gMap
            });

            marker.addListener("click", () => {
              history.push(`/neighborhood/${aMarker.neighborhood_id}`);
              console.log(aMarker.neighborhood_id);
            })

            marker.addListener("mouseover", () => {
              infoWindow.open(gMap,marker)
              });
            
            marker.addListener("mouseout", () => {
              infoWindow.close(gMap,marker)
            });
          }
         }
       })
      addMarkers();
    }

      const script = document.createElement("script");
      script.type = "text/javascript";
      if (script.readyState) {
        script.onreadystatechange = function() {
          if (script.readyState === "loaded" || script.readyState === "complete") {
            script.onreadystatechange = null;
            onLoad();
          }
        };
      } else {
        script.onload = () => onLoad();
      }

      script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyABrkGgdfKYcuUmSE_VZ9cgThiFKHkfYiQ";

      document.getElementsByTagName("head")[0].appendChild(script);
      console.log("Script is adding");
    }, []);

    return (
      <React.Fragment>
        <Container>
          <h4 id="map-heading">Click on a marker to learn more about the neighborhood</h4>
          <div id="map"
          style={{ height: "500px", width:"70%" }}
          {...{ref}}>
          </div>
        </Container>
      </React.Fragment>
    );
  }

  //<Link to={`/neighborhood/${neighborhood_id}`}> Neighborhood Details </Link>


function MapHousing() {
  const options = {
    zoom:12.2,
    center:{lat:37.7822, lng:-122.4342}
    };
  const ref = React.useRef();
  const [map, setMap] = React.useState("");
  const [markerList, setMarkerList] = React.useState("");
  let history = useHistory();

  React.useEffect(() => {
    fetch("/api/neighborhood-details.json")
    .then(response => response.json())
    .then((data) => {

      const markerList = [];

      for (const neighborhood of data) {
        const markerDetails = {
          coords: {lat:neighborhood.latitude, lng:neighborhood.longitude},
          windowContent: neighborhood.name,
        };
        markerList.push(markerDetails);
       }
       setMarkerList(markerList)
      })
  }, []);

  React.useEffect(() => {
    const onLoad = () => {
      const gMap = new window.google.maps.Map(ref.current, options);
      setMap(gMap);

      const addMarkers = () => 
        fetch("/api/neighborhood-details.json")
        .then(response => response.json())
        .then((data) => {

        const markerList = [];

        for (const neighborhood of data) {
          const markerDetails = {
            coords: {lat:neighborhood.latitude, lng:neighborhood.longitude},
            windowContent: neighborhood.name,
            neighborhood_id: neighborhood.neighborhood_id
          };
          markerList.push(markerDetails);
         }
         setMarkerList(markerList);
          
          for (const aMarker of markerList) {

          const infoWindow = new google.maps.InfoWindow({
            content: aMarker.windowContent
            });
          
          const marker = new window.google.maps.Marker({
            position:aMarker.coords,
            animation: google.maps.Animation.DROP,
            map:gMap
            });

            marker.addListener("click", () => {
              history.push(`/post/${aMarker.neighborhood_id}`);
            })
            marker.addListener("mouseover", () => {
              infoWindow.open(gMap,marker)
              });
            marker.addListener("mouseout", () => {
              infoWindow.close(gMap,marker)
            });
        }
      })
     addMarkers();
    }

      const script = document.createElement("script");
      script.type = "text/javascript";
      if (script.readyState) {
        script.onreadystatechange = function() {
          if (script.readyState === "loaded" || script.readyState === "complete") {
            script.onreadystatechange = null;
     //       onLoad();
          }
        };
      } else {
        script.onload = () => onLoad();
      }

      script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyABrkGgdfKYcuUmSE_VZ9cgThiFKHkfYiQ";

      document.getElementsByTagName("head")[0].appendChild(script);
      console.log("Script is adding");
    }, []);

  return (
    <React.Fragment>
      <Container>
        <h4 id="map-heading">Click on a marker closest to the housing you'd like to post</h4>
            <div id="map"
            style={{ height: "500px", width:"70%" }}
            {...{ref}}>
          </div>
    </Container>
  </React.Fragment>
 );
}

function Neighborhood() {
  const [name, setName] = React.useState("");
  const [desc, setDesc] = React.useState('');
  const [medianHomePrice, setMedianHomePrice] = React.useState();
  const [medianRental, setMedianRental] = React.useState();
  const [sqFtPrice, setSqFtPrice] = React.useState();
  const [walkScore, setWalkScore] = React.useState();
  const [transitScore, setTransitScore] = React.useState();
  let {neighborhood_id} = ReactRouterDOM.useParams();
  let history = useHistory();


  React.useEffect(() => {
    fetch(`/api/neighborhood/${neighborhood_id}`)
    .then(response => response.json())
    .then((data) => {
        setName(data.name);
        setDesc(data.long_desc);
        setMedianHomePrice(data.median_home_price);
        setMedianRental(data.median_rental);
        setSqFtPrice(data.sq_ft_price);
        setTransitScore(data.transit_score);
        setWalkScore(data.walk_score);
    });
  }, [])

  const redirectToFindHousing = () => {
    history.push(`/housing/${neighborhood_id}`);
  }
  //<p><Link to={`/housing/${neighborhood_id}`}> Find {name} housing </Link></p>

  const redirectToPostHousing = () => {
    history.push(`/post/${neighborhood_id}`)
  }

  const redirectToMap = () => {
    history.push('/map')
  }
  
  //<Link to={`/post/${neighborhood_id}`}> Post {name} housing </Link>

  return(
    <React.Fragment>
      
        <Container>
          <Row>
              <Col s={12} md={5}>
                  <h3 className="neighborhood-header">{name}</h3>
                  <p className="neighborhood-desc">{desc} </p>

                  <Table striped bordered hover size="sm">
                    <tbody>
                      <tr>
                        <td>Median Rental Price:</td>
                        <td>${medianRental}</td>
                      </tr>
                      <tr>
                        <td>Median Home Price:</td>
                        <td>${medianHomePrice}</td>
                      </tr>
                      <tr>
                        <td>Sq Ft Price:</td>
                        <td>${sqFtPrice}</td>
                      </tr>
                      <tr>
                        <td>Walk Score:</td>
                        <td>{walkScore}</td>
                      </tr>
                      <tr>
                        <td>Transit Score:</td>
                        <td>{transitScore}</td>
                      </tr>
                    </tbody>
                  </Table>
                </Col>
              <Col s={12} md={7
              }> 
                <Images neighborhood_id={neighborhood_id} />
                <Row>
                  <Col sm={4}>
                    <Button className="restaurant-button" variant="primary" onClick={redirectToFindHousing}>Find Housing</Button>
                  </Col>
                  <Col sm={4}>
                    <Button className="restaurant-button" variant="primary" onClick={redirectToPostHousing}>Post Housing</Button>
                  </Col>
                  <Col sm={4}>
                    <Button className="restaurant-button" variant="primary" onClick={redirectToMap}>Neighborhoods </Button>
                  </Col>
                </Row>
              </Col>
            </Row>
         <Row>  
              <h5>{name} Restaurants</h5>  
          </Row>
          <Row>
            <div className="card-deck">
                <Restaurants neighborhood_id={neighborhood_id} />
            </div>
        </Row> 
    </Container>
          
    </React.Fragment>
  );
}

function Images(props) {

  const [imageList, setImageList] = React.useState(["loading..."]);

  React.useEffect(() => {
    fetch(`/api/images/${props.neighborhood_id}`)
    .then(response => response.json())
    .then((data) => {
        const imageFetchList = []

        for (const image of data) {
          imageFetchList.push(
            <ImageListItem
              key={image.image_id}
              image_name={image.image_name}
              neighborhood_id={image.neighborhood_id}
            />
          );
        }
        setImageList(imageFetchList);
    })
  }, [])


  return(
    <React.Fragment>
        {imageList}
    </React.Fragment>
  );
}

function ImageListItem(props) {
  
  const image_url = `/static/img/${props.image_name}`

  return (
   
    <img className="neighborhood-image" src={image_url} />
    
  );
}

function RestaurantListItem(props) {

  return(
    <Col sm={12} md={3}>
      <div className="restaurant-card">
          <div className="card">
          <img
            src={props.photo}
            className="card-img-top"
          />
          <div className="card-body">
          
            <p className="restaurant-text">
              <b>{props.name}</b><br></br>
              {props.address}<br></br>
              Rating: {props.rating}<br></br> 
              <a href={props.website} target="blank">Website</a>
            </p>
           </div>
       </div>
    </div>
  </Col>
  );
}

function Restaurants(props) {

  const [restaurantList, setRestaurantList] = React.useState(["...loading..."]);

  React.useEffect(() => {
    fetch(`/api/restaurants/${props.neighborhood_id}`)
    .then(response => response.json())
    .then((data) => {
        const restaurantFetchList = []

        for (const restaurant of data) {
          restaurantFetchList.push(
            <RestaurantListItem
              key={restaurant.place_id}
              name={restaurant.name}
              address={restaurant.address}
              rating={restaurant.rating}
              website={restaurant.website}
              photo={restaurant.photo}
            />
          );
        }
        setRestaurantList(restaurantFetchList);
    })
  }, [])

  return(
    <React.Fragment>
        {restaurantList}
    </React.Fragment>
  );
}

function FindHousing(props) {

  let {neighborhood_id} = ReactRouterDOM.useParams();
  const [postList, setPostList] = React.useState(["loading..."]);
  const [neighborhoodName, setNeighborhoodName] = React.useState(["loading..."]);

  

     //Get neighborhood name based on neighborhood_id
  React.useEffect(() => {
    fetch(`/api/neighborhood/${neighborhood_id}`)
      .then(response => response.json())
      .then((data) => {
        setNeighborhoodName(data.name);
      })
    }, [])
  

  React.useEffect(() => {
    fetch(`/api/housing/${neighborhood_id}`)
      .then(response => response.json())
      .then((data) => {
        
        const postFetchList = []

        for (const posting of data) {

          postFetchList.push(
            <PostListItem
              key={posting.posting_id}
              posting_id={posting.posting_id}
              date={posting.date}
              title={posting.title}
              desc={posting.desc}
              contact_info={posting.contact_info}
              image_url={posting.image_url}
            />
           );
          }
        setPostList(postFetchList);
      })
  }, [])

    
  return(
    <React.Fragment>
      <Container>
        <h3>{neighborhoodName} Housing</h3>
        {postList}
      </Container>
    </React.Fragment>
  );
}

function PostHousing() {

  let {neighborhood_id} = ReactRouterDOM.useParams();
  const email = localStorage.getItem('logged_in_user');

  const [neighborhoodName, setNeighborhoodName] = React.useState(["loading..."]);
  const[title, setTitle] = React.useState('');
  const[desc, setDesc] = React.useState('');
  const[contact_info, setContact_info] = React.useState('');
  const [url, setUrl] = React.useState('');
  const [image, setImage] = React.useState('');
  let history = useHistory();

  //Get neighborhood name based on neighborhood_id
  React.useEffect(() => {
  fetch(`/api/neighborhood/${neighborhood_id}`)
    .then(response => response.json())
    .then((data) => {
      setNeighborhoodName(data.name);
    })
  }, [])

  const createNewPost = () => {
    const post = {
      'neighborhood_id': neighborhood_id,
      'email': email,
      'title': title,
      'desc': desc,
      'contact_info': contact_info,
      'image_url': url,
      }
    fetch('/api/create-posting', {
      method: 'POST',
      body: JSON.stringify(post),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data === "Success") {
        alert('Post added')
      }
    });
    history.push('/profile');
  }

  const uploadImage = () => {
    const data = new FormData()
    data.append("file", image)

    data.append("upload_preset", "Frisco")
    data.append("cloud_name", "sana3339")
    fetch("https://api.cloudinary.com/v1_1/sana3339/image/upload", {
      method:"POST",
      body: data
    })
    .then(resp => resp.json())
    .then(data => {
      setUrl(data.url);
    })
    .catch(err => console.log(err))
  }
  
  return (
    <React.Fragment>
        <Jumbotron className="create-account-background">
          <Row className="justify-content-center">
            <Col sm={12} md={8}>
            <Card className="post-housing-form bg-light">
              <p className="posting-form-title">Post {neighborhoodName} Housing</p>
              
                <p className="posting-form-header">Title:</p>
                <input
                  className="posting-form-input"
                  type="text"
                  onChange={(event) => setTitle(event.target.value)}
                  value={title}
                  />
                
                <p className="posting-form-header">Description:</p>
                  <textarea
                    className="posting-textarea-input"
                    onChange={(event) => setDesc(event.target.value)}
                    value={desc}
                  />
                
                  <p className="posting-form-header">Email:</p>
                    <input
                      className="posting-form-input"
                      type="text"
                      onChange={(event) => setContact_info(event.target.value)}
                      value={contact_info}
                    />
                
                  <div className="posting-file-input">
                    <input type="file" onChange= {(event)=> setImage(event.target.files[0])}></input>
                      <button onClick={uploadImage}>Upload</button>
                    </div>
                    <div>
                        <img className="posting-image" src={url} />
                    </div>
                <Button className="posting-form-button" onClick={createNewPost}> Add Posting </Button>
              
            </Card>
          </Col>
        </Row>
      </Jumbotron>
    </React.Fragment>
  );
}


function PostListItem(props){

  let history = useHistory();

  console.log('posting id is:', props.posting_id)

  const redirectToContact = () => {
      history.push(`/send-email/${props.posting_id}`);
  }

  return(
    <React.Fragment>
        <Card.Title>{props.date}{props.title}</Card.Title>
        <p></p>
        <p></p>
        <p>{props.desc}</p>
        <p>{props.contact_info}</p>   
        <img src={props.image_url} />
        <button onClick={redirectToContact}>Contact Seller</button>
    </React.Fragment>
  );
}

function ContactSellerForm() {

  const [fromName, setFromName] = React.useState('');
  const [sellerEmail, setSellerEmail] = React.useState('');
  const [replyToEmail, setReplyToEmail] = React.useState('');
  const [message, setMessage] = React.useState('');

  let {posting_id} = ReactRouterDOM.useParams();
  let history = useHistory();

  React.useEffect(() => {
      fetch(`/api/get-seller-email/${posting_id}`)
      .then(response => response.json())
      .then((data) => {
          setSellerEmail(data)
      })
  }, [])

  console.log("seller email is:", sellerEmail); 

  const redirectBack = () => {
      history.goBack();
  }

  function sendEmail(e) {
      e.preventDefault();

      window.emailjs.sendForm('default_service', 'template_43ponc9', e.target, 'user_uTFw7bspn4zVAkmNegIxE')
          .then((result) => {
              console.log(result.text);
              alert("Your message has been sent")
              setFromName('');
              setSellerEmail('');
              setReplyToEmail('');
              setMessage('');
          }, (error) => {
              console.log(error.text);
          });
      }

      
  return (
      <React.Fragment>
      <form id="contact-form" onSubmit={sendEmail}>
          <input type="hidden" name="seller_email" 
              onChange={(event) => setSellerEmail(event.target.value)}
              value={sellerEmail}/>
          <label>Your Name</label>
          <input type="text" name="from_name" 
              onChange={(event) => setFromName(event.target.value)}
              value={fromName}/>
          <label>Your Email</label>
          <input type="email" name="reply_to" 
              onChange={(event) => setReplyToEmail(event.target.value)}
              value={replyToEmail}/>
          <label>Your Message</label>
          <textarea name="message"
              onChange={(event) => setMessage(event.target.value)}
              value={message}/>
          <input type="submit" value="Send" />
      </form>
      <button onClick={redirectBack}>Back</button>
      </React.Fragment>
      );
  }


//This is a copy of the PostListItem component above but it includes delete functionality.
//These are different components bc a post should only be able to be deleted by the user who created it
//from their user profile page
function PostListItemWithDelete(props){

  return(
    <React.Fragment>
        <p>{props.date} &nbsp; <u>{props.title}</u></p>
        <p>{props.desc}</p>  
        <img className="posting-image" src={props.image_url} />
        <DeletePosting posting_id={props.posting_id}/> 
    </React.Fragment>
  );
}

function DeletePosting(props) {  

  console.log("In DeletePosting, posting_id is:", props.posting_id)

  const deletePosting = () => {
    fetch('/api/delete-posting', {
      method: 'POST',
      body: JSON.stringify(props.posting_id)
    })
    .then(response => response.json())
    .then(data => {
      if (data) {
        alert("Posting Deleted");
      }
    });
   }

  return (
    <form action="/profile">
      <button type="submit" onClick={deletePosting}>Delete</button>
    </form>
  );
}

function CreateUser() {

  let history = useHistory();

  const[email, setEmail] = React.useState('');
  const[password, setPassword] = React.useState('');

  const createNewUser = () => {
    const user = {'email': email, 'password': password}
    fetch('/api/create-user', {
      method: 'POST',
      body: JSON.stringify(user),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.message === "Error - user already exists. Please log in.") {
        alert(data.message);
        history.push('/login');
      } else {
        alert(data.message);
        localStorage.setItem('logged_in_user', data.email);
        history.push('/profile');
      }
    })
  }

  return(
    <React.Fragment>
      
        <Jumbotron className="create-account-background">
          <Row className="justify-content-center">
            <Card className="user-form">
              <Card.Body>
              <Card.Title className="text-center">Create Account</Card.Title>
              <Form>

              <Form.Group controlId="formBasicEmail">
                <Form.Label>Email:</Form.Label>
                <Form.Control type="email"
                  onChange={(event) => setEmail(event.target.value)}
                  value={email}/>
              </Form.Group>

              <Form.Group controlId="formBasicPassword">
                <Form.Label>Password:</Form.Label>
                <Form.Control type="password"
                  onChange={(event) => setPassword(event.target.value)}
                  value={password}
                  />
              </Form.Group>
              
              <Button className="form-button" type="button" onClick={createNewUser} block>Register</Button>
             </Form>
            </Card.Body>
          </Card>
         </Row>
         </Jumbotron>
    
    </React.Fragment>
  );
}

function PrivateRoute({ children, ...rest }) {
  return (
    <Route {...rest} render={({ location }) => {
      return localStorage.getItem('logged_in_user') !== null
      ? children
      : <Redirect to={{
        pathname: "/login",
        state: { from: location }
      }} />
    }} />
  )
}

function Login(props) {

  console.log(localStorage.getItem('logged_in_user'));
  if (localStorage.getItem('logged_in_user') !== null) {
  }

  let history = useHistory();
  const { state } = ReactRouterDOM.useLocation();

  const [redirectToReferrer, setredirectToReferrer] = React.useState(false)

  const [email,setEmail] = React.useState();
  const [password,setPassword] = React.useState();

  const loginUser = () => {
    const user = {'email': email, 'password': password}
    fetch("/api/handle-login", {
      method: 'POST',
      body: JSON.stringify(user),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.message === "No account exists for that email. Please create an account.") {
        alert(data.message);
        history.push('/create-user');
      } else if (data.message === "Incorrect password.") {
          alert(data.message);
          history.push('/login')
      } else if (data.message === "You are now logged in.") {
          alert(data.message);
          localStorage.setItem('logged_in_user', data.email);
         // history.push('/profile')
         setredirectToReferrer(true);
        }
      }
    ) 
  }

  if (redirectToReferrer === true) {
    if (state) {
      return <Redirect to={state.from}/>
    } else {
      return <Redirect to="/"/>
   }
  }
  

  return (
    <React.Fragment>
      <Jumbotron className="login-background">
        <Row className="justify-content-center">
          <Card className="user-form">
            <Card.Body>
              <Card.Title className="text-center">Login</Card.Title>
                <Form>
                  <Form.Text className="form-text">You must be logged in to post housing.</Form.Text>
                  
              
                <Form.Group controlId="formBasicEmail">
                <Form.Label>Email:</Form.Label>
                  <Form.Control
                    type="text"
                    onChange={(event) => setEmail(event.target.value)}
                    value={email || ''}
                    />
                  </Form.Group>

                  <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password:</Form.Label>
                      <Form.Control
                        type="password"
                        onChange={(event) => setPassword(event.target.value)}
                        value={password || ''}
                        />
                    </Form.Group>
                    <Button className="form-button" type="button" onClick={loginUser} block> Login </Button> 
                
                    <Form.Text className="muted text-center"> Not registered? &nbsp;
                        <Link to="/create-user">Create an account</Link>
                  </Form.Text>
                </Form>
              </Card.Body>
          </Card>
        </Row>
      </Jumbotron>
    </React.Fragment>
  );
}

function UserProfile() {

  const [postList, setPostList] = React.useState(["loading..."]);

  const email = localStorage.getItem('logged_in_user')
  const email_list = email.split("@")
  const username = email_list[0];

  React.useEffect(() => { 
    fetch('/api/get-user-postings', {
      method: 'POST',
      body: JSON.stringify(email),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then((data) => {
      const postFetchList = []

        for (const posting of data) {
          console.log("posting_id is:", posting.posting_id);
          postFetchList.push(
            <PostListItemWithDelete
              key={posting.posting_id}
              posting_id={posting.posting_id}
              date={posting.date}
              title={posting.title}
              desc={posting.desc}
              contact_info={posting.contact_info}
              image_url={posting.image_url}
            />
           );
          }
       setPostList(postFetchList);   
     })
    }, []);

    const postHousingButton = () => {
      history.push("/post-housing");
    }

    let history = useHistory();

  return (
    <React.Fragment>
      <Container>
          <h4>Welcome {username}!
              <Button id="post-button" type="button" onClick={postHousingButton}> Post Housing </Button>
              <Logout />
          </h4>
            <h5>Your posted housing listings are below:</h5>
            {postList}
       </Container>
    </React.Fragment>
  );
}

function Logout() {

  let history = useHistory();

  const handleLogout = () => {
    if (!localStorage.getItem('logged_in_user')) {
      alert("User isn't logged in");
      history.push("/");
    } else {
        localStorage.removeItem('logged_in_user');
        alert("Log out successful.");
        history.push("/");
      }
    }

  return(
    <Button id="logout-button" type="button" onClick={handleLogout}> Logout </Button>
  );
}

function App() {

  return (
    <Router>
        <Navbar bg="light" sticky="top">
          <Nav className="ml-auto">
            <Nav.Item>
              <Nav.Link href="/"> Home </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="/map"> Neighborhoods </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="/login"> Login </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="/create-user"> Create Account </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="/profile"> Profile </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="/post-housing"> Post Housing </Nav.Link>
            </Nav.Item>
          </Nav>
        </Navbar>
      
        <Switch>
          <Route exact path="/login">
              <Login />
            </Route>
            <Route exact path="/logout">
              <Logout />
            </Route>
            <Route exact path="/create-user">
              <CreateUser />
            </Route>
            <Route exact path="/neighborhood/:neighborhood_id">
              <Neighborhood />
            </Route>
            <Route path="/housing/:neighborhood_id">
              <FindHousing />
            </Route>
            <PrivateRoute exact path="/post/:neighborhood_id">
              <PostHousing />
            </PrivateRoute>
            <PrivateRoute exact path="/profile">
              <UserProfile />
            </PrivateRoute>
            <PrivateRoute exact path="/post-housing">
              <MapHousing />
            </PrivateRoute>
            <Route exact path="/map">
              <MapView />
            </Route>       
            <Route exact path="/send-email/:posting_id">
                <ContactSellerForm />
            </Route>
            <Route exact path="/">
              <Homepage />
            </Route>
          </Switch>
    </Router>
  );
}

ReactDOM.render(<App />, document.querySelector('#root'));
