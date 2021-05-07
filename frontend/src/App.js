import React from 'react';
import './App.css';
import AuthorList from './components/Author.js'
import FooterItem from './components/Footer.js'
import ProjectList from './components/Project.js'
import TODOList from './components/TODOs.js'
import LoginForm from './components/Auth.js'
import {BrowserRouter, Link, Route} from 'react-router-dom'
import axios from 'axios'
import Cookies from 'universal-cookie';
import ProjectForm from "./components/ProjectForm";
import TODOForm from "./components/TODOForm";


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}


class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'projects': [],
            'todos': []
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }


    load_data() {
        const headers = this.get_headers()

        axios.get('http://127.0.0.1:8000/api/1.0/employees/', {headers})
            .then(response => {
                this.setState({'authors': response.data.results})
            }).catch(error => {
            console.log(error)
            this.setState({authors: []})
        })


        axios.get('http://127.0.0.1:8000/api/1.0/projects/', {headers})
            .then(response => {
                this.setState({'projects': response.data.results})
            }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })


        axios.get('http://127.0.0.1:8000/api/1.0/api_todos/', {headers})
            .then(response => {
                this.setState({'todos': response.data.results})
            }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }


    deleteProject(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/1.0/projects/${id}`, {headers, headers})
            .then(response => {
                this.setState({projects: this.state.projects.filter((item) => item.uuid !== id)})
            }).catch(error => console.log(error))
    }

    createProject(name, repository_url, users) {
        const headers = this.get_headers()
        const data = {name: name, repository_url: repository_url, users: [users]}
        axios.post(`http://127.0.0.1:8000/api/1.0/projects/`, data, {headers, headers})
            .then(response => {
                let new_project = response.data


                this.setState({projects: [this.state.projects, new_project]})
            }).catch(error => console.log(error))
    }

    deleteTODO(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/1.0/todos/${id}`, {headers, headers})
            .then(response => {
                this.setState({todos: this.state.todos.filter((item) => item.uuid !== id)})
            }).catch(error => console.log(error))
    }

    createTODO(text, author, project) {
        const headers = this.get_headers()
        const data = {text: text, author: author, project: project}
        axios.post(`http://127.0.0.1:8000/api/1.0/todos/`, data, {headers, headers})
            .then(response => {
                let new_todo = response.data


                this.setState({todos: [this.state.todos, new_todo]})
            }).catch(error => console.log(error))
    }


    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link to='/'>Authors</Link></li>
                            <li><Link to='/projects'>Projects</Link></li>
                            <li><Link to='/todos'>TODOs</Link></li>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                                    <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                    <Route exact path='/projects/create' component={() => <ProjectForm users={this.state.authors}
                        createProject={(name, repository_url, users) => this.createProject(name, repository_url, users)}/>}/>

                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}
                                                                                deleteProject={(id) => this.deleteProject(id)}/>}/>

                    <Route exact path='/todos/create' component={() => <TODOForm author={this.state.authors} project={this.state.projects}
                        createTODO={(text, author, project, state) => this.createTODO(text, author, project, state)}/>}/>

                    <Route exact path='/todos' component={() => <TODOList items={this.state.todos}
                                                                                deleteTODO={(id) => this.deleteTODO(id)}/>}/>
                    <Route exact path='/login' component={() => <LoginForm
                        get_token={(username, password) => this.get_token(username, password)}/>}/>
                </BrowserRouter>
                <FooterItem/>
            </div>
        )
    }
}


export default App;

