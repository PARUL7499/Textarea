import React from 'react'
import Navbar from './Components/Navbar'
import Textarea from './Components/Textarea'
import About from './pages/About '


import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";


function App() {

  const router = createBrowserRouter([
    {
      path: "/",
      element: <>  <Navbar /> <Textarea />   </>,
    },

    {
      path: "/about",
      element: <>  <Navbar /> <About />   </>,
    },
  ]);



  return (
    <>

      <RouterProvider router={router} />
    </>
  )
}

export default App
