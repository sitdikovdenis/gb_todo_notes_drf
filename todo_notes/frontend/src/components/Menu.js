import React from 'react'
import {Link} from 'react-router-dom'

const MenuItem = () => {
   return (
       <nav>
            <ul>
              <li>
                <Link to='/'>Authors</Link>
              </li>
              <li>
                <Link to='/projects'>Projects</Link>
              </li>
              <li>
                <Link to='/todos'>TODOs</Link>
              </li>
            </ul>
          </nav>
   )
}

export default MenuItem