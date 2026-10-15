from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from api.schemas import JobCreate, JobUpdate, JobResponse
from repository.base import JSONRepository

router = APIRouter()
job_repo = JSONRepository("jobs")

@router.get("/", response_model=List[JobResponse])
def get_jobs():
    return job_repo.get_all()

@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: str):
    job = job_repo.get_by_id(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/", response_model=JobResponse)
def create_job(job: JobCreate):
    job_data = job.model_dump()
    job_data["status"] = "Open"
    job_data["created_at"] = datetime.now().isoformat()
    created = job_repo.create(job_data)
    return created

@router.put("/{job_id}", response_model=JobResponse)
def update_job(job_id: str, job: JobUpdate):
    updated = job_repo.update(job_id, job.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Job not found")
    return updated

@router.delete("/{job_id}")
def delete_job(job_id: str):
    success = job_repo.delete(job_id)
    if not success:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"message": "Job deleted"}
