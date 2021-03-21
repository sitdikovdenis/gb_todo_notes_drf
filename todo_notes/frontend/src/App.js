
import React from 'react';
import './App.css';
import AuthorList from './components/Author.js'
import MenuItem from './components/Menu.js'
import FooterItem from './components/Footer.js'
import ProjectList from './components/Project.js'
import TODOList from './components/TODOs.js'
import {BrowserRouter, Switch, Link, Route} from 'react-router-dom'
import axios from 'axios'

class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'authors': [],
           'projects': [],
           'todos': []
       }
   }

   componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/employees/')
            .then(response => {
                this.setState({
                        'authors': response.data.results
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                this.setState({
                        'projects': response.data.results
                    }
                )
            }).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/todos/')
            .then(response => {
                this.setState({
                        'todos': response.data.results
                    }
                )
            }).catch(error => console.log(error))

    }

    render() {
        return (
          <div className="App">
            <BrowserRouter>
              <MenuItem/>
              <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />}  />
              <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
              <Route exact path='/todos' component={() => <TODOList items={this.state.todos} />} />
            </BrowserRouter>
            <FooterItem/>
          </div>
        )
  }
}


export default App;

