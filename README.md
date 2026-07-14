# 🚀 DevOps System Health Dashboard

A production-ready Flask application demonstrating modern DevOps practices including Docker, Docker Compose, GitHub Actions CI, automated testing, and Gunicorn deployment.

---

## 📖 Overview

The DevOps System Health Dashboard is a lightweight web application that displays application health and environment information through a clean dashboard and REST APIs.

This project was built to demonstrate fundamental DevOps concepts such as containerization, continuous integration, automated testing, configuration management, and production deployment using industry-standard tools.

---

## ✨ Features

- ✅ Interactive System Health Dashboard
- ✅ REST API Endpoints
- ✅ Application Health Monitoring
- ✅ Environment Configuration
- ✅ Docker Containerization
- ✅ Docker Compose Support
- ✅ GitHub Actions CI Pipeline
- ✅ Automated Testing with Pytest
- ✅ Gunicorn Production Server
- ✅ Configuration Management using Environment Variables

---

## 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.12 |
| Framework | Flask |
| Production Server | Gunicorn |
| Containerization | Docker |
| Container Orchestration | Docker Compose |
| CI/CD | GitHub Actions |
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
├── compose.yml
├── config.py
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 🏗 Architecture

```text
                 Browser
                    │
                    ▼
            Gunicorn Server
                    │
                    ▼
             Flask Application
                    │
                    ▼
          Docker Container
                    │
                    ▼
          Docker Compose
                    │
                    ▼
      GitHub Actions CI Pipeline
```

---

# 🌐 API Endpoints

## Health Check

```
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

```
GET /api/info
```

Example Response

```json
{
    "app_name": "DevOps System Health Dashboard",
    "version": "1.0.0",
    "environment": "production"
}
```

---

# ⚙️ Running Locally

## Clone Repository

```bash
git clone https://github.com/EricRathod/devops-systemhealth-dashboard.git
```

```bash
cd devops-systemhealth-dashboard
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Application will be available at:

```
http://localhost:5000
```

---

# 🐳 Docker

## Build Image

```bash
docker build -t devops-dashboard .
```

## Run Container

```bash
docker run -p 5000:5000 devops-dashboard
```

---

# 🐳 Docker Compose

## Build and Start

```bash
docker compose up --build
```

## Run in Background

```bash
docker compose up -d
```

## Stop

```bash
docker compose down
```

---

# 🔄 Continuous Integration

GitHub Actions automatically performs the following tasks whenever code is pushed to the **main** branch:

- Checkout Repository
- Install Python
- Install Dependencies
- Run Automated Tests
- Build Docker Image

This ensures that every code change is automatically validated before deployment.

---

# 🧪 Running Tests

```bash
pytest -v
```

---

# 📸 Project Screenshots

### Dashboard

> *(Add dashboard screenshot here)*

---

### GitHub Actions CI

> *(Add GitHub Actions screenshot here)*

---

### Docker Compose

> *(Add Docker Compose screenshot here)*

---

# 🚀 Future Improvements

- Kubernetes Deployment
- AWS EC2 Deployment
- Terraform Infrastructure as Code
- Prometheus Monitoring
- Grafana Dashboard
- Nginx Reverse Proxy
- HTTPS with SSL

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Eric Rathod**

Master of Artificial Intelligence – Design and Development

Seneca Polytechnic

GitHub: https://github.com/EricRathod

---

## ⭐ If you found this project helpful, consider giving it a star!
