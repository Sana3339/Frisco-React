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
const Container = ReactBootstrap.Container;
const Row = ReactBootstrap.Row;
const Col = ReactBootstrap.Col;
const Card = ReactBootstrap.Card;
const Alert = ReactBootstrap.Alert;
const Table = ReactBootstrap.Table;
const Jumbotron = ReactBootstrap.Jumbotron;
const OverlayTrigger = ReactBootstrap.OverlayTrigger;
const Tooltip = ReactBootstrap.Tooltip;
const Modal = ReactBootstrap.Modal;

function Homepage() {
  let history = useHistory();
  
  const redirectToMapPage = () => {
    history.push('/map');
  }

  return (
    <React.Fragment>
      
        <Jumbotron className="Frisco-background">
          <Row className="justify-content-center">
            <div className="block-center">
              <div id="Frisco">Frisco</div>
              <div id="Frisco-subheading">Which San Francisco neighborhood should you live in?</div>
              <Button id="button-Frisco" type="button" variant="light" onClick={redirectToMapPage}> Enter </Button>
            </div>
          </Row>
          
            <div id="homepage-footer">
              <i className="fab fa-github"></i>
                <a href="https://github.com/Sana3339" style={{ color:"black", fontWeight:"400" }}>&nbsp;github.com/Sana3339</a><br></br>
              <i className="fab fa-linkedin-in"></i>
                <a href="https://www.linkedin.com/in/sanaahmad/" style={{ color:"black", fontWeight:"400" }}>&nbsp;linkedin.com/in/sanaahmad</a>
            </div>
          
        </Jumbotron>
      
    </React.Fragment>
  );   
}

function MapView(){
  const options = {
    zoom:12.4,
    center:{lat:37.7822, lng:-122.4342}
    };
  const ref = React.useRef();
  // const [map, setMap] = React.useState("");
  // const [markerList, setMarkerList] = React.useState("");
  let history = useHistory();

  // React.useEffect(() => {
  //   fetch("/api/neighborhood-details.json")
  //   .then(response => response.json())
  //   .then((data) => {

  //     const markerList = [];

  //     for (const neighborhood of data) {
  //       const markerDetails = {
  //         coords: {lat:neighborhood.latitude, lng:neighborhood.longitude},
  //         windowContent: neighborhood.short_desc,
  //       };
  //       markerList.push(markerDetails);
  //      }
  //      setMarkerList(markerList)
  //     })
  // }, []);

  React.useEffect(() => {
    const onLoad = () => {
      const gMap = new window.google.maps.Map(ref.current, options);
      // setMap(gMap);

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
        //  setMarkerList(markerList);
          
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
        <Jumbotron className="map-background">
          <Row className="justify-content-center">
            <Container>
              <h4 id="map-heading">Click on a marker to learn more about the neighborhood</h4>
              <div id="map"
              style={{ height: "470px", width:"70%" }}
              {...{ref}}>
              </div>
            </Container>
          </Row>
        </Jumbotron>
      </React.Fragment>
    );
  }

  //<Link to={`/neighborhood/${neighborhood_id}`}> Neighborhood Details </Link>


function MapHousing() {
  const options = {
    zoom:12.4,
    center:{lat:37.7822, lng:-122.4342},
    };

  //Line below is to control the state of our modal
  const [isOpen, setIsOpen] = React.useState(true);

  const ref = React.useRef();
  // const [map, setMap] = React.useState("");
  // const [markerList, setMarkerList] = React.useState("");
  let history = useHistory();

  // React.useEffect(() => {
  //   fetch("/api/neighborhood-details.json")
  //   .then(response => response.json())
  //   .then((data) => {

  //     const markerList = [];

  //     for (const neighborhood of data) {
  //       const markerDetails = {
  //         coords: {lat:neighborhood.latitude, lng:neighborhood.longitude},
  //         windowContent: neighborhood.name,
  //       };
  //       markerList.push(markerDetails);
  //      }
  //      setMarkerList(markerList)
  //     })
  // }, []);

  React.useEffect(() => {
    const onLoad = () => {
      const gMap = new window.google.maps.Map(ref.current, options);
      // setMap(gMap);

      const addMarkers = () => 
        fetch("/api/neighborhood-details.json")
        .then(response => response.json())
        .then((data) => {

        const markerList = [];

        for (const neighborhood of data) {
          const markerDetails = {
            coords: {lat:neighborhood.latitude, lng:neighborhood.longitude},
            windowContent: `<div style='font-size:1rem;'>${neighborhood.name}`,
            neighborhood_id: neighborhood.neighborhood_id
          };
          markerList.push(markerDetails);
         }
        //  setMarkerList(markerList);
          
          for (const aMarker of markerList) {

          const infoWindow = new google.maps.InfoWindow({
            content: aMarker.windowContent
            });
          
          const marker = new window.google.maps.Marker({
            position:aMarker.coords,
            animation: google.maps.Animation.DROP,
            map:gMap,
            icon: {
              url: "/static/img/blue-pushpin.png",
              scaledSize: new google.maps.Size(38, 38)
             }
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

    //This function closes the modal
    const handleClose = () => setIsOpen(false);

  return (
    <React.Fragment>
        <Jumbotron className="posting-map-background">
        <Modal show={isOpen}>
              <Modal.Body className="modal-text">Click on the pin closest to the housing you'd like to post.</Modal.Body>
                <Modal.Footer>
                  <Button onClick={handleClose}>Got it!</Button>
                </Modal.Footer>
            </Modal>
          <Row className="justify-content-center">
            <Container>
              <h4 id="map-heading">Click on the pin closest to the housing you'd like to post</h4>
                  <div id="map"
                  style={{ height: "470px", width:"70%" }}
                  {...{ref}}>
                </div>
            </Container>
          </Row>
        </Jumbotron>
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

  const redirectToPostHousing = () => {
    history.push(`/post/${neighborhood_id}`)
  }

  const redirectToMap = () => {
    history.push('/map')
  }

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
                   <p id="data-source">Sources: Wikipedia, Zumper, Zillow and Walk Score, May 2021</p> 

                </Col>
              <Col s={12} md={7}> 
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
              <h5>&nbsp; {name} Restaurants</h5>  
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
        <h3 className="find-housing-title">{neighborhoodName} Housing</h3>
        <hr></hr>
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

  //Line below is to control the state of our modal
  const [isOpen, setIsOpen] = React.useState(false);

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
 //       alert('Post added.')
        setIsOpen(true);
      }
    });
 //   history.push('/profile');
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

  const renderTooltip = (props) => (
    <Tooltip id="button-tooltip" {...props}>
      Provide an email where you would like to receive responses to your post.
      Your email will be anonymized and not shared directly with users.
    </Tooltip>
  );

  const redirectToProfile = () => {
    history.push('/profile');
}
  
  return (
    <React.Fragment>
        <Jumbotron className="post-housing-background">
          <Row className="justify-content-center">
            <Col sm={12} md={7}>
            <Modal show={isOpen}>
              <Modal.Body modal-text>Your post has been added.</Modal.Body>
                <Modal.Footer>
                  <Button className="modal-button" onClick={redirectToProfile}>Go to Profile</Button>
                </Modal.Footer>
            </Modal>
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
                
                  <p className="posting-form-header">Email: 
                      <OverlayTrigger
                        placement="right"
                        delay={{ show: 250, hide: 400 }}
                        overlay={renderTooltip}>
                          <i className="fa fa-question-circle" aria-hidden="true"></i>
                      </OverlayTrigger> 
                  </p>
                    <input
                      className="posting-form-input"
                      type="email"
                      onChange={(event) => setContact_info(event.target.value)}
                      value={contact_info}
                    />
                
                  <div className="posting-file-input">
                    <input type="file" onChange= {(event)=> setImage(event.target.files[0])}></input>
                      <button onClick={uploadImage}>Upload</button>
                    </div>
                    <div>
                        <img className="input-posting-image" src={url} />
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
        <p>{props.date} &nbsp; <b>{props.title}</b></p>
        <p>{props.desc}</p>  
        <img className="find-housing-image" src={props.image_url} />
        <p><Button onClick={redirectToContact}>Contact Seller</Button></p>
        <hr></hr>
    </React.Fragment>
  );
}

function ContactSellerForm() {

  const [fromName, setFromName] = React.useState('');
  const [sellerEmail, setSellerEmail] = React.useState('');
  const [replyToEmail, setReplyToEmail] = React.useState('');
  const [message, setMessage] = React.useState('');

  //Line below is to control the state of our modal
  const [isOpen, setIsOpen] = React.useState(false);

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
 //             alert("Your message has been sent")

            //Once form is submitted, modal is displayed
              setIsOpen(true);

            //Form is reset  
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
      <Jumbotron className="contact-seller-background">
        <Row className="justify-content-center">
          <Card className="contact-seller-form bg-light">
            <Modal show={isOpen}>
              <Modal.Body modal-text>Your message has been sent</Modal.Body>
                <Modal.Footer>
                  <Button className="modal-button" onClick={redirectBack}>Back to Housing</Button>
                </Modal.Footer>
            </Modal>
            <Card.Body>
              <Card.Title className="text-center">Contact Seller</Card.Title>
                <Form onSubmit={sendEmail}>
                  
                    <input type="hidden" name="seller_email" 
                        onChange={(event) => setSellerEmail(event.target.value)}
                        value={sellerEmail}/>
                    <Form.Group>
                      <label className="contact-seller-header">Your Name:</label><br></br>
                      <input 
                          type="text" 
                          name="from_name" 
                          className="contact-seller-input"
                          onChange={(event) => setFromName(event.target.value)}
                          value={fromName}/>
                    </Form.Group>
                  
                    <Form.Group>
                      <label className="contact-seller-header">Your Email:</label><br></br>
                      <input 
                          type="email" 
                          name="reply_to" 
                          className="contact-seller-input"
                          onChange={(event) => setReplyToEmail(event.target.value)}
                          value={replyToEmail}/>
                    </Form.Group>

                    <Form.Group>
                      <label className="contact-seller-header">Your Message:</label><br></br>
                      <textarea 
                          name="message"
                          className="contact-seller-textarea"
                          onChange={(event) => setMessage(event.target.value)}
                          value={message}/>
                      <br></br>&emsp;&emsp;&emsp;&emsp;
                    <Button type="submit" value="Send" >Send</Button>
                    <Button onClick={redirectBack}>Back</Button>
                  </Form.Group>
                </Form>
              
            </Card.Body>
          </Card>
        </Row>
      </Jumbotron>
    </React.Fragment>
    );
}


//This is a copy of the PostListItem component above but it includes delete functionality.
//These are different components bc a post should only be able to be deleted by the user who
//created it from their user profile page
function PostListItemWithDelete(props){

  return(
    <React.Fragment>
        <p>{props.date} &nbsp; <u><b>{props.title}</b></u></p>
        <p>{props.desc}</p>  
        <img className="posting-image" src={props.image_url} />
        <DeletePosting posting_id={props.posting_id}/> 
        <hr></hr>
    </React.Fragment>
  );
}

function DeletePosting(props) {  

  const deletePosting = () => {
    fetch('/api/delete-posting', {
      method: 'POST',
      body: JSON.stringify(props.posting_id)
    })
    .then(response => response.json())
    .then(data => {
      if (data) {
//        alert("Posting Deleted");
      }
    });
   }

  return (
    <form action="/profile">
      <button className="delete-button" type="submit" onClick={deletePosting}>Delete</button>
    </form>
  );
}

function CreateUser() {

  let history = useHistory();

  const[email, setEmail] = React.useState('');
  const[password, setPassword] = React.useState('');

  const [isOpen1, setIsOpen1] = React.useState(false);
  const [isOpen2, setIsOpen2] = React.useState(false);

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
 //       alert(data.message);
        setIsOpen1(true);
 //       history.push('/login');
      } else {
 //       alert(data.message);
        localStorage.setItem('logged_in_user', data.email);
 //       history.push('/login');
        setIsOpen2(true);
      }
    })
  }

  const redirectToLogin = () => {
    history.push('/login');
}

  return(
    <React.Fragment>
        <Jumbotron className="create-account-background">
          <Row className="justify-content-center">
          <Modal show={isOpen1}>
              <Modal.Body modal-text>Error - user already exists. Please log in.</Modal.Body>
                <Modal.Footer>
                  <Button className="modal-button" onClick={redirectToLogin}>Go to Login</Button>
                </Modal.Footer>
            </Modal>
            <Modal show={isOpen2}>
              <Modal.Body modal-text>Account created. Please log in.</Modal.Body>
                <Modal.Footer>
                  <Button className="modal-button" onClick={redirectToLogin}>Go to Login</Button>
                </Modal.Footer>
            </Modal>
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

function Login() {

  let history = useHistory();
  const { state } = ReactRouterDOM.useLocation();
  const {setIsLoggedIn} = React.useContext(AuthContext);

  const [redirectToReferrer, setredirectToReferrer] = React.useState(false)

  const [email,setEmail] = React.useState();
  const [password,setPassword] = React.useState();

  const [isOpen1, setIsOpen1] = React.useState(false);
  const [isOpen2, setIsOpen2] = React.useState(false);

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
//        alert(data.message);
//        history.push('/create-user');
          setIsOpen1(true);
      } else if (data.message === "Incorrect password.") {
//          alert(data.message);
//          history.push('/login')
          setIsOpen2(true);
      } else if (data.message === "You are now logged in.") {
 //         alert(data.message);
          setIsLoggedIn(true);
          localStorage.setItem('logged_in_user', data.email);
         setredirectToReferrer(true);
        }
      }
    ) 
  }

  if (redirectToReferrer === true) {
    if (state) {
      return <Redirect to={state.from}/>
    } else {
      return <Redirect to="/profile"/>
   }
  }

  const redirectToCreateAccount = () => {
    history.push('/create-user');
  }

  const handleClose = () => setIsOpen2(false);
  

  return (
    <React.Fragment>
      <Jumbotron className="login-background">
        
        <Row className="justify-content-center">
            <Alert variant="primary" style={{ fontSize:"1rem", fontWeight:"300" }}>
              <p><b>You must be logged in to post housing.</b></p>
            </Alert>
        </Row>
          <Modal show={isOpen1}>
              <Modal.Body modal-text>No account exists for that email. Please create an account.</Modal.Body>
                <Modal.Footer>
                  <Button onClick={redirectToCreateAccount}>OK</Button>
                </Modal.Footer>
            </Modal>
            <Modal show={isOpen2}>
              <Modal.Body modal-text>Incorrect password.</Modal.Body>
                <Modal.Footer>
                  <Button onClick={handleClose}>OK</Button>
                </Modal.Footer>
            </Modal>
 
          <Row className="justify-content-center">
            <Card className="user-form">
              <Card.Body>
                <Card.Title className="text-center">Login</Card.Title>
                  <Form>
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

  let history = useHistory();

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
       setPostList(postFetchList.reverse());   
     })
    }, [email]);

    const postHousingButton = () => {
      history.push("/post-housing");
    }

  if(postList.length === 0) {
    setPostList("You have no housing posted.")
  } 

  return (
    <React.Fragment>
      <Container>
          <h4>Welcome {username}!
              <Button id="post-button" type="button" onClick={postHousingButton}> Post Housing </Button>
              <Logout />
          </h4>
            <h5>Your posted housing listings are below:</h5>
            <hr></hr>
            {postList}
       </Container>
    </React.Fragment>
  );
}

function Logout() {

  let history = useHistory();
  const {setIsLoggedIn} = React.useContext(AuthContext);

  const handleLogout = () => {
    if (!localStorage.getItem('logged_in_user')) {
//      alert("User isn't logged in");
      history.push("/");
    } else {
        localStorage.removeItem('logged_in_user');
//        alert("Log out successful.");
        setIsLoggedIn(false);
        history.push("/");
      }
    }

  return(
    <Button id="logout-button" type="button" onClick={handleLogout}> Logout </Button>
  );
}


function NavigationBar() {
  const {isLoggedIn, setIsLoggedIn} = React.useContext(AuthContext);
  let history = useHistory();

  const handleLogout = () => {
    localStorage.removeItem('logged_in_user');
  //      alert("Log out successful.");
        setIsLoggedIn(false);
        history.push("/");
    }

  if (isLoggedIn == true) {
    return(
      <Navbar bg="light" sticky="top">
        <Navbar.Brand href="/" id="Frisco-navbar-brand">Frisco</Navbar.Brand>
          <Nav className="ml-auto">
            <Nav.Item>
              <Nav.Link href="/"> Home </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="/map"> Neighborhoods </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="/profile"> Profile </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="/post-housing"> Post Housing </Nav.Link>
          </Nav.Item>
          <Nav.Item>
              <Nav.Link onClick={handleLogout}> Logout </Nav.Link>
          </Nav.Item>
      </Nav>
    </Navbar>
    )
  } else {
    return (
      <Navbar bg="light" sticky="top">
      <Navbar.Brand href="/" id="Frisco-navbar-brand">Frisco</Navbar.Brand>
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
      </Nav>
    </Navbar>
  );
 }
}

//creating an instance of AuthContext which should be outside of any function
const AuthContext = React.createContext();

function App() {

  const [isLoggedIn, setIsLoggedIn] = React.useState();

  React.useEffect(() => {
    if (localStorage.getItem('logged_in_user') !== null) {
      setIsLoggedIn(true);
    }
  }, [isLoggedIn])

  return (
    <Router>
        <AuthContext.Provider value={{isLoggedIn, setIsLoggedIn}}>
            <NavigationBar />
      
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
      </AuthContext.Provider>
    </Router>
  );
}

ReactDOM.render(<App />, document.querySelector('#root'));
