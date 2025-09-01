import { useState } from 'react'
import axios from 'axios'

export default function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [status, setStatus] = useState('')

  const submit = async (e) => {
    e.preventDefault()
    try {
      const res = await axios.post('/api/auth/token/', { username: email, password })
      localStorage.setItem('access', res.data.access)
      localStorage.setItem('refresh', res.data.refresh)
      setStatus('وارد شدید')
    } catch (e) {
      setStatus('ورود ناموفق')
    }
  }

  return (
    <div style={{ maxWidth: 420, margin: '40px auto' }}>
      <h2>ورود</h2>
      <form onSubmit={submit}>
        <label>ایمیل</label>
        <input value={email} onChange={(e) => setEmail(e.target.value)} />
        <label>رمز عبور</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button type="submit">ورود</button>
      </form>
      <p>{status}</p>
    </div>
  )
}