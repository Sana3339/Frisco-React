const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;

function MapView(){
  const options = {
    zoom:12.2,
    center:{lat:37.7618, lng:-122.4432}
    };
  const ref = React.useRef();
  const [map, setMap] = React.useState("");

  React.useEffect(() => {
    const onLoad = () => {
      const gMap = new window.google.maps.Map(ref.current, options);
      setMap(gMap);
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
      console.log("Script is adding")
    }, []);

    return (
      <div
      style={{ height: "60vh", margin: "1em 0", borderRadius: "0.5em" }}
      {...{ref}}>
      </div>
    );
  }



function Homepage() {
  return (
    <React.Fragment>
      Welcome to my site
    </React.Fragment>
  );
    
}

function About() {
  return (
    <React.Fragment>
      Map
      <MapView />
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
          <u1>
            <li>
              <Link to="/"> Home </Link>
            </li>
            <li>
              <Link to="/about"> About </Link>
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
          </u1>
        </nav>
        <Switch>
        <Route path="/login">
            <Login />
          </Route>
          <Route path="/about">
            <About />
          </Route>       
          <Route path="/jobs">
            <JobsList />
          </Route>   
          <Route path="/add-job">
            <AddJob />
          </Route>   
          <Route path="/">
            <Homepage />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

ReactDOM.render(<App />, document.querySelector('#root'));
