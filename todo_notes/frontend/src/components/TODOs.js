import React from 'react'


const TODOItem = ({todo}) => {
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
       </tr>
   )
}


const TODOList = ({items}) => {
   return (
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
           {items.map((item) => <TODOItem todo={item} />)}
       </table>
   )
}


export default TODOList