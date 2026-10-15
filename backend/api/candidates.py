from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from typing import List, Optional
import os
import shutil
import uuid
from datetime import datetime
from api.schemas import CandidateResponse
from repository.base import JSONRepository
from services.nlp_engine import extract_skills_from_text

# In a real app we'd use pdfplumber/PyPDF2 and python-docx here.
import PyPDF2
import docx

router = APIRouter()
candidate_repo = JSONRepository("candidates")

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "uploads")
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Minimal demo skill list
KNOWN_SKILLS = ["python", "java", "javascript", "react", "fastapi", "sql", "machine learning", "docker", "aws"]

def extract_text_from_file(filepath: str) -> str:
    text = ""
    ext = filepath.split('.')[-1].lower()
    try:
        if ext == 'pdf':
            with open(filepath, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + " "
        elif ext == 'docx':
            doc = docx.Document(filepath)
            for para in doc.paragraphs:
                text += para.text + " "
    except Exception as e:
        print(f"Error parsing file {filepath}: {e}")
    return text

@router.get("/", response_model=List[CandidateResponse])
def get_candidates():
    return candidate_repo.get_all()

@router.post("/upload", response_model=CandidateResponse)
def upload_candidate(
    name: str = Form(...),
    email: str = Form(...),
    phone: Optional[str] = Form(None),
    file: UploadFile = File(...)
):
    # Save file
    ext = file.filename.split('.')[-1]
    if ext.lower() not in ['pdf', 'docx']:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX are supported")
    
    file_id = str(uuid.uuid4())
    filename = f"{file_id}.{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # Parse file
    text = extract_text_from_file(filepath)
    skills = extract_skills_from_text(text, KNOWN_SKILLS)
    
    candidate_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "resume_file": filename,
        "created_at": datetime.now().isoformat()
    }
    
    created = candidate_repo.create(candidate_data)
    return created
