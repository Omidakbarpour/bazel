import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div style={{ padding: 24 }}>
      <h2>رزرو خدمات آرایشگری</h2>
      <nav style={{ display: 'flex', gap: 12 }}>
        <Link to="/auth/register">ثبت‌نام</Link>
        <Link to="/auth/verify">تأیید کد</Link>
        <Link to="/auth/login">ورود</Link>
      </nav>
      <p>این یک نسخه اولیه از فرانت‌اند است.</p>
    </div>
  )
}