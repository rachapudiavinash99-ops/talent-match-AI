import os
import json
import random
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "backend", "data")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

jobs = [
    {
        "id": f"eiq-job-{i}",
        "title": title,
        "department": dept,
        "location": loc,
        "description": f"ElevateIQ Soft Tech is seeking a talented {title} to scale our enterprise solutions in our {loc} facility. Elevate Your Career, Empower Your Future.",
        "required_skills": req_skills,
        "preferred_skills": pref_skills,
        "min_experience_years": exp,
        "education_requirement": edu,
        "status": "Open",
        "created_at": datetime.now().isoformat()
    }
    for i, (title, dept, loc, req_skills, pref_skills, exp, edu) in enumerate([
        ("Senior Full-Stack Engineer (React & Python)", "IT Engineering", "Chennai", ["react", "python", "fastapi", "sql"], ["docker", "next.js"], 4, "B.Tech / MCA"),
        ("Data Harvesting & Crawler Specialist", "Data Solutions", "Hyderabad", ["python", "web scraping", "selenium", "sql"], ["scrapy", "proxy rotation"], 3, "B.Tech / B.Sc Computer Science"),
        ("Cloud & DevOps Architect", "Cloud & Infra", "Kochi", ["aws", "docker", "kubernetes", "linux"], ["terraform", "ci/cd"], 5, "B.Tech / MCA"),
        ("Intelligent Document Processing (IDP) Engineer", "AI & Data", "Bengaluru", ["python", "ocr", "nlp", "machine learning"], ["layoutlm", "tensorflow"], 3, "B.Tech / M.Tech"),
        ("Data Annotation & ML Tagging Lead", "AI Solutions", "Narasaraopet", ["computer vision", "annotation", "nlp", "quality audit"], ["labeling", "python"], 2, "Any Graduate / BCA"),
        ("Certified Medical Coder (ICD-10 & CPT)", "Non-IT & Healthcare BPO", "Chennai", ["medical coding", "icd-10", "cpt", "hipaa"], ["rcm", "claims audit"], 3, "B.Pharm / Life Sciences / Nursing"),
        ("AR Calling & Denial Resolution Executive", "Healthcare Operations", "Kochi", ["ar calling", "denial management", "revenue cycle", "communication"], ["insurance follow-up"], 2, "Any Graduate"),
        ("TESS Quality & Technical Support Lead", "BPO & Customer Operations", "Narasaraopet", ["customer support", "tele-evaluation", "quality assurance", "communication"], ["helpdesk", "reporting"], 3, "Any Graduate"),
        ("Backend Python & Microservices Developer", "IT Engineering", "Hyderabad", ["python", "django", "sql", "redis"], ["aws", "kafka"], 4, "B.Tech / MCA"),
        ("Enterprise Frontend Developer (Next.js)", "IT Engineering", "Chennai", ["react", "next.js", "typescript", "tailwind"], ["graphql", "figma"], 3, "B.Tech / BCA")
    ], start=1)
]

candidates = [
    {
        "id": f"eiq-cand-{i}",
        "name": name,
        "email": f"{name.lower().replace(' ', '.')}@elevateiq-talent.in",
        "phone": f"+91-98{random.randint(10000000, 99999999)}",
        "skills": skills,
        "resume_file": f"{name.replace(' ', '_')}_Resume.pdf",
        "created_at": datetime.now().isoformat()
    }
    for i, (name, skills) in enumerate([
        ("Suresh Reddy", ["react", "python", "fastapi", "sql", "docker"]),
        ("Deepa Nair", ["python", "web scraping", "selenium", "sql", "scrapy"]),
        ("Karthik Menon", ["aws", "docker", "kubernetes", "linux", "terraform"]),
        ("Pooja Swaminathan", ["python", "ocr", "nlp", "machine learning", "tensorflow"]),
        ("Venkat Sai", ["computer vision", "annotation", "nlp", "quality audit", "labeling"]),
        ("Dr. Shalini Krishnan", ["medical coding", "icd-10", "cpt", "hipaa", "rcm"]),
        ("Akhil Varma", ["ar calling", "denial management", "revenue cycle", "communication"]),
        ("Anusha Rao", ["customer support", "tele-evaluation", "quality assurance", "communication"]),
        ("Mahesh Babu K", ["python", "django", "sql", "redis", "aws"]),
        ("Divya Balaji", ["react", "next.js", "typescript", "tailwind", "figma"])
    ], start=1)
]

# Generate realistic applications matching candidates with jobs
applications = []
for i in range(10):
    job = jobs[i]
    cand = candidates[i]
    
    req_match = len(set(cand["skills"]) & set(job["required_skills"]))
    req_score = (req_match / len(job["required_skills"])) if job["required_skills"] else 1.0
    overall = min(98.5, round((req_score * 0.85 + 0.12) * 100, 1))
    
    applications.append({
        "id": f"eiq-app-{i+1}",
        "job_id": job["id"],
        "candidate_id": cand["id"],
        "stage": random.choice(["Shortlisted", "Interview", "Offer", "Applied"]),
        "match_score": overall,
        "match_details": {
            "overall_score": overall,
            "required_skills_matched": list(set(cand["skills"]) & set(job["required_skills"])),
            "preferred_skills_matched": list(set(cand["skills"]) & set(job["preferred_skills"]))
        },
        "created_at": datetime.now().isoformat()
    })

with open(os.path.join(DATA_DIR, "jobs.json"), "w") as f:
    json.dump(jobs, f, indent=4)

with open(os.path.join(DATA_DIR, "candidates.json"), "w") as f:
    json.dump(candidates, f, indent=4)

with open(os.path.join(DATA_DIR, "applications.json"), "w") as f:
    json.dump(applications, f, indent=4)

print("ElevateIQ Soft Tech customized records successfully populated!")
