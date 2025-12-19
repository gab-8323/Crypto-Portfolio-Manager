# Deployment Guide - Crypto Portfolio Manager

This project is optimized for deployment on **Render** using a persistent disk for the SQLite database.

## Render Deployment (Recommended)

1. **GitHub Sync**: Push your code to a private or public GitHub repository.
2. **Create Web Service**:
   - Log in to [dashboard.render.com](https://dashboard.render.com/).
   - Click **"New +"** and select **"Web Service"**.
   - Connect your GitHub repository.
3. **Configuration**:
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. **Persistent Storage (SQLite)**:
   - Go to the **"Disks"** tab in your Render service settings.
   - Click **"Add Disk"**.
   - **Name**: `portfolio-db`
   - **Mount Path**: `/data`
   - **Size**: `1GB` (Minimum)
5. **Environment Variables**:
   - Go to the **"Env Vars"** tab.
   - Add a new variable:
     - **Key**: `DATABASE_URL`
     - **Value**: `/data/portfolio.db`

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
```
