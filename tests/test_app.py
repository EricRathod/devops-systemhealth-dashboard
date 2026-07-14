import pytest

from app import create_app


@pytest.fixture
def client():
    """Create a Flask test client."""

    app = create_app(
        {
            "TESTING": True,
        }
    )

    with app.test_client() as test_client:
        yield test_client


def test_homepage_returns_success(client):
    """The homepage should load successfully."""

    response = client.get("/")

    assert response.status_code == 200
    assert b"DevOps System Health Dashboard" in response.data


def test_health_endpoint(client):
    """The health endpoint should return healthy status."""

    response = client.get("/health")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "healthy"
    assert data["service"] == "devops-system-health-dashboard"


def test_application_info_endpoint(client):
    """The information endpoint should return app details."""

    response = client.get("/api/info")
    data = response.get_json()

    assert response.status_code == 200
    assert data["application"] == "DevOps System Health Dashboard"
    assert data["version"] == "1.0.0"
    assert data["environment"] == "development"


def test_unknown_route_returns_404(client):
    """An unknown route should return a JSON 404 response."""

    response = client.get("/does-not-exist")
    data = response.get_json()

    assert response.status_code == 404
    assert data["error"] == "Not Found"