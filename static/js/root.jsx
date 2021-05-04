const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;

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
    center:{lat:37.7618, lng:-122.4432}
    };
  const ref = React.useRef();
  const [map, setMap] = React.useState("");
  const [markerList, setMarkerList] = React.useState("");

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
          };
          markerList.push(markerDetails);
         }
         setMarkerList(markerList);
      
          console.log(markerList);
          
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
            infoWindow.open(gMap,marker)
            });
            marker.addListener("dblclick", () => {
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
        <div
        style={{ height: "500px", width:"60%" }}
        {...{ref}}>
        </div>
      </React.Fragment>
    );
  }


function MapContainer() {

  return (
    <React.Fragment>
      Map
      <MapView  />
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
