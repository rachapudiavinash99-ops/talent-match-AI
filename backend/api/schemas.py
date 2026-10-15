from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class JobBase(BaseModel):
    title: str
    department: str
    location: str
    description: str
    required_skills: List[str]
    preferred_skills: List[str]
    min_experience_years: int
    education_requirement: str

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    title: Optional[str] = None
    department: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    required_skills: Optional[List[str]] = None
    preferred_skills: Optional[List[str]] = None
    min_experience_years: Optional[int] = None
    education_requirement: Optional[str] = None
    status: Optional[str] = None

class JobResponse(JobBase):
    id: str
    status: str
    created_at: str

class CandidateBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    skills: List[str]
    education: Optional[str] = None
    experience: Optional[str] = None
    projects: Optional[str] = None

class CandidateResponse(CandidateBase):
    id: str
    resume_file: Optional[str] = None
    created_at: str

class ApplicationBase(BaseModel):
    job_id: str
    candidate_id: str
    stage: str = "Applied"
    notes: Optional[str] = None
    match_score: Optional[float] = None
    match_details: Optional[dict] = None

class ApplicationResponse(ApplicationBase):
    id: str
    created_at: str
