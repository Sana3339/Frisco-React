const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;
const useHistory = ReactRouterDOM.useHistory;

function Homepage() {
  return (
    <React.Fragment>
      This is the homepage
    </React.Fragment>
  );   
}

function MapView(props){
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

            //console.log(aMarker.neighborhood_id);

          const infoWindow = new google.maps.InfoWindow({
            content: aMarker.windowContent
            });
          
          const marker = new window.google.maps.Marker({
            position:aMarker.coords,
            animation: google.maps.Animation.DROP,
            map:gMap
            });

            marker.addListener("dblclick", () => {
              history.push(`/neighborhood/${aMarker.neighborhood_id}`);
              console.log(aMarker.neighborhood_id);
            })
            marker.addListener("click", () => {
              infoWindow.open(gMap,marker)
              });
          //   marker.addListener("dblclick", () => {
          //     infoWindow.close(gMap,marker)
          //   });
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
        <div
        style={{ height: "500px", width:"60%" }}
        {...{ref}}>
        </div>
      </React.Fragment>
    );
  }

  //<Link to={`/neighborhood/${neighborhood_id}`}> Neighborhood Details </Link>


function MapContainer() {

  return (
    <React.Fragment>
      Click on a marker to learn more about the neighborhood
      <MapView  />
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
      <Restaurants neighborhood_id={neighborhood_id} />
    </React.Fragment>
  );
}

function Restaurants(props) {

  console.log("I'm the neighborhood id from inside Restaurant component", props.neighborhood_id);

  return(
    <React.Fragment>
        I'm a list of restaurants
    </React.Fragment>
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
    fetch("/api/jobs.json")
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

function Login(props) {
  return (
    <div>
      Username:
      <input type="text"></input>
      Password:
      <input type="text"></input>
      <button> Login </button> 
    </div>
  )
}

function App() {

  //const neighborhood_id = "test";

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
            {/* <li>
              <Link to={`/neighborhood/${neighborhood_id}`}> Neighborhood Details </Link>
            </li> */}
            <li>
              <Link to="/login"> Login </Link>
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
            <Route path="/neighborhood/:neighborhood_id">
              <Neighborhood />
            </Route>
            <Route exact path="/map">
              <MapContainer />
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
          </Switch>
        </div>
    </Router>
  );
}

ReactDOM.render(<App />, document.querySelector('#root'));
