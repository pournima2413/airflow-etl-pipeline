# 🚀 Airflow ETL Pipeline with API Integration & PostgreSQL

> Production-style ETL pipeline using Apache Airflow, Docker, and PostgreSQL with real-time API integration

---

## 📌 Project Overview

This project builds an end-to-end **ETL (Extract, Transform, Load) pipeline** using Apache Airflow to automate data ingestion, transformation, and storage.

The pipeline extracts data from NASA’s Astronomy Picture of the Day (APOD) API, processes the JSON response, and loads structured data into a PostgreSQL database.

The entire system is containerized using Docker, ensuring a reproducible and scalable environment.

---

## 🎯 Project Impact

- Built a fully automated ETL pipeline using Apache Airflow  
- Integrated real-time API data into a structured database  
- Designed a containerized system using Docker  
- Gained hands-on experience debugging real-world issues like port conflicts and persistent volumes  

---

## 🖼️ Architecture Overview

![ETL Pipeline](./airflow_etl.png)

---

## 📂 Dataset Information

This project uses data from NASA’s Astronomy Picture of the Day (APOD) API.

The API provides daily astronomy-related data in JSON format, including metadata about space images.

### 📊 Data Fields Used

The pipeline extracts and stores the following key attributes:

- **date** → Date of the image  
- **title** → Title of the astronomy picture  
- **explanation** → Description of the image  
- **url** → Image URL  

---

## 🛠️ Tech Stack

- Python  
- Apache Airflow (TaskFlow API + Operators)  
- Docker  
- PostgreSQL  
- REST API (NASA APOD)  

---

## 🧩 Pipeline Flow

API → Airflow DAG → Transform (TaskFlow API) → PostgreSQL

---

## 🔄 How the Pipeline Works

### 1️⃣ Extract
- Fetches data from NASA APOD API  
- Uses HTTP-based operator in Airflow  
- Receives JSON response  

---

### 2️⃣ Transform
- Cleans and processes JSON data  
- Extracts key fields:
  - Title  
  - Explanation  
  - Image URL  
  - Date  
- Implemented using Airflow TaskFlow API (`@task`)  

---

### 3️⃣ Load
- Inserts processed data into PostgreSQL  
- Uses `PostgresHook`  
- Automatically creates table if not present  

---

## 📊 Sample Output

| Date       | Title                | URL                |
|------------|---------------------|--------------------|
| 2026-04-20 | Example Image Title | https://image.url  |

---

## ⚠️ Challenges & Solutions

### 🔹 Postgres Authentication Failure
- **Issue:** Password changes not reflected  
- **Cause:** Docker volumes persisted old credentials  
- **Solution:** Removed volumes and reinitialized database  

---

### 🔹 Dynamic Port Mapping (Astro)
- **Issue:** Postgres port kept changing  
- **Solution:** Used container-based connections inside Airflow instead of host ports  

---

### 🔹 Docker Networking Confusion
- **Issue:** Services couldn’t communicate  
- **Solution:** Learned difference between:
  - `localhost` (host)
  - container name (internal Docker network)

---

## ⚙️ Key Features

- Automated workflow using Airflow DAGs  
- Task dependencies handled sequentially  
- TaskFlow API for cleaner data processing  
- Real-world API integration  
- Containerized environment with Docker  
- Handles production-like issues and debugging  

---

## 🚀 How to Run

```bash
astro dev start
