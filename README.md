# talent-match-AI

> **TalentMatch AI** — Enterprise-Grade Autonomous Resume Screening & Recruitment Intelligence Platform for **ElevateIQ Soft Tech Pvt. Ltd.**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-009688.svg?style=flat&logo=FastAPI)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18.2.0-61DAFB.svg?style=flat&logo=React)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-5.4-646CFF.svg?style=flat&logo=Vite)](https://vitejs.dev/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.4-38B2AC.svg?style=flat&logo=TailwindCSS)](https://tailwindcss.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-F7931E.svg?style=flat&logo=scikitlearn)](https://scikit-learn.org/)
[![Zero-Database](https://img.shields.io/badge/Data%20Layer-Thread--Safe%20JSON%20Repository-success.svg)](#architecture)
[![Zero-External-API](https://img.shields.io/badge/AI%20Engine-100%25%20Local%20Deterministic%20NLP-blue.svg)](#local-ai-engine)

---

## 🌟 Executive Overview

**TalentMatch AI** is a complete, unified, production-grade recruitment and candidate screening ecosystem designed to streamline high-volume talent acquisition for modern engineering enterprises. Built with a **privacy-first, zero-database architecture**, the platform guarantees 100% local, deterministic processing without exposing candidate data to third-party commercial APIs or external cloud databases.

The platform bridges two interconnected operational surfaces:
1. **ElevateIQ Public Careers & Job Seeker Portal:** High-impact, responsive candidate experience featuring open positions across Chennai, Kochi, Narasaraopet, and Hyderabad with instant resume upload and real-time AI match scoring.
2. **ElevateIQ Recruiter Command Center:** Comprehensive candidate tracking, deep skill vector decomposition (TF-IDF cosine similarity, required vs. missing skill gaps, bonus competencies), stage progression, and CSV audit reporting.

---

## 🏗️ Architecture & Technical Stack

### High-Level Topology
```
                     ┌────────────────────────────────────────┐
                     │          ElevateIQ Web Client          │
                     │  (React 18 + Vite + Tailwind + Lucide) │
                     └───────────────────┬────────────────────┘
                                         │ HTTP REST (Port 5173)
                                         ▼
                     ┌────────────────────────────────────────┐
                     │       FastAPI Application Gateway      │
                     │          (Uvicorn ASGI Server)         │
                     └───────────────────┬────────────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
   ┌───────────────────────────┐                   ┌───────────────────────────┐
   │    Local AI / NLP Core    │                   │   File-Based Repository   │
   │  - TF-IDF Vectorizer      │                   │  - JSON Data Persistence  │
   │  - Cosine Distance Engine │                   │  - FileLock Concurrency   │
   │  - PyPDF2 / python-docx   │                   │  - Atomic Disk Writes     │
   │  - Skill Taxonomy & Synset│                   │  - Zero SQL/NoSQL Engines │
   └───────────────────────────┘                   └───────────────────────────┘
```

### Core Technologies
- **Frontend:** React 18, Vite 5, Tailwind CSS, Lucide React, Axios, React Router DOM v6
- **Backend Services:** Python 3.10+, FastAPI, Uvicorn, Pydantic v2
- **NLP & Matching:** Scikit-Learn (TF-IDF vectorizer, cosine similarity), PyPDF2, python-docx
- **Data Persistence:** Thread-safe `JSONRepository` utilizing `filelock.FileLock`
- **Branding & Design System:** ElevateIQ Soft Tech Midnight (`#06091A`), Elevate Orange (`#ff8a3d`), and Electric Cyan (`#3fd0ff`)

---

## 🚀 Key Modules & Capabilities

### 1. Unified Careers & Job Seeker Portal
- **Real-Time Job Requisitions:** Filter jobs by technical domain (*IT Engineering*, *Data Solutions*, *Cloud & DevOps*, *Healthcare BPO*) and branch location (*Chennai*, *Kochi*, *Narasaraopet*, *Hyderabad*, *Bengaluru*).
- **Direct Resume Extraction:** Drag-and-drop ingestion of PDF and DOCX documents with automated text normalization.
- **Candidate AI Match Diagnostic:** Instant feedback calculating compatibility percentage, extracted skill vectors, and candidate fit.

### 2. Recruiter Command Center
- **Dynamic Funnel Analytics:** Live visualization tracking applicants through *Applied*, *Under Review*, *Shortlisted*, *Interview*, and *Offer* stages.
- **Deep Neural Diagnostic Modal:** Interactive 3-way skill vector breakdown highlighting *Confirmed Skills*, *Critical Skill Deficits*, and *Bonus Transferable Skills*.
- **Master Audit Reporting:** Dynamic CSV telemetry export containing full candidate application histories and screening metrics.

---

## 🛠️ Local Installation & Execution

### Prerequisites
- Python 3.10 or higher
- Node.js 18 or 20 (Node 20 LTS recommended)
- Git

### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate   # Windows
# source venv/bin/activate # macOS/Linux

# Install required packages
pip install fastapi uvicorn filelock scikit-learn PyPDF2 python-docx python-multipart

# Start the FastAPI ASGI server
uvicorn main:app --reload --port 8000
```

### Frontend Setup
```bash
# In a separate terminal, navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the Vite development server
npm run dev
```

Open your browser to: **`http://localhost:5173/`**

---

## 📊 Directory Structure
```
D:\resume project\
├── .gitignore
├── README.md
├── architecture_proposal.md
├── populate_data.py
├── backend/
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── applications.py
│   │   ├── candidates.py
│   │   ├── jobs.py
│   │   └── schemas.py
│   ├── data/
│   │   ├── applications.json
│   │   ├── candidates.json
│   │   └── jobs.json
│   ├── repository/
│   │   ├── __init__.py
│   │   └── base.py
│   └── services/
│       ├── __init__.py
│       ├── nlp_engine.py
│       └── parser.py
└── frontend/
    ├── package.json
    ├── vite.config.js
    ├── tailwind.config.js
    └── src/
        ├── App.jsx
        ├── main.jsx
        ├── index.css
        └── pages/
            ├── ElevateIQHome.jsx
            ├── Dashboard.jsx
            ├── Jobs.jsx
            ├── Candidates.jsx
            ├── Applications.jsx
            ├── Reports.jsx
            └── Settings.jsx
```

---

## 🔒 Compliance & Non-Negotiable Rules
- **No Database Engine:** Strictly persists structured records in thread-safe JSON files with atomic writes.
- **Zero API Dependency:** Local deterministic algorithms execute on-premise without external token costs or network latency.
- **Privacy & Security:** Sensitive candidate attributes are scrubbed and kept strictly within local controlled directories.

---

© 2026 ElevateIQ Soft Tech Private Limited. All Rights Reserved.
