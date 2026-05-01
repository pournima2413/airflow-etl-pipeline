# ⚙️ Airflow ETL Pipeline — NASA APOD API + PostgreSQL

> Production-style ETL pipeline using Apache Airflow, Docker, and PostgreSQL with real-time API integration.

![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-14B8A6?style=flat-square)

---

## 📌 Overview

This project builds an end-to-end **ETL pipeline** using Apache Airflow to automate data ingestion, transformation, and storage.

The pipeline extracts data from **NASA's Astronomy Picture of the Day (APOD) API**, processes the JSON response, and loads structured records into a **PostgreSQL database** — all running inside a containerized Docker environment.

---

## 🏗️ Architecture


NASA APOD API
      │
      ▼
Apache Airflow DAG
      │
      ├── Extract   →   HTTP Operator fetches JSON from API
      │
      ├── Transform →   TaskFlow @task cleans and structures data
      │
      └── Load      →   PostgresHook inserts records into PostgreSQL


All services run inside Docker containers on a shared internal network.



## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core pipeline logic |
| Apache Airflow | DAG orchestration and scheduling |
| TaskFlow API | Clean task definition with `@task` decorator |
| Docker | Containerized and reproducible environment |
| PostgreSQL | Structured data storage |
| NASA APOD API | Real-time data source |

---

## 📂 Dataset — NASA APOD API

The pipeline extracts the following fields from the API response:

| Field | Type | Description |
|---|---|---|
| `date` | DATE | Date of the astronomy picture |
| `title` | TEXT | Title of the image |
| `explanation` | TEXT | Scientific description |
| `url` | TEXT | Direct link to the image |

---

## 🔄 Pipeline — Step by Step

### 1. Extract
- Calls NASA APOD REST API on a scheduled trigger
- Uses Airflow's HTTP Operator
- Returns raw JSON response

### 2. Transform
- Parses and cleans the JSON payload
- Extracts `title`, `date`, `url`, `explanation`
- Implemented using the TaskFlow API `@task` decorator

### 3. Load
- Inserts processed records into PostgreSQL via `PostgresHook`
- Auto-creates the table on first run if not present
- Handles duplicate entries gracefully

---

## 📊 Sample Output

| Date | Title | URL |
|---|---|---|
| 2026-04-20 | Pillars of Creation | https://apod.nasa.gov/... |
| 2026-04-21 | Andromeda Galaxy | https://apod.nasa.gov/... |
| 2026-04-22 | Solar Flare Event | https://apod.nasa.gov/... |

---

## 📁 Project Structure


airflow-etl-pipeline/
│
├── dags/
│   └── etl_pipeline.py       ← Main DAG definition
│
├── include/
│   └── sql/                  ← SQL scripts
│
├── plugins/                  ← Custom Airflow plugins
├── tests/                    ← Unit tests
├── Dockerfile                ← Airflow image config
├── docker-compose.yml        ← Multi-container setup
├── requirements.txt          ← Python dependencies
└── README.md


---

## ⚠️ Challenges & Solutions

**1. Postgres Authentication Failure**
- Issue: Password changes not reflected after container restart
- Cause: Docker volumes were persisting old credentials
- Fix: Removed existing volumes and reinitialized the database

**2. Dynamic Port Mapping**
- Issue: Postgres port kept changing between Astro CLI restarts
- Fix: Switched to container-name-based internal connections instead of host ports

**3. Docker Networking**
- Issue: Services couldn't communicate across containers
- Fix: Used container names as hostnames instead of `localhost` — containers communicate via Docker's internal network, not the host machine

---

## ⚙️ Key Features

- Automated workflow orchestrated by Airflow DAGs
- Sequential task dependencies with clear separation of concerns
- TaskFlow API for readable and maintainable pipeline code
- Real-world API integration with error handling
- Fully containerized — runs identically on any machine
- Auto-provisions database table on first run

---

## 🚀 How to Run

**Prerequisites:** Docker Desktop and Astro CLI installed

bash
### Clone the repository
git clone https://github.com/pournima2413/airflow-etl-pipeline
cd airflow-etl-pipeline

### Start the Airflow environment
astro dev start

### Open Airflow UI
  http://localhost:8080
  Username: admin | Password: admin

### Trigger the DAG from the UI or via CLI
astro run etl_pipeline

### Stop the environment
astro dev stop


---

## 🔗 Connect

**Pournima Kamble** — MS Computer Science @ Cleveland State University (2026)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/pournimakamble)
[![GitHub](https://img.shields.io/badge/GitHub-pournima2413-333?style=flat-square&logo=github&logoColor=white)](https://github.com/pournima2413)
[![Email](https://img.shields.io/badge/Email-pournima2413@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:pournima2413@gmail.com)
