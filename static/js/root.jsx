const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
const useHistory = ReactRouterDOM.useHistory;
const useLocation = ReactRouterDOM.useLocation;

function Homepage() {
  let history = useHistory();
  
  const redirectToMapPage = () => {
    history.push('/map');
  }

  return (
    <React.Fragment>
      <p>Which San Francisco neighborhood should you live in?</p>
      <button type="submit" onClick={redirectToMapPage}> Enter </button>
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
              console.log(aMarker.neighborhood_id);
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

    //const neighborhood_id = "marina";

    return (
      <React.Fragment>
        Click on a marker to learn more about the neighborhood
        <div id="map"
        style={{ height: "500px", width:"60%" }}
        {...{ref}}>
        </div>
      </React.Fragment>
    );
  }

  //<Link to={`/neighborhood/${neighborhood_id}`}> Neighborhood Details </Link>


function MapHousing() {
  const options = {
    zoom:12,
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
    Click on a marker closest to the housing you'd like to post
      <div
      style={{ height: "500px", width:"60%" }}
      {...{ref}}>
    </div>
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


  return(
    <React.Fragment>
      <p><b>{name}</b></p>
      <p>{desc} </p>
      <p>Median Home Price: ${medianHomePrice}</p>
      <p>Median Rental Price: ${medianRental}</p>
      <p>Sq Ft Price: ${sqFtPrice}</p>
      <p>Walk Score: {walkScore}</p>
      <p>Transit Score: {transitScore}</p>
      <Images neighborhood_id={neighborhood_id} />
      <Restaurants neighborhood_id={neighborhood_id} />
      <p><Link to={`/housing/${neighborhood_id}`}> Find {name} housing </Link></p>
      <p><Link to={`/post/${neighborhood_id}`}> Post {name} housing </Link></p>
      
    </React.Fragment>
  );
}

function Images(props) {

  const [imageList, setImageList] = React.useState([" loading..."]);

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
      Images should load here:
        {imageList}
    </React.Fragment>
  );
}

function ImageListItem(props) {
  
  const image_url = `/static/img/${props.image_name}`

  return (
    <p>
    <img className="photo" src={image_url} />
    </p>
  );
}

function RestaurantListItem(props) {

  return(
    <div className="restaurant-list">
      <p><b>{props.name}</b></p>
      <p>Address: {props.address}</p>
      <p>Rating: {props.rating}</p>
      <a href={props.website}>Website</a>
    </div>
  );
}

function Restaurants(props) {

  const [restaurantList, setRestaurantList] = React.useState([" loading..."]);

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
            />
          );
        }
        setRestaurantList(restaurantFetchList);
    })
  }, [])

  return(
    <React.Fragment>
      Restaurants
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
      <b>{neighborhoodName} Housing</b>
      {postList}
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
      <b>Post {neighborhoodName} Housing</b>
      <div>
        <p>
          Title:
          <input
            type="text"
            onChange={(event) => setTitle(event.target.value)}
            value={title}
            />
        </p>
        <p>
          Description:
          <textarea
            onChange={(event) => setDesc(event.target.value)}
            value={desc}
          />
        </p>
        <p>
          Contact Info:
          <input
            type="text"
            onChange={(event) => setContact_info(event.target.value)}
            value={contact_info}
          />
        </p>
          <div>
            <input type="file" onChange= {(event)=> setImage(event.target.files[0])}></input>
              <button onClick={uploadImage}>Upload</button>
            </div>
          <div>
              Uploaded image here:
              <img src={url} />
          </div>
        <button onClick={createNewPost}> Add Posting </button>
      </div>
    </React.Fragment>
  );
}

function PostListItem(props){

  return(
    <React.Fragment>
      <p>{props.date}</p>
      <p>{props.title}</p>
      <p>{props.desc}</p>
      <p>{props.contact_info}</p>   
      <img src={props.image_url} />
    </React.Fragment>
  );
}

//This is a copy of the PostListItem component above but it includes delete functionality.
//These are different components bc a post should only be able to be deleted by the user who created it
//from their user profile page
function PostListItemWithDelete(props){

  return(
    <React.Fragment>
      <p>{props.date}</p>
      <p>{props.title}</p>
      <p>{props.desc}</p>
      <p>{props.contact_info}</p>   
      <img src={props.image_url} />
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

function SearchBox() {
  return (
    <div id="search-box">
      Search:
      <input type="text"></input>
      <button>Search</button>
    </div>
  );
}

function DeleteJobBox() {
  //This is a fully controlled form
  const [jobID, setjobID] = React.useState('')

  const deleteJob = () => {
    fetch('/api/delete-job', {
      method: 'POST',
      body: JSON.stringify(jobID)
    })
    .then(response => response.json())
    .then(data => {
      if (data) {
        alert("Job Deleted");
      }
    });
   }
  
  return (
    <form action="/jobs">
        Job ID to Delete:
        <input 
          type="text" 
          onChange={(event) => setjobID(event.target.value)}
          value={jobID}
        />
        <button type="submit" onClick={deleteJob}> Delete </button>
    </form> 
  );
}
  

function JobListItem(props) {
  
  return(
    <div className="jobcard">
      <p>ID: {props.job_id}</p>
      <p>Position: {props.job_name}</p>
      <p>Company: {props.company}</p>
    </div>
  );
}

function AddJob(props) {
  //This is a fully controlled form
  const [name, setName] = React.useState('')
  const [company, setCompany] = React.useState('')

  const addNewJob = () => {
    const job = {"job_name": name, "company": company}
    fetch('/api/add-job', {
      method: 'POST',
      body: JSON.stringify(job)
    })
      .then(response => response.json())
      .then(data => {
        if (data === "Success") {
          alert('Job added')
        }
    });
  }

  return (
    <form action="/jobs">
      <p>
        Position:
        <input 
          type="text" 
          onChange={(event) => setName(event.target.value)}
          value={name}
        />
      </p>
      <p>
        Company:
        <input 
          type="text" 
          onChange={(event) => setCompany(event.target.value)}
          value={company}
        />
        <button type="submit" onClick={addNewJob}> Add Job </button>
      </p>
    </form>
  )
}
//By changing the type of the button to "button" above, it prevents the default behavior of submitting


function JobsList(props) {

  //get info from server, make components out of it, render them

  const [jobList, setJobList] = React.useState(["loading..."]);

  

  React.useEffect(() => {
    fetch('/api/jobs.json')
    .then(response => response.json())
    .then((data) => {
      
      const jobList = []
      
      for (const job of data) {
        jobList.unshift(
          <JobListItem 
            key={job.job_id}
            job_id={job.job_id}
            job_name={job.job_name}
            company={job.company}
            />
        );
      }
      setJobList(jobList)
    })
  }, [])

  return (
      <React.Fragment>
        <SearchBox />
        <DeleteJobBox />
        {jobList}
      </React.Fragment>
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
      Create Account
      <form>
        <p>
          Email:
          <input
            type="text"
            onChange={(event) => setEmail(event.target.value)}
            value={email}
          />
        </p>
        <p>
          Password:
          <input
            type="password"
            onChange={(event) => setPassword(event.target.value)}
            value={password}
          />
          <button type="button" onClick={createNewUser}>Submit</button>
        </p>
      </form>
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
      

      <p><b>Login</b></p>

      You must be logged in to post housing.
    <form>
      <p>
      Email:
      <input 
        type="text"
        onChange={(event) => setEmail(event.target.value)}
        value={email || ''}
        />
      </p>
      <p>
      Password:
      <input 
        type="password"
        onChange={(event) => setPassword(event.target.value)}
        value={password || ''}
        />
        <button type="button" onClick={loginUser}> Login </button> 
      </p>
    </form>
      Not registered? &nbsp;
      <Link to="/create-user">Create account</Link>
    </React.Fragment>
  );
}

function UserProfile() {

//  let history = useHistory();
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
      <b>Welcome {username}!</b>
      <p>
      <Logout />
      <button type="button" onClick={postHousingButton}> PostHousing </button>
      </p>
       {postList}
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
    <button type="button" onClick={handleLogout}> Logout </button>
  );
}

function App() {

//  let history = useHistory();

  

  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/"> Home </Link>
            </li>
            <li>
              <Link to="/map"> Map Container </Link>
            </li>
            <li>
              <Link to="/login"> Login </Link>
            </li>
            <li>
              <Link to="/logout"> Logout </Link>
            </li>
            <li>
              <Link to="/create-user"> Create Account </Link>
            </li>
            <li>
              <Link to="/profile"> Profile </Link>
            </li>
            <li>
              <Link to="/post-housing"> Post Housing </Link>
            </li>
            <li>
              <Link to="/jobs"> Jobs </Link>
            </li>
            <li>
              <Link to="/add-job"> Add Job </Link>
            </li>
          </ul>
        </nav>
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
            <Route path="/neighborhood/:neighborhood_id">
              <Neighborhood />
            </Route>
            <Route path="/housing/:neighborhood_id">
              <FindHousing />
            </Route>
            <PrivateRoute path="/post/:neighborhood_id">
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
            <Route exact path="/jobs">
              <JobsList />
            </Route>   
            <Route exact path="/add-job">
              <AddJob />
            </Route>   
            <Route exact path="/">
              <Homepage />
            </Route>
            {/* <Route exact path="'*">
              <NoMatch />
            </Route> */}
          </Switch>
        </div>
    </Router>
  );
}

ReactDOM.render(<App />, document.querySelector('#root'));
