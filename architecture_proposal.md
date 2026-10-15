# TalentMatch AI - Implementation Plan & Architecture Proposal

## 1. Repository Inspection Results

I have inspected the target directory `D:\resume project`.
**Status:** The repository is currently **empty**. There are no existing frontend, backend, or configurations to inherit.

As per your instructions: *"If the repository is empty, propose a minimal, coherent architecture that satisfies all requirements before implementation."*

## 2. Proposed Architecture

Since we need a local AI/NLP matching engine (requiring Python for data science libraries) and a unified, responsive frontend, I propose the following architecture:

### Tech Stack
*   **Backend:** Python with **FastAPI**
    *   *Why:* Excellent for serving API routes, handling file uploads, and seamlessly integrating with Python's rich ecosystem of NLP libraries (NLTK, scikit-learn).
*   **Frontend:** **React** (via Vite) with **Tailwind CSS**
    *   *Why:* Provides a highly responsive, component-driven UI for dashboards, job management, and drag-and-drop file uploads.
*   **Data Persistence (No Database):** **JSON / CSV files**
    *   *Why:* Satisfies the strict "No DB" rule. We will build a generic Repository layer in Python that reads/writes models to JSON files (with file locking mechanisms to prevent concurrent write issues).
*   **Local NLP / AI Matching:**
    *   *Libraries:* `scikit-learn` (for TF-IDF and Cosine Similarity), `PyPDF2` / `pdfplumber` (for PDF parsing), `python-docx` (for DOCX parsing), `nltk` or `spacy` (for text normalization and skill extraction).

### Directory Structure

```text
D:\resume project\
├── backend\                  # FastAPI application
│   ├── main.py               # Entry point
│   ├── api\                  # API routes (jobs, candidates, matching)
│   ├── core\                 # Configuration, Logging, File Locks
│   ├── data\                 # Local file storage (JSON/CSV) - Excluded from git
│   ├── repository\           # File-based CRUD operations
│   ├── services\             # Business logic (Parsing, Matching, Scoring)
│   ├── tests\                # Pytest test suite
│   └── requirements.txt      # Python dependencies
├── frontend\                 # React application
│   ├── src\
│   │   ├── components\       # Reusable UI components (Sidebar, Tables, Modals)
│   │   ├── pages\            # Dashboard, Jobs, Candidates, Reports
│   │   ├── services\         # API client hooks
│   │   └── App.jsx           # Main routing
│   ├── package.json
│   └── tailwind.config.js
└── README.md
```

## 3. Key Feature Implementation Plan

1.  **File-Based Storage System:**
    *   Create a base `JSONRepository` class in Python that implements `get_all`, `get_by_id`, `create`, `update`, `delete`.
    *   Use file locks (`filelock` library) to prevent race conditions.
2.  **Resume Parsing & Local NLP Engine:**
    *   Implement an upload endpoint that accepts PDFs and DOCX files.
    *   Extract text and perform basic NER (Named Entity Recognition) to find emails, names, and a predefined list of technical skills.
    *   Implement TF-IDF vectorization on the job description vs the resume text, calculating cosine similarity for a baseline match score, combined with boolean skill matching.
3.  **Unified Frontend:**
    *   Build a Single Page Application (SPA) with React Router.
    *   Implement layout with a sidebar navigation (Dashboard, Jobs, Candidates, Reports).
4.  **Analytics & Reports:**
    *   Aggregate JSON data in memory on the backend to serve statistics for the frontend Dashboard.
    *   Provide endpoints that export CSVs of candidates and applications.

## 4. Next Steps

Before I begin broad code generation, please **review and approve** this architecture plan. 
Once you give the go-ahead, I will start by scaffolding the backend and building the file-based repository layer.
