import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import App from './App.jsx'
import RegisterPhone from './pages/auth/RegisterPhone.jsx'
import VerifyCode from './pages/auth/VerifyCode.jsx'
import Login from './pages/auth/Login.jsx'
import Home from './pages/Home.jsx'

const router = createBrowserRouter([
  { path: '/', element: <Home /> },
  { path: '/auth/register', element: <RegisterPhone /> },
  { path: '/auth/verify', element: <VerifyCode /> },
  { path: '/auth/login', element: <Login /> },
  { path: '/app', element: <App /> },
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
