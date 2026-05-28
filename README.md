# M Hotspot Billing System

A professional, scalable, and modern hotspot management platform built with FastAPI and Neon PostgreSQL.

## Features

- **Voucher System**: Generate, redeem, and manage WiFi vouchers.
- **Plan Management**: Tiered pricing and speed limits.
- **Admin Dashboard**: Real-time analytics and user management.
- **Reseller Portal**: Dedicated interface for voucher resellers.
- **Modern UI**: Responsive, glassmorphism-inspired frontend.

## Tech Stack

- **Backend**: Python FastAPI
- **Database**: PostgreSQL (Neon)
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Render

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/MasterAihub/mhotspotbillingsystem.git
   ```

2. Backend setup:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Configure environment variables in `.env`:
   ```env
   DATABASE_URL=your_neon_postgres_url
   SECRET_KEY=your_secret_key
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Deployment

This project is configured for easy deployment on **Render**. Simply connect your GitHub repository and Render will use the `render.yaml` configuration to set up the backend and static frontend.

## License

MIT
