# COIMBATORE INSTITUTE OF TECHNOLOGY
*(Government Aided Autonomous Institution Affiliated to Anna University)*
### 23IT723 – DEVOPS LABORATORY
## FINAL MINI PROJECT REPORT
# CAMPUS EVENT BOARD

**OCTOBER 2026**

---

### Submitted by:
**2303717620522022 — JAYASREE R**  
*(or Candidate Name / Register Number)*  
Department of Information Technology  
Coimbatore Institute of Technology, Coimbatore – 641 014  

---

<div style="page-break-after: always;"></div>

# COIMBATORE INSTITUTE OF TECHNOLOGY
*(Government Aided Autonomous Institution Affiliated to Anna University)*

## BONAFIDE CERTIFICATE

Certified that this project report titled **“CAMPUS EVENT BOARD”** is the bonafide work of **2303717620522022 - JAYASREE R** completed during the academic year **2025-2026-Semester VII** for the project presentation of **23IT723 - DEVOPS LABORATORY** under our supervision.

Certified that the candidate was examined by using the project work examination.

### Review Members:
1. **Dr. M. Sangeetha**
2. **Dr. E. Arul**

<div style="page-break-after: always;"></div>

# 23IT723 – DEVOPS LABORATORY
## FINAL MINI PROJECT – EVALUATION SCHEME

### Final Mini Project Assessment
The final mini project requires students to integrate the major DevOps practices covered in the laboratory. The project demonstrates practical implementation of version control, collaborative development, Continuous Integration, containerization and automated configuration/provisioning, with execution evidence.

| S.No. | Evaluation Component | Key Verification Points | Marks |
| :---: | :--- | :--- | :---: |
| 1 | **Problem Definition & Project Planning** | Problem statement, objectives, requirements, scope, module identification, technology selection and workflow planning. | 10 |
| 2 | **Git Repository & Version Control** | Repository creation, meaningful commits, README, .gitignore, remote repository, push/pull/fetch operations and commit history. | 15 |
| 3 | **Branching, Merging & Collaboration** | Feature branches, parallel development, merging, conflict handling, branch organization and collaborative workflow. | 10 |
| 4 | **Application Development & Build** | Working application/source code, project structure, dependency management, build configuration and successful execution. | 15 |
| 5 | **Jenkins Continuous Integration** | Jenkins configuration, source-code integration, automated checkout, build job/pipeline, build execution and console verification. | 15 |
| 6 | **Docker / Containerization** | Dockerfile, image creation, container execution, port/configuration handling, application deployment and container verification. | 10 |
| 7 | **Automation / Configuration Management** | Ansible/Chef/Puppet/SaltStack or equivalent automation where applicable; repeatable configuration/provisioning and successful execution. | 5 |
| 8 | **Testing & Verification** | Functional testing, build verification, error identification, test evidence and corrective action. | 5 |
| 9 | **Documentation & Technical Presentation** | Architecture/workflow diagram, commands/configuration, screenshots, results, troubleshooting, conclusion and repository details. | 5 |
| 10 | **Final Demonstration & Viva-Voce** | Live demonstration, explanation of implementation, troubleshooting responses and technical understanding. | 10 |
| | **TOTAL** | | **100** |

---

### Minimum Evidence to be Submitted:
- Project repository URL and project README.
- Git commit history and branch/merge evidence.
- Jenkins job/pipeline configuration and successful build evidence.
- Dockerfile, image, and running container evidence where Docker is used.
- Automation/configuration scripts (Ansible playbook).
- Application execution and testing evidence.
- Architecture and workflow diagrams.
- Short technical report containing implementation steps, results, and troubleshooting.
- Live demonstration of the complete DevOps workflow.

<div style="page-break-after: always;"></div>

# TABLE OF CONTENTS

| S. NO. | CONTENT |
| :---: | :--- |
| 1 | INTRODUCTION |
| 2 | OBJECTIVES |
| 3 | ABSTRACT |
| 4 | TECHNOLOGY STACK |
| 5 | SYSTEM ARCHITECTURE |
| 6 | MODULE 1 — USER INTERFACE & EVENT DISCOVERY |
| 7 | MODULE 2 — FLASK BACKEND & REGISTRATION MANAGEMENT |
| 8 | MODULE 3 — SQLITE DATABASE MANAGEMENT |
| 9 | MODULE 4 — GIT & GITHUB SOURCE CONTROL |
| 10 | MODULE 5 — DOCKER CONTAINERIZATION |
| 11 | MODULE 6 — JENKINS CI/CD PIPELINE |
| 12 | MODULE 7 — AUTOMATED TESTING |
| 13 | MODULE 8 — ANSIBLE DEPLOYMENT |
| 14 | MODULE 9 — PERSISTENT STORAGE |
| 15 | MODULE 10 — ADMIN & EVENT MANAGEMENT |
| 16 | MODULE 11 — CI/CD INTEGRATION |
| 17 | MODULE 12 — APPLICATION & DEPLOYMENT VERIFICATION |
| 18 | RESULTS AND OUTPUT |
| 19 | COMMANDS USED |
| 20 | ADVANTAGES |
| 21 | LIMITATIONS |
| 22 | FUTURE ENHANCEMENTS |
| 23 | CONCLUSION |

<div style="page-break-after: always;"></div>

---

## 1. INTRODUCTION

The **Campus Event Board** is a web-based event coordination, discovery, and student registration management platform designed to solve information fragmentation across college departments and clubs. In a bustling academic campus like Coimbatore Institute of Technology, students often miss out on inter-collegiate hackathons, technical paper symposiums, cultural nights, sports tournaments, and faculty guest seminars because event posters remain scattered across physical notice boards, email threads, or disparate chat groups.

The Campus Event Board provides an interactive, centralized digital portal where students can search, filter by category, explore event venues and timings, and register with one click to obtain instant digital event entry passes. Furthermore, an administrative console provides faculty organizers and student coordinators with real-time analytics on registrations, capacity limits, and attendee roster management.

The application is engineered using HTML5, modern CSS3 with dark mode theme design tokens, JavaScript ES6+, Python, Flask, and SQLite. Flask handles application logic and RESTful API endpoints, while SQLite stores relational event and attendee data.

Crucially, the project integrates modern industry DevOps automation practices throughout the entire software delivery lifecycle:
- **Git and GitHub** manage version control and collaborative branching.
- **Jenkins** automates continuous integration and triggers tests and deployments.
- **Docker** packages the Flask application into lightweight, consistent containers.
- **Pytest** performs automated test execution to block regressions before deployment.
- **Ansible** automates container deployment, networking, and restart policies.
- **Docker Volumes** (`eventboard_data`) provide persistence for the SQLite database so attendee registrations persist through updates.

---

## 2. OBJECTIVES

- To develop a user-friendly digital campus event hub enabling students to browse, filter, search, and register for co-curricular and extracurricular events.
- To eliminate manual sign-up sheets and provide unique digital event passes (`CIT-EVT-XXXXXX`) for entrance verification.
- To provide an administrative console for college staff to publish events, track capacity progress, and export attendee rosters.
- To implement Git version control with structured feature branching and commit tracking.
- To automate Continuous Integration (CI) using Jenkins pipelines that automatically fetch source code, build Docker images, and execute unit tests.
- To containerize the application using Docker for deterministic execution across environments.
- To integrate Pytest automated test scripts to ensure API health and business logic validity before deployment.
- To automate deployment and configuration management using Ansible playbooks.
- To ensure database persistence using Docker Volumes (`eventboard_data`) mounted to `/app/data`, preventing data loss across container lifecycles.

---

## 3. ABSTRACT

The **Campus Event Board** addresses the challenges of manual event scheduling, disconnected student communication, and fragmented registrations in collegiate environments. The system delivers a responsive web platform where students browse events categorized into Hackathons, Workshops, Cultural, Technical, Sports, and Seminars. Students register with their student credentials and instantly receive a digital entry pass. Administrators monitor capacity, toggle registrations, and view student attendee rosters.

The application is built using HTML5, CSS3, JavaScript, Python 3.11, Flask, and SQLite. To fulfill the DevOps Laboratory syllabus objectives, the software incorporates end-to-end automation. Git and GitHub govern version control. Jenkins serves as the CI/CD pipeline engine. Docker packages the application into the `campus-event-ci` image. Pytest conducts automated test verification. Ansible configures the deployment on the target host by deploying container `campus-event-ansible` on port 5001. A Docker volume named `eventboard_data` is mounted to `/app/data` to ensure persistent storage for `events.db`.

The end-to-end delivery workflow follows:
$$\text{GitHub} \longrightarrow \text{Jenkins} \longrightarrow \text{Docker Build} \longrightarrow \text{Pytest} \longrightarrow \text{Ansible} \longrightarrow \text{Docker Container} \longrightarrow \text{Flask} \longrightarrow \text{SQLite (Volume Persistent)}$$
This satisfies all DevOps laboratory verification criteria with demonstrable working evidence.

---

## 4. TECHNOLOGY STACK

| Technology | Version | Purpose |
| :--- | :--- | :--- |
| **HTML** | HTML5 | Semantic structure for public and admin web portals |
| **CSS** | CSS3 | Dark-themed design system, cards, glassmorphic banners, progress meters |
| **JavaScript** | ES6+ | Real-time DOM updates, dynamic search, modals, local ticket caching |
| **Icons** | Font Awesome 6.5.1 | Consistent iconography across navigation, badges, and action triggers |
| **Python** | 3.11 / 3.14 | Backend programming language |
| **Flask** | 3.1.x | Lightweight backend web server and REST API framework |
| **SQLite** | 3.x | Relational database engine for event listings and registrations |
| **Git** | 2.x | Distributed version control system |
| **GitHub** | Cloud | Remote centralized Git repository hosting |
| **Jenkins** | 2.541.x | Continuous integration and deployment orchestration |
| **Docker** | 28.x | Application containerization and image creation |
| **Pytest** | 8.x / 9.x | Automated functional and endpoint unit testing |
| **Ansible** | 2.10+ | Configuration management and container deployment automation |
| **community.docker** | 1.2+ / 2.x | Ansible collection for managing Docker containers & volumes |

---

## 5. SYSTEM ARCHITECTURE

```
+-----------------------------------------------------------------------------------+
|                        CAMPUS EVENT BOARD - DEVOPS ARCHITECTURE                    |
+-----------------------------------------------------------------------------------+

[ Developer ] --(git commit/push)--> [ GitHub Repository ]
                                            |
                                            v (Webhook / Poll SCM)
                                    [ Jenkins CI Engine ]
                                            |
                           +----------------+----------------+
                           |                                 |
                     1. Docker Build                   2. Pytest Execution
                 (campus-event-ci image)             (inside container / runner)
                           |                                 |
                           +----------------+----------------+
                                            |
                                            v (Trigger Deploy Stage)
                                    [ Ansible Engine ]
                                (inventory.ini + docker-deploy.yml)
                                            |
                                            v
                                 [ Docker Runtime Host ]
                                            |
                      +---------------------+---------------------+
                      |                                           |
           [ Container: campus-event-ansible ]            [ Docker Volume ]
           - Port: 5001 -> 5000                           - eventboard_data
           - Flask App (Python 3.11)                              |
           - REST APIs & Jinja2 Templates                         v
                      |                               [ /app/data/events.db ]
                      +-------------------------------------------+
                      |
        +-------------+-------------+
        |                           |
  [ Student View ]            [ Admin View ]
  http://localhost:5001       http://localhost:5001/admin
```

### Architectural Workflow Steps:
1. **Development**: Developer designs features (UI layout, registration logic, admin dashboard).
2. **Source Control Management**: Code commits, branches, and `.gitignore` managed locally via Git.
3. **GitHub Remote Sync**: Source code pushed to GitHub repository for centralized tracking.
4. **Jenkins Pipeline Trigger**: Jenkins detects changes and initiates the multi-stage declarative pipeline.
5. **Docker Container Build**: Jenkins compiles the application into Docker image `campus-event-ci`.
6. **Automated Testing**: Jenkins runs `pytest test_app.py` inside the container image; failures halt the build immediately.
7. **Ansible Deployment Execution**: Upon test pass, Jenkins invokes the Ansible playbook (`docker-deploy.yml`).
8. **Container Configuration**: Ansible provisions container `campus-event-ansible`, configures port forwarding `5001:5000`, and attaches volume `eventboard_data`.
9. **Data Persistence**: The SQLite database stored at `/app/data/events.db` persists indefinitely even across container upgrades and restarts.
10. **Application Access**: Users interact with the live portal at `http://localhost:5001`.

---

## 6. MODULE 1 — USER INTERFACE & EVENT DISCOVERY

This module provides the student-facing user interface of the Campus Event Board application. It provides an intuitive, high-performance portal for discovering upcoming college events.

### Main Features:
- **Curated Event Cards**: Displays title, category, date, time, venue, organizer, description, and available capacity.
- **Instant Search**: Real-time filtering by keywords, event titles, faculty coordinators, and hall locations.
- **Category Filter Chips**: Fast switching between Hackathons, Workshops, Cultural Fests, Technical symposiums, Sports, and Seminars.
- **Seat Capacity Meter**: Visual progress indicator displaying booked seats vs total hall capacity.
- **Event Registration Modal**: Streamlined form collecting Student Name, Register Number, Department, Year of Study, College Email, and Contact Number.
- **Digital Event Pass Modal**: Automatically generates a unique ticket voucher (`CIT-EVT-XXXXXX`) that students can view, save, or print.
- **Offline / Local Pass Storage**: Allows students to review previously booked passes locally on their device.
- **Responsive Layout**: Fluidly adapts across mobile phones, tablets, and desktop workstations.

**Technologies**: HTML5, Modern CSS3 (Dark Mode & CSS Variables), JavaScript ES6+, Font Awesome 6.

---

## 7. MODULE 2 — FLASK BACKEND & REGISTRATION MANAGEMENT

This module powers the core business logic, API endpoints, and database interactions of the Campus Event Board. Flask receives HTTP requests from the frontend and communicates with SQLite.

### Main Functions:
- Serves dynamic HTML pages using Flask's Jinja2 templating engine.
- Exposes RESTful endpoints:
  - `GET /` — Serves home interface.
  - `GET /api/events` — Returns event records with optional category and search filters.
  - `GET /api/events/<id>` — Returns single event metadata.
  - `POST /api/register` — Validates student inputs, verifies hall capacity, checks for duplicate roll number registrations, inserts ticket record, and updates seat counter.
  - `GET /health` — Provides microservice health status for Docker and Jenkins health checks.
- Generates cryptographically pseudorandom alphanumeric ticket identifiers (`CIT-EVT-[A-Z0-9]{6}`).
- Handles error states with proper HTTP status codes (`400 Bad Request`, `404 Not Found`, `409 Conflict`).

**Technology**: Python 3.11 with Flask 3.1.x.

---

## 8. MODULE 3 — SQLITE DATABASE MANAGEMENT

This module handles persistent relational storage for events and student registrations using SQLite.

### Database Schema:
1. **`events` Table**:
   - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
   - `title` (TEXT NOT NULL)
   - `category` (TEXT NOT NULL)
   - `event_date` (TEXT NOT NULL)
   - `event_time` (TEXT NOT NULL)
   - `venue` (TEXT NOT NULL)
   - `organizer` (TEXT NOT NULL)
   - `capacity` (INTEGER NOT NULL DEFAULT 100)
   - `registered_count` (INTEGER NOT NULL DEFAULT 0)
   - `description` (TEXT)
   - `status` (TEXT NOT NULL DEFAULT 'Open')
   - `created_at` (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)

2. **`registrations` Table**:
   - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
   - `ticket_code` (TEXT UNIQUE NOT NULL)
   - `event_id` (INTEGER NOT NULL, FOREIGN KEY REFERENCES events(id))
   - `student_name` (TEXT NOT NULL)
   - `roll_no` (TEXT NOT NULL)
   - `department` (TEXT NOT NULL)
   - `year` (TEXT NOT NULL)
   - `email` (TEXT NOT NULL)
   - `phone` (TEXT)
   - `registered_at` (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)

### Database File Location:
- Host path / volume: `data/events.db`
- Inside Docker container: `/app/data/events.db`

---

## 9. MODULE 4 — GIT & GITHUB SOURCE CONTROL

This module manages project source code, branch organization, and version tracking.

### Core Repository Files:
- `app.py` — Flask backend application
- `test_app.py` — Automated Pytest test suite
- `requirements.txt` — Python dependencies
- `Dockerfile` — Container build definition
- `docker-compose.yml` — Multi-container orchestration specification
- `Jenkinsfile` — Declarative CI/CD pipeline script
- `ansible/inventory.ini` — Ansible target host definitions
- `ansible/docker-deploy.yml` — Ansible container provisioning playbook
- `ansible/ansible.cfg` — Ansible configuration settings
- `static/css/style.css` — Centralized theme styling
- `static/js/app.js` — Client side application logic
- `templates/index.html` — Public event board template
- `templates/admin.html` — Administrative dashboard template
- `.gitignore` — Ignore virtual environments, caches, and temporary files

---

## 10. MODULE 5 — DOCKER CONTAINERIZATION

Docker packages the Campus Event Board application, runtime dependencies, and configuration into an immutable, portable Docker container.

### Docker Configuration Summary:
- **Base Image**: `python:3.11-slim`
- **Working Directory**: `/app`
- **Exposed Port**: `5000`
- **Volume Mount**: `/app/data`
- **Built Image Tag**: `campus-event-ci`
- **Deployed Container Name**: `campus-event-ansible`
- **Host Port Mapping**: `5001:5000`
- **Application URL**: `http://localhost:5001`

---

## 11. MODULE 6 — JENKINS CI/CD PIPELINE

Jenkins provides complete build, test, and continuous deployment automation.

### Pipeline Stages in `Jenkinsfile`:
1. **Checkout SCM**: Checks out the latest commit from the Git repository.
2. **Build Docker Image**: Executes `docker build -t campus-event-ci .`.
3. **Run Automated Tests**: Executes `docker run --rm campus-event-ci python -m pytest test_app.py -v`.
4. **Deploy with Ansible**: Invokes `ansible-playbook -i ansible/inventory.ini ansible/docker-deploy.yml` (or via `ansible-docker-lab`).
5. **Verify Deployment Health**: Validates container status and tests `curl http://localhost:5001/health`.

---

## 12. MODULE 7 — AUTOMATED TESTING

Pytest validates application health, API endpoints, registration rules, duplicate prevention, and administrative statistics before any deployment occurs.

### Test Cases in `test_app.py`:
- `test_health_check`: Confirms microservice status returns `healthy` with HTTP 200.
- `test_home_page_status`: Confirms landing page loads and template contains brand titles.
- `test_get_events_api`: Asserts `/api/events` returns list of active events with proper schema.
- `test_event_registration_workflow`: Validates full registration lifecycle, ticket generation, count incrementation, and duplicate prevention.
- `test_admin_stats_and_endpoints`: Verifies admin metrics calculate correct totals.

**Execution Command**:
```bash
python -m pytest test_app.py -v
```
**Result**: 5 passed in 0.30s (100% success).

---

## 13. MODULE 8 — ANSIBLE DEPLOYMENT

Ansible automates deployment, container state management, volume mounting, and networking policies through an idempotent playbook (`docker-deploy.yml`).

### Ansible Task Configuration:
- Module: `community.docker.docker_container`
- Container Name: `campus-event-ansible`
- Image: `campus-event-ci`
- State: `started`
- Restart Policy: `unless-stopped`
- Port Mapping: `"5001:5000"`
- Volume Mount: `"eventboard_data:/app/data"`

---

## 14. MODULE 9 — PERSISTENT STORAGE

A dedicated Docker Volume named `eventboard_data` is mounted to `/app/data`. This guarantees that SQLite database files (`events.db`) survive across:
- Container updates
- Container restarts
- Image rebuilds in CI/CD pipelines

**Verification Command**:
```bash
docker volume inspect eventboard_data
```

---

## 15. MODULE 10 — ADMIN & EVENT MANAGEMENT

This module provides administrators, club convenors, and faculty evaluators with centralized oversight.

### Admin Capabilities:
- View live aggregate statistics: Total Events, Active Events, Total Student RSVPs, Campus Capacity.
- Add new events with customizable date, venue, category, and capacity.
- Toggle event availability (`Open` vs `Closed`).
- Delete obsolete event records.
- View real-time attendee table with search filtering by roll number or student name.
- Export student attendee roster to CSV format.

**Admin URL**: `http://localhost:5001/admin`

---

## 16. MODULE 11 — CI/CD INTEGRATION

The pipeline binds Git, Jenkins, Docker, Pytest, and Ansible into an unbroken automation chain. Changes committed to GitHub automatically trigger automated builds, run tests in an isolated container, and update the deployed container without manual human intervention.

---

## 17. MODULE 12 — APPLICATION & DEPLOYMENT VERIFICATION

Post-deployment verification includes:
- Checking container status: `docker ps`
- Verifying container logs: `docker logs campus-event-ansible`
- Confirming HTTP endpoint availability at port `5001`
- Confirming database schema and records inside container
- Confirming volume persistence after stopping and recreating container

---

## 18. RESULTS AND OUTPUT

The implemented system successfully delivers:
- Interactive campus event browsing with real-time category filtering.
- Full keyword search across events and venues.
- Seamless student registration with automated ticket code generation (`CIT-EVT-XXXXXX`).
- Administrative dashboard with attendee rosters and CSV export.
- Reliable SQLite relational storage with Docker volume persistence.
- Complete containerization using Docker.
- 100% automated test pass rate with Pytest.
- Automated CI/CD pipeline via Jenkins.
- Idempotent configuration management and deployment via Ansible.

---

## 19. COMMANDS USED

### 1. Docker Commands
```bash
# Check running containers
docker ps

# Check all containers
docker ps -a

# Build Docker image
docker build -t campus-event-ci .

# Run container with persistent volume
docker run -d --name campus-event-ansible --restart unless-stopped -p 5001:5000 -v eventboard_data:/app/data campus-event-ci

# View container logs
docker logs campus-event-ansible

# Check Docker volumes
docker volume ls
docker volume inspect eventboard_data
```

### 2. Automated Testing Commands
```bash
# Run pytest directly
python -m pytest test_app.py -v

# Run pytest inside Docker image
docker run --rm campus-event-ci python -m pytest test_app.py -v
```

### 3. Ansible Commands
```bash
# Run playbook directly
ansible-playbook -i ansible/inventory.ini ansible/docker-deploy.yml

# Run inside Ansible control container
docker exec ansible-docker-lab ansible-playbook -i /inventory.ini /docker-deploy.yml
```

### 4. SQLite Database Verification Commands
```bash
# Display tables inside running container
docker exec campus-event-ansible python -c "import sqlite3; c=sqlite3.connect('/app/data/events.db'); print(c.execute(\"SELECT name FROM sqlite_master WHERE type='table'\").fetchall()); c.close()"

# Display stored event records
docker exec campus-event-ansible python -c "import sqlite3; c=sqlite3.connect('/app/data/events.db'); [print(row) for row in c.execute('SELECT id, title, registered_count, capacity, status FROM events')]; c.close()"

# Display registered student attendees
docker exec campus-event-ansible python -c "import sqlite3; c=sqlite3.connect('/app/data/events.db'); [print(row) for row in c.execute('SELECT ticket_code, student_name, roll_no, event_id FROM registrations')]; c.close()"
```

### 5. Git Commands
```bash
# Initialize repository
git init

# Track changes
git add .

# Create descriptive commit
git commit -m "Initialize Campus Event Board with CI/CD, Docker, and Ansible"

# Branch management
git branch -M main

# Connect remote repository
git remote add origin https://github.com/<username>/CampusEventBoard.git
git push -u origin main
```

---

## 20. ADVANTAGES

- **Eliminates Physical Notice Board Clutter**: Instant centralized visibility for all college activities.
- **Prevents Overbooking**: Real-time capacity validation prevents registrations beyond hall limits.
- **Unique Digital Passes**: Alphanumeric ticket codes simplify on-site attendance verification.
- **Automated Quality Gate**: Pytest prevents broken code from reaching the live server.
- **Reproducible Environments**: Docker ensures the application runs identically on any workstation or server.
- **Zero-Data Loss Architecture**: Docker Volume guarantees data preservation during application redeployments.
- **Hands-Free Deployment**: Ansible and Jenkins eliminate error-prone manual server configuration.

---

## 21. LIMITATIONS

- Uses SQLite, which is ideal for single-node deployments but may experience concurrency locks under massive multi-thousand concurrent writes.
- Authentication currently uses roll-number validation rather than campus LDAP / Single Sign-On (SSO).
- SMS notifications and payment gateway integration are not currently implemented.
- System operates in a local containerized cluster rather than a multi-region cloud orchestrator (e.g., Kubernetes).

---

## 22. FUTURE ENHANCEMENTS

1. **Campus Single Sign-On (SSO)**: Integration with CIT Google Workspace / Microsoft 365 OAuth2.
2. **QR Code Generation**: Printable QR codes on passes for instant mobile camera scanning at venue gates.
3. **Email & WhatsApp Notifications**: Automated calendar invites (`.ics`) and registration reminders.
4. **PostgreSQL Migration**: High-concurrency relational backend for university-wide scaling.
5. **Kubernetes Orchestration**: Deployment to Amazon EKS or Google GKE using Helm charts for automatic pod scaling.
6. **Prometheus & Grafana**: Real-time metric monitoring and system alerts.

---

## 23. CONCLUSION

The **Campus Event Board** successfully demonstrates the complete integration of a modern web application with industry-standard DevOps automation practices. Students can effortlessly discover campus events and secure digital event passes, while administrators gain real-time oversight over event logistics.

The project fulfills all requirements of the **23IT723 – DevOps Laboratory** curriculum:
$$\text{GitHub} \longrightarrow \text{Jenkins} \longrightarrow \text{Docker} \longrightarrow \text{Pytest} \longrightarrow \text{Ansible} \longrightarrow \text{Flask} \longrightarrow \text{SQLite (Persistent Volume)}$$
By combining modular software engineering with an automated CI/CD pipeline, repeatable container deployments, and persistent storage, the Campus Event Board delivers an exemplary, production-grade DevOps implementation.
