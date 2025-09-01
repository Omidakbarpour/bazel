# Beauty Booking (Django + React)

Monorepo with `backend/` (Django + DRF) and `frontend/` (Vite + React).

## Structure
- backend/
  - core (settings, urls, wsgi)
  - users, services, specialists, bookings, payments, chat
  - requirements.txt, settings.example.env
- frontend/
  - src/pages (auth pages and home)

## Local Setup (quick)
1) Backend dependencies
- Create and activate a Python venv (Ubuntu: `sudo apt install python3-venv` then `python3 -m venv .venv && source .venv/bin/activate`)
- `pip install -r backend/requirements.txt`
- `cd backend && python manage.py migrate && python manage.py runserver 0.0.0.0:8000`

2) Frontend
- `cd frontend && npm run dev`

## API Highlights
- POST /api/auth/register/ -> send verification code (mock)
- POST /api/auth/verify-phone/ -> verify and get JWT tokens
- GET /api/services/ -> list services
- POST /api/bookings/ -> create booking (JWT required)

More to come: specialists upgrade, payments mock, chat.
