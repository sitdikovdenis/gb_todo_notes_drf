
import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import axios from 'axios'


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'authors': []
       }
   }

   componentDidMount() {
   axios.get('http://127.0.0.1:8000/api/employees')
       .then(response => {
           const authors = response.data
               this.setState(
               {
                   'authors': authors
               }
           )
       }).catch(error => console.log(error))
}

   render () {
       return (
           <>
               <menu></menu>
               <div id='1'>
                   <AuthorList authors={this.state.authors} />
               </div>
               <footer></footer>
           </>
       )
   }
}


export default App;

