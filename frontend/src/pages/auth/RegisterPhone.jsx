import { useState } from 'react'
import axios from 'axios'

export default function RegisterPhone() {
  const [email, setEmail] = useState('')
  const [phone, setPhone] = useState('')
  const [status, setStatus] = useState('')

  const submit = async (e) => {
    e.preventDefault()
    try {
      const res = await axios.post('/api/auth/register/', { email, phone })
      setStatus(`کد ارسال شد. (موک: ${res.data.mock_code || '****'})`)
    } catch (e) {
      setStatus('خطا در ارسال کد')
    }
  }

  return (
    <div style={{ maxWidth: 420, margin: '40px auto' }}>
      <h2>ثبت‌نام</h2>
      <form onSubmit={submit}>
        <label>ایمیل</label>
        <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="you@example.com" />
        <label>موبایل</label>
        <input value={phone} onChange={(e) => setPhone(e.target.value)} placeholder="09xxxxxxxxx" />
        <button type="submit">ارسال کد</button>
      </form>
      <p>{status}</p>
    </div>
  )
}