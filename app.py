import os
import sqlite3
import random
import string
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "campus-event-board-secret-key-2026")

# Database Path Configuration
DB_DIR = os.environ.get("DB_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, "events.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create events table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        event_date TEXT NOT NULL,
        event_time TEXT NOT NULL,
        venue TEXT NOT NULL,
        organizer TEXT NOT NULL,
        capacity INTEGER NOT NULL DEFAULT 100,
        registered_count INTEGER NOT NULL DEFAULT 0,
        description TEXT,
        status TEXT NOT NULL DEFAULT 'Open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Create registrations table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registrations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_code TEXT UNIQUE NOT NULL,
        event_id INTEGER NOT NULL,
        student_name TEXT NOT NULL,
        roll_no TEXT NOT NULL,
        department TEXT NOT NULL,
        year TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT,
        registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
    )
    """)
    conn.commit()

    # Seed initial data if empty
    cursor.execute("SELECT COUNT(*) FROM events")
    count = cursor.fetchone()[0]
    if count == 0:
        seed_events = [
            (
                "CIT HackFest 2026",
                "Hackathon",
                "2026-10-25",
                "09:00 AM",
                "Auditorium & Innovation Hub",
                "Department of Information Technology",
                120,
                38,
                "A 24-hour national level hackathon focused on AI, Cloud, and Sustainable Tech solutions with exciting cash awards.",
                "Open"
            ),
            (
                "AI & Cloud DevOps Bootcamp",
                "Workshop",
                "2026-10-28",
                "10:00 AM",
                "DevOps Lab (Hall 302)",
                "IEEE Student Branch",
                60,
                45,
                "Hands-on workshop on CI/CD pipelines, Docker containerization, and Kubernetes cluster orchestration.",
                "Open"
            ),
            (
                "Dhruva Inter-Collegiate Cultural Fest",
                "Cultural",
                "2026-11-05",
                "04:00 PM",
                "Open Air Amphitheatre",
                "CIT Fine Arts Club",
                300,
                112,
                "The grand annual festival featuring music bands, western & classical dance showdowns, and celebrity performances.",
                "Open"
            ),
            (
                "National Robotics & Drone Championship",
                "Technical",
                "2026-11-12",
                "09:30 AM",
                "Mechanical Engineering Seminar Hall",
                "Robotics Association",
                80,
                80,
                "Autonomous line-follower, obstacle avoidance drone racing, and robo-soccer competitions.",
                "Closed"
            ),
            (
                "Inter-Department Badminton & Futsal Trophy",
                "Sports",
                "2026-11-18",
                "07:30 AM",
                "Indoor Sports Complex",
                "Physical Education Dept",
                100,
                24,
                "Annual sports league pitting departments across collegiate knockout rounds for the Rolling Trophy.",
                "Open"
            ),
            (
                "Industry Expert Talk: Future of Agentic AI",
                "Seminar",
                "2026-11-22",
                "02:00 PM",
                "Main Library AV Hall",
                "Industry Relations Cell",
                150,
                90,
                "Keynote address by Silicon Valley AI Architects on Large Action Models, Autonomy, and Enterprise Architectures.",
                "Open"
            )
        ]
        cursor.executemany("""
        INSERT INTO events (title, category, event_date, event_time, venue, organizer, capacity, registered_count, description, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, seed_events)
        conn.commit()
    conn.close()

# Initialize database on startup
init_db()

def generate_ticket_code():
    chars = string.ascii_uppercase + string.digits
    suffix = ''.join(random.choices(chars, k=6))
    return f"CIT-EVT-{suffix}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "campus-event-board",
        "database": "sqlite3",
        "persistent_storage": DB_PATH
    }), 200

@app.route("/api/events", methods=["GET"])
def get_events():
    category = request.args.get("category", "").strip()
    search = request.args.get("search", "").strip()
    
    conn = get_db_connection()
    query = "SELECT * FROM events WHERE 1=1"
    params = []
    
    if category and category.lower() != "all":
        query += " AND LOWER(category) = LOWER(?)"
        params.append(category)
        
    if search:
        query += " AND (LOWER(title) LIKE LOWER(?) OR LOWER(description) LIKE LOWER(?) OR LOWER(venue) LIKE LOWER(?))"
        term = f"%{search}%"
        params.extend([term, term, term])
        
    query += " ORDER BY event_date ASC, id ASC"
    cursor = conn.cursor()
    cursor.execute(query, params)
    events = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(events)

@app.route("/api/events/<int:event_id>", methods=["GET"])
def get_single_event(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events WHERE id = ?", (event_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify(dict(row))
    return jsonify({"error": "Event not found"}), 404

@app.route("/api/register", methods=["POST"])
def register_for_event():
    data = request.get_json() or {}
    
    event_id = data.get("event_id")
    student_name = data.get("student_name", "").strip()
    roll_no = data.get("roll_no", "").strip().upper()
    department = data.get("department", "").strip()
    year = data.get("year", "").strip()
    email = data.get("email", "").strip()
    phone = data.get("phone", "").strip()
    
    if not all([event_id, student_name, roll_no, department, year, email]):
        return jsonify({"success": False, "error": "All required fields must be filled"}), 400
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check event existence & capacity
    cursor.execute("SELECT * FROM events WHERE id = ?", (event_id,))
    event = cursor.fetchone()
    if not event:
        conn.close()
        return jsonify({"success": False, "error": "Event does not exist"}), 404
        
    if event["status"] != "Open":
        conn.close()
        return jsonify({"success": False, "error": "Registrations are closed for this event"}), 400
        
    if event["registered_count"] >= event["capacity"]:
        conn.close()
        return jsonify({"success": False, "error": "Event capacity is full"}), 400
        
    # Check for duplicate registration by same roll_no for this event
    cursor.execute("SELECT id FROM registrations WHERE event_id = ? AND roll_no = ?", (event_id, roll_no))
    if cursor.fetchone():
        conn.close()
        return jsonify({"success": False, "error": f"Student with Roll No {roll_no} is already registered for this event."}), 409
        
    ticket_code = generate_ticket_code()
    
    cursor.execute("""
    INSERT INTO registrations (ticket_code, event_id, student_name, roll_no, department, year, email, phone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (ticket_code, event_id, student_name, roll_no, department, year, email, phone))
    
    # Update event registered_count
    new_count = event["registered_count"] + 1
    new_status = "Closed" if new_count >= event["capacity"] else "Open"
    cursor.execute("UPDATE events SET registered_count = ?, status = ? WHERE id = ?", (new_count, new_status, event_id))
    
    conn.commit()
    conn.close()
    
    return jsonify({
        "success": True,
        "message": "Registration successful!",
        "ticket_code": ticket_code,
        "event_title": event["title"],
        "student_name": student_name,
        "roll_no": roll_no,
        "event_date": event["event_date"],
        "event_time": event["event_time"],
        "venue": event["venue"]
    }), 201

@app.route("/admin")
def admin_page():
    return render_template("admin.html")

@app.route("/api/admin/stats", methods=["GET"])
def admin_stats():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM events")
    total_events = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM events WHERE status = 'Open'")
    active_events = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM registrations")
    total_registrations = cursor.fetchone()[0]
    
    cursor.execute("SELECT SUM(capacity) FROM events")
    total_capacity = cursor.fetchone()[0] or 0
    
    conn.close()
    return jsonify({
        "total_events": total_events,
        "active_events": active_events,
        "total_registrations": total_registrations,
        "total_capacity": total_capacity
    })

@app.route("/api/admin/events", methods=["GET", "POST"])
def admin_events():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == "POST":
        data = request.get_json() or {}
        title = data.get("title", "").strip()
        category = data.get("category", "General").strip()
        event_date = data.get("event_date", "").strip()
        event_time = data.get("event_time", "").strip()
        venue = data.get("venue", "").strip()
        organizer = data.get("organizer", "").strip()
        capacity = int(data.get("capacity", 100))
        description = data.get("description", "").strip()
        
        if not all([title, category, event_date, event_time, venue, organizer]):
            conn.close()
            return jsonify({"success": False, "error": "Missing required event fields"}), 400
            
        cursor.execute("""
        INSERT INTO events (title, category, event_date, event_time, venue, organizer, capacity, registered_count, description, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?, 'Open')
        """, (title, category, event_date, event_time, venue, organizer, capacity, description))
        conn.commit()
        event_id = cursor.lastrowid
        conn.close()
        return jsonify({"success": True, "event_id": event_id, "message": "Event created successfully"}), 201
        
    cursor.execute("SELECT * FROM events ORDER BY created_at DESC")
    events = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(events)

@app.route("/api/admin/events/<int:event_id>", methods=["DELETE"])
def admin_delete_event(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
    cursor.execute("DELETE FROM registrations WHERE event_id = ?", (event_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "Event deleted successfully"})

@app.route("/api/admin/events/<int:event_id>/toggle", methods=["POST"])
def admin_toggle_event(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM events WHERE id = ?", (event_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return jsonify({"error": "Event not found"}), 404
    new_status = "Closed" if row["status"] == "Open" else "Open"
    cursor.execute("UPDATE events SET status = ? WHERE id = ?", (new_status, event_id))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "new_status": new_status})

@app.route("/api/admin/registrations", methods=["GET"])
def admin_registrations():
    event_id = request.args.get("event_id")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if event_id:
        cursor.execute("""
        SELECT r.*, e.title as event_title 
        FROM registrations r 
        JOIN events e ON r.event_id = e.id 
        WHERE r.event_id = ? 
        ORDER BY r.registered_at DESC
        """, (event_id,))
    else:
        cursor.execute("""
        SELECT r.*, e.title as event_title 
        FROM registrations r 
        JOIN events e ON r.event_id = e.id 
        ORDER BY r.registered_at DESC
        """)
        
    records = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(records)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
