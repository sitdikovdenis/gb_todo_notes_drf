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
        this.setState({'token': token})
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
        this.setState({'token': token})
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    load_data() {
        axios.get('http://127.0.0.1:8000/api/employees/')
            .then(response => {
                this.setState({'authors': response.data.results})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                this.setState({'projects': response.data.results})
            }).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/api_todos/')
            .then(response => {
                this.setState({'todos': response.data.results})
            }).catch(error => console.log(error))
    }


    componentDidMount() {
        this.get_token_from_storage()
        this.load_data()
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
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>
                    <Route exact path='/todos' component={() => <TODOList items={this.state.todos}/>}/>
                    <Route exact path='/login' component={() => <LoginForm
                        get_token={(username, password) => this.get_token(username, password)}/>}/>

                </BrowserRouter>
                <FooterItem/>
            </div>
        )
    }
}


export default App;

