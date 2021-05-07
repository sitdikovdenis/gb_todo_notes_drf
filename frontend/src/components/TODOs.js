import React from 'react'
import {Link} from "react-router-dom";


const TODOItem = ({todo, deleteTODO}) => {
   return (
       <tr>
           <td>
               {todo.text}
           </td>
           <td>
               {todo.created_at}
           </td>
           <td>
               {todo.state}
           </td>
           <td>
               {todo.author}
           </td>
            <td>
                <button onClick={() => deleteTODO(todo.uuid)} type='button'>Delete</button>
            </td>
       </tr>
   )
}


const TODOList = ({items, deleteTODO}) => {
   return (
       <div>
       <table>
           <th>
               Текст
           </th>
           <th>
               Дата создания
           </th>
           <th>
               Состояние
           </th>
           <th>
               Автор
           </th>
           <th>
           </th>
           {items.map((item) => <TODOItem todo={item} deleteTODO={deleteTODO}/>)}
       </table>
            <Link to='/todos/create'>Create</Link>
        </div>
   )
}


export default TODOList