from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
import os
from api.schemas import ApplicationBase, ApplicationResponse
from repository.base import JSONRepository
from services.nlp_engine import calculate_match_score
from api.candidates import extract_text_from_file, UPLOAD_DIR

router = APIRouter()
app_repo = JSONRepository("applications")
job_repo = JSONRepository("jobs")
candidate_repo = JSONRepository("candidates")

@router.get("/", response_model=List[ApplicationResponse])
def get_applications():
    return app_repo.get_all()

@router.post("/", response_model=ApplicationResponse)
def create_application(app: ApplicationBase):
    job = job_repo.get_by_id(app.job_id)
    candidate = candidate_repo.get_by_id(app.candidate_id)
    
    if not job or not candidate:
        raise HTTPException(status_code=404, detail="Job or Candidate not found")
        
    # Read resume text to calculate score
    resume_text = ""
    if candidate.get("resume_file"):
        filepath = os.path.join(UPLOAD_DIR, candidate["resume_file"])
        if os.path.exists(filepath):
            resume_text = extract_text_from_file(filepath)
            
    # Calculate match
    match_result = calculate_match_score(
        job_desc=job.get("description", ""),
        req_skills=job.get("required_skills", []),
        pref_skills=job.get("preferred_skills", []),
        resume_text=resume_text,
        candidate_skills=candidate.get("skills", [])
    )
    
    app_data = app.model_dump()
    app_data["match_score"] = match_result["overall_score"]
    app_data["match_details"] = match_result
    app_data["created_at"] = datetime.now().isoformat()
    
    created = app_repo.create(app_data)
    return created

@router.put("/{app_id}/stage")
def update_stage(app_id: str, stage: str):
    updated = app_repo.update(app_id, {"stage": stage})
    if not updated:
        raise HTTPException(status_code=404, detail="Application not found")
    return updated
