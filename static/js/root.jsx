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

function JobListItem(props) {
  return(
    <div className="jobcard">
      <p>Position: {props.job_name}</p>
      <p>Company: {props.company}</p>
    </div>
  );
}

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
          <Route path="/">
            <Homepage />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

ReactDOM.render(<App />, document.querySelector('#root'));
