from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import jobs, candidates, applications

app = FastAPI(title="TalentMatch AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Welcome to TalentMatch AI API"}

app.include_router(jobs.router, prefix="/api/jobs", tags=["Jobs"])
app.include_router(candidates.router, prefix="/api/candidates", tags=["Candidates"])
app.include_router(applications.router, prefix="/api/applications", tags=["Applications"])
