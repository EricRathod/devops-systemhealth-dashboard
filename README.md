# 🚀 DevOps System Health Dashboard

![CI](https://github.com/EricRathod/devops-systemhealth-dashboard/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![Render](https://img.shields.io/badge/Render-Live-46E3B7)
![License](https://img.shields.io/badge/License-MIT-green)

A Dockerized Flask web application that demonstrates modern DevOps practices including containerization, automated testing, Continuous Integration (CI), and cloud deployment.

---

# 🌐 Live Demo

### 🔗 https://devops-systemhealth-dashboard.onrender.com/

> **Note:** This application is hosted on Render's free tier. The first request after inactivity may take **30–60 seconds** while the service starts.

---

# 📖 Overview

The **DevOps System Health Dashboard** is a lightweight monitoring application that displays system health and application information through a clean web dashboard and REST APIs.

The project was built to demonstrate a complete DevOps workflow, from local development to automated testing, containerization, continuous integration, and cloud deployment.

---

# ✨ Features

- Interactive System Health Dashboard
- REST API Endpoints
- Health Check Endpoint
- Application Information Endpoint
- Environment-Based Configuration
- Docker Containerization
- Docker Compose Support
- Automated Testing with Pytest
- GitHub Actions CI Pipeline
- Gunicorn Production Server
- Live Deployment on Render

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.12 |
| Framework | Flask |
| Production Server | Gunicorn |
| Containerization | Docker |
| Container Management | Docker Compose |
| CI/CD | GitHub Actions |
| Cloud Hosting | Render |
| Testing | Pytest |
| Frontend | HTML, CSS |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
devops-systemhealth-dashboard/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docs/
│   └── screenshots/
│       ├── dashboard.png
│       ├── docker-compose.png
│       └── github-actions.png
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── tests/
│   ├── __init__.py
│   └── test_app.py
│
├── .dockerignore
├── .gitignore
├── app.py
├── config.py
├── compose.yml
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 🏗️ Runtime Architecture

```text
              Browser
                  │
                  ▼
       Render Cloud Platform
                  │
                  ▼
         Docker Container
                  │
                  ▼
             Gunicorn
                  │
                  ▼
          Flask Application
```

---

# 🔄 CI/CD Workflow

```text
Developer
    │
git push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Install Dependencies
    ├── Run Pytest
    └── Build Docker Image
    │
    ▼
Render Auto Deployment
    │
    ▼
Live Application
```

---

# 🌐 REST API

## Health Check

```http
GET /health
```

Example Response

```json
{
  "status": "healthy"
}
```

---

## Application Information

```http
GET /api/info
```

Example Response

```json
{
  "application": "DevOps System Health Dashboard",
  "version": "1.0.0",
  "environment": "production",
  "python_version": "3.12.x",
  "operating_system": "Linux"
}
```

---

# 🚀 Running Locally

## Clone the Repository

```bash
git clone https://github.com/EricRathod/devops-systemhealth-dashboard.git
cd devops-systemhealth-dashboard
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

# 🐳 Docker

### Build Image

```bash
docker build -t devops-dashboard .
```

### Run Container

```bash
docker run -p 5000:5000 devops-dashboard
```

---

# 🐳 Docker Compose

### Start

```bash
docker compose up --build
```

### Run in Background

```bash
docker compose up -d
```

### Stop

```bash
docker compose down
```

---

# 🧪 Running Tests

```bash
pytest -v
```

---

# ☁️ Deployment

This application is deployed on **Render** using Docker.

Deployment workflow:

1. Push changes to the **main** branch.
2. GitHub Actions automatically:
   - Installs dependencies
   - Runs automated tests
   - Builds the Docker image
3. Render automatically deploys the latest version.

Live URL:

**https://devops-systemhealth-dashboard.onrender.com/**

---

# 📸 Project Screenshots

## Dashboard

![Dashboard](docs/screenshots/dashboard.png)

---

## GitHub Actions CI Pipeline

![GitHub Actions](docs/screenshots/github-actions.png)

---

## Docker Compose

![Docker Compose](docs/screenshots/docker-compose.png)

---

# 🚀 Future Improvements

- Deploy on AWS EC2
- Kubernetes (K8s)
- Terraform Infrastructure as Code
- Prometheus & Grafana Monitoring
- Nginx Reverse Proxy
- Custom Domain with HTTPS
- Centralized Logging (ELK Stack)

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Eric Rathod**

Master of Artificial Intelligence – Design and Development  
Seneca Polytechnic

- **GitHub:** https://github.com/EricRathod
- **LinkedIn:** *(Add your LinkedIn profile URL)*

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
