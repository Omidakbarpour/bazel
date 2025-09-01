import { useState } from 'react'
import axios from 'axios'

export default function VerifyCode() {
  const [phone, setPhone] = useState('')
  const [code, setCode] = useState('')
  const [status, setStatus] = useState('')

  const submit = async (e) => {
    e.preventDefault()
    try {
      const res = await axios.post('/api/auth/verify-phone/', { phone, code })
      localStorage.setItem('access', res.data.access)
      localStorage.setItem('refresh', res.data.refresh)
      setStatus('تأیید شد و وارد شدید')
    } catch (e) {
      setStatus('کد نامعتبر است')
    }
  }

  return (
    <div style={{ maxWidth: 420, margin: '40px auto' }}>
      <h2>تأیید کد</h2>
      <form onSubmit={submit}>
        <label>موبایل</label>
        <input value={phone} onChange={(e) => setPhone(e.target.value)} placeholder="09xxxxxxxxx" />
        <label>کد</label>
        <input value={code} onChange={(e) => setCode(e.target.value)} placeholder="123456" />
        <button type="submit">تأیید</button>
      </form>
      <p>{status}</p>
    </div>
  )
}