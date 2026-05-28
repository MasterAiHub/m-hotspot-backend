# Installation Guide

## Prerequisites
- Python 3.9+
- PostgreSQL (Neon.tech recommended)
- Git

## Local Setup

1. **Clone the Repo**
   ```bash
   git clone https://github.com/MasterAihub/mhotspotbillingsystem.git
   cd mhotspotbillingsystem
   ```

2. **Backend Environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Database Migration**
   The application uses SQLAlchemy. Ensure your `DATABASE_URL` is set in `.env`.
   ```bash
   # Run migrations (if using Alembic)
   alembic upgrade head
   ```

4. **Frontend**
   The frontend is static. You can serve it using any web server or just open `frontend/index.html` in a browser (note: API calls will need the backend running).

## Environment Variables
Create a `.env` file in the `backend` directory:
```env
DATABASE_URL=postgresql+asyncpg://user:password@host/dbname
SECRET_KEY=your-super-secret-key
```
