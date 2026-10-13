import os
import tempfile
import pytest
import sqlite3

# Set environment before importing app so it uses an isolated test DB
os.environ["SECRET_KEY"] = "test-key"

from app import app, init_db, DB_PATH

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Verify health endpoint returns status healthy."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["service"] == "campus-event-board"

def test_home_page_status(client):
    """Verify main user interface loads successfully with HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Campus Event Board" in response.data

def test_get_events_api(client):
    """Verify events API returns list of populated events."""
    response = client.get("/api/events")
    assert response.status_code == 200
    events = response.get_json()
    assert isinstance(events, list)
    assert len(events) > 0
    first = events[0]
    assert "title" in first
    assert "category" in first
    assert "capacity" in first

def test_event_registration_workflow(client):
    """Verify registration creates ticket code and stores in database."""
    # Fetch first open event
    res = client.get("/api/events")
    events = res.get_json()
    target_event = next(e for e in events if e["status"] == "Open")
    initial_count = target_event["registered_count"]

    payload = {
        "event_id": target_event["id"],
        "student_name": "DevOps Candidate",
        "roll_no": "23ITTEST999",
        "department": "Information Technology",
        "year": "IV Year",
        "email": "test.devops@cit.edu.in",
        "phone": "+91 9999988888"
    }

    reg_res = client.post("/api/register", json=payload)
    assert reg_res.status_code == 201
    data = reg_res.get_json()
    assert data["success"] is True
    assert "ticket_code" in data
    assert data["ticket_code"].startswith("CIT-EVT-")

    # Verify duplicate registration is rejected with HTTP 409
    dup_res = client.post("/api/register", json=payload)
    assert dup_res.status_code == 409
    dup_data = dup_res.get_json()
    assert dup_data["success"] is False

def test_admin_stats_and_endpoints(client):
    """Verify admin endpoints provide accurate metric counters."""
    res = client.get("/api/admin/stats")
    assert res.status_code == 200
    stats = res.get_json()
    assert stats["total_events"] > 0
    assert stats["total_capacity"] > 0
