const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Link = ReactRouterDOM.Link;
const Prompt = ReactRouterDOM.Prompt;
const Switch = ReactRouterDOM.Switch;
const Redirect = ReactRouterDOM.Redirect;

function Homepage() {
  return <div> Welcome to my site </div>
}

function About() {
  return (<div> A tiny react demo site </div>)
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
    .then(response = response.json())
    .then(data => {
      if (data === "Success") {
        alert("Job deleted")
      }
    });
   }
  
  return (
    <form>
        Job ID to Delete:
        <input 
          type="text" 
          onChange={(event) => setjobID(event.target.value)}
          value={jobID}
        />
        <button type="button" onClick={deleteJob}> Delete </button>
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
    <form>
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
        <button type="button" onClick={addNewJob}> Add Job </button>
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
        jobList.push(
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
