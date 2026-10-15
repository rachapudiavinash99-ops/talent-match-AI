import os
import json
import random
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(__file__), "backend", "data")

# Load existing jobs
jobs_file = os.path.join(DATA_DIR, "jobs.json")
with open(jobs_file, "r", encoding="utf-8") as f:
    jobs = json.load(f)

# Existing candidates and applications preservation
candidates_file = os.path.join(DATA_DIR, "candidates.json")
try:
    with open(candidates_file, "r", encoding="utf-8") as f:
        existing_cands = {c["id"]: c for c in json.load(f)}
except Exception:
    existing_cands = {}

applications_file = os.path.join(DATA_DIR, "applications.json")
try:
    with open(applications_file, "r", encoding="utf-8") as f:
        existing_apps = json.load(f)
except Exception:
    existing_apps = []

# Preserve user-submitted application (like bhanu)
preserved_apps = [a for a in existing_apps if a.get("candidate_id") == "462e73b3-8892-4100-b4cb-17fc7a0997f3"]
preserved_cand_ids = {"462e73b3-8892-4100-b4cb-17fc7a0997f3"}

# Job specific profiles specification: 5 candidates for each job with distinct percentages and stages
job_profiles = {
    "eiq-job-1": [
        ("Suresh Reddy", ["react", "python", "fastapi", "sql", "docker", "next.js"], 96.5, "Offer", "Chennai"),
        ("Ananya Sharma", ["react", "python", "fastapi", "next.js"], 86.0, "Interview", "Bengaluru"),
        ("Vikramaditya Rao", ["react", "python", "sql", "git"], 73.5, "Shortlisted", "Hyderabad"),
        ("Meera Krishnan", ["python", "sql", "docker"], 58.0, "Under Review", "Chennai"),
        ("Rohan Deshmukh", ["react", "javascript", "html", "css"], 41.5, "Applied", "Pune")
    ],
    "eiq-job-2": [
        ("Deepa Nair", ["python", "web scraping", "selenium", "sql", "scrapy"], 97.2, "Offer", "Kochi"),
        ("Harish Venkat", ["python", "web scraping", "selenium", "proxy rotation"], 85.4, "Interview", "Hyderabad"),
        ("Sneha Kulkarni", ["python", "web scraping", "sql"], 74.0, "Shortlisted", "Bengaluru"),
        ("Ashwin Prasad", ["python", "sql", "scrapy", "bs4"], 57.5, "Under Review", "Chennai"),
        ("Kavita Subramanian", ["python", "pandas", "excel"], 39.0, "Applied", "Hyderabad")
    ],
    "eiq-job-3": [
        ("Karthik Menon", ["aws", "docker", "kubernetes", "linux", "terraform", "ci/cd"], 98.4, "Offer", "Kochi"),
        ("Rajesh Nambiar", ["aws", "docker", "linux", "ci/cd"], 86.8, "Interview", "Thiruvananthapuram"),
        ("Divya Varma", ["docker", "linux", "aws", "bash"], 72.5, "Shortlisted", "Kochi"),
        ("Tarun Chawla", ["linux", "docker", "terraform"], 56.0, "Under Review", "Bengaluru"),
        ("Neha Singhal", ["linux", "networking", "system admin"], 38.2, "Rejected", "Noida")
    ],
    "eiq-job-4": [
        ("Pooja Swaminathan", ["python", "ocr", "nlp", "machine learning", "tensorflow", "layoutlm"], 96.8, "Offer", "Chennai"),
        ("Arvind Sundaram", ["python", "nlp", "machine learning", "layoutlm"], 87.5, "Interview", "Bengaluru"),
        ("Priyanka Joshi", ["python", "machine learning", "ocr", "pytorch"], 75.0, "Shortlisted", "Hyderabad"),
        ("Gaurav Sengupta", ["python", "nlp", "tensorflow"], 59.2, "Under Review", "Kolkata"),
        ("Shalini Patnaik", ["python", "scikit-learn", "data analysis"], 43.0, "Applied", "Bhubaneswar")
    ],
    "eiq-job-5": [
        ("Venkatesh Prasad", ["computer vision", "annotation", "nlp", "quality audit", "labeling"], 95.5, "Offer", "Vijayawada"),
        ("Bhavana Kommineni", ["annotation", "quality audit", "computer vision", "python"], 84.8, "Interview", "Guntur"),
        ("Manoj Kumar Reddy", ["annotation", "quality audit", "nlp", "labeling"], 71.5, "Shortlisted", "Narasaraopet"),
        ("Rashmi Hegde", ["annotation", "quality audit", "excel"], 54.0, "Under Review", "Mangaluru"),
        ("Deepak Verma", ["annotation", "data entry"], 37.5, "Applied", "Visakhapatnam")
    ],
    "eiq-job-6": [
        ("Dr. Shalini Krishnan", ["medical coding", "icd-10", "cpt", "hipaa", "rcm"], 97.6, "Offer", "Chennai"),
        ("Dr. Sangeetha Raman", ["medical coding", "icd-10", "cpt", "claims audit"], 88.4, "Interview", "Coimbatore"),
        ("Vignesh Pandian", ["medical coding", "icd-10", "hipaa"], 76.2, "Shortlisted", "Madurai"),
        ("Swati Murthy", ["medical coding", "hipaa", "rcm"], 62.0, "Under Review", "Chennai"),
        ("Praveen Pillai", ["medical coding", "anatomy", "billing"], 44.5, "Applied", "Kollam")
    ],
    "eiq-job-7": [
        ("Akhil Varma", ["ar calling", "denial management", "revenue cycle", "communication", "insurance follow-up"], 96.2, "Offer", "Kochi"),
        ("Keerthi Vasudevan", ["ar calling", "denial management", "communication", "insurance follow-up"], 86.5, "Interview", "Thrissur"),
        ("Gokul Raj", ["ar calling", "communication", "revenue cycle"], 73.8, "Shortlisted", "Calicut"),
        ("Madhuri Rao", ["ar calling", "communication", "insurance follow-up"], 58.2, "Under Review", "Kochi"),
        ("Santosh Iyer", ["communication", "voice operations"], 40.0, "Applied", "Palakkad")
    ],
    "eiq-job-8": [
        ("Anusha Rao", ["customer support", "tele-evaluation", "quality assurance", "communication", "helpdesk"], 95.8, "Offer", "Narasaraopet"),
        ("Vijay Anand", ["customer support", "quality assurance", "communication", "reporting"], 85.6, "Interview", "Guntur"),
        ("Preethi Chandran", ["customer support", "tele-evaluation", "communication"], 74.0, "Shortlisted", "Nellore"),
        ("Rohit George", ["customer support", "communication", "helpdesk"], 57.5, "Under Review", "Kochi"),
        ("Shalini Sridhar", ["customer support", "inbound calls"], 42.0, "Applied", "Ongole")
    ],
    "eiq-job-9": [
        ("Mahesh Babu K", ["python", "django", "sql", "redis", "aws", "kafka"], 97.0, "Offer", "Hyderabad"),
        ("Tanvi Deshpande", ["python", "django", "sql", "aws"], 86.2, "Interview", "Pune"),
        ("Nikhil Bhat", ["python", "sql", "redis", "flask"], 73.0, "Shortlisted", "Bengaluru"),
        ("Radhika Patel", ["python", "sql", "kafka"], 56.4, "Under Review", "Ahmedabad"),
        ("Abhishek Kulkarni", ["python", "c++", "data structures"], 38.5, "Applied", "Hyderabad")
    ],
    "eiq-job-10": [
        ("Divya Balaji", ["react", "next.js", "typescript", "tailwind", "graphql", "figma"], 98.0, "Offer", "Chennai"),
        ("Karthika Mohan", ["react", "next.js", "typescript", "graphql"], 88.0, "Interview", "Tiruchirappalli"),
        ("Varun Nambisan", ["react", "next.js", "tailwind", "css"], 75.5, "Shortlisted", "Chennai"),
        ("Aditi Saxena", ["react", "tailwind", "figma", "ui design"], 61.2, "Under Review", "Delhi"),
        ("Mithun Roy", ["react", "javascript", "bootstrap"], 44.0, "Applied", "Chennai")
    ]
}

new_candidates = []
new_applications = []

cand_idx = 1
app_idx = 1

base_time = datetime.now() - timedelta(days=5)

for job in jobs:
    jid = job["id"]
    req_skills = job.get("required_skills", [])
    pref_skills = job.get("preferred_skills", [])
    
    profiles = job_profiles.get(jid, [])
    # If no predefined profile, synthesize 5 varied profiles
    if not profiles:
        title = job.get("title", "Software Engineer")
        profiles = [
            (f"Lead Specialist {jid[-2:]}A", req_skills + pref_skills, 96.0, "Offer", "Chennai"),
            (f"Senior Pro {jid[-2:]}B", req_skills[:3] + pref_skills[:1], 85.5, "Interview", "Hyderabad"),
            (f"Specialist {jid[-2:]}C", req_skills[:2] + req_skills[-1:], 74.0, "Shortlisted", "Kochi"),
            (f"Associate {jid[-2:]}D", req_skills[:2], 58.5, "Under Review", "Narasaraopet"),
            (f"Graduate {jid[-2:]}E", req_skills[:1], 42.0, "Applied", "Bengaluru")
        ]

    for p_idx, (name, cand_skills, score, stage, city) in enumerate(profiles, start=1):
        cid = f"eiq-cand-auto-{cand_idx}"
        phone_num = f"+91-98{random.randint(10000000, 99999999)}"
        email_addr = f"{name.lower().replace(' ', '.').replace('dr.', 'dr')}.{random.randint(10,99)}@elevateiq-talent.in"
        cand_time = (base_time + timedelta(hours=random.randint(1, 100))).isoformat()
        
        cand_obj = {
            "id": cid,
            "name": name,
            "email": email_addr,
            "phone": phone_num,
            "skills": cand_skills,
            "education": "B.Tech / MCA / Relevant Degree",
            "experience": f"{random.randint(2, 8)} Years Professional Experience in {city}",
            "projects": f"Enterprise Scale implementations at ElevateIQ delivery ecosystem.",
            "resume_file": f"{name.replace(' ', '_').replace('Dr._', '')}_Resume.pdf",
            "created_at": cand_time
        }
        new_candidates.append(cand_obj)
        
        # Skill matching details
        matched_req = [s for s in req_skills if s.lower() in [cs.lower() for cs in cand_skills]]
        missing_req = [s for s in req_skills if s.lower() not in [cs.lower() for cs in cand_skills]]
        matched_pref = [s for s in pref_skills if s.lower() in [cs.lower() for cs in cand_skills]]
        
        # Cosine similarity estimation correlating to overall score
        cosine_sim = round(max(5.0, score - random.uniform(3.0, 8.0)), 2)
        
        app_obj = {
            "id": f"eiq-app-auto-{app_idx}",
            "job_id": jid,
            "candidate_id": cid,
            "stage": stage,
            "notes": f"Screened profile from {city}. Competency score verified against job skill vectors.",
            "match_score": score,
            "match_details": {
                "overall_score": score,
                "cosine_similarity": cosine_sim,
                "required_skills_matched": matched_req,
                "required_skills_missing": missing_req,
                "preferred_skills_matched": matched_pref
            },
            "created_at": cand_time
        }
        new_applications.append(app_obj)
        
        cand_idx += 1
        app_idx += 1

# Append preserved candidates (like bhanu)
for pid in preserved_cand_ids:
    if pid in existing_cands:
        new_candidates.append(existing_cands[pid])

# Append preserved applications
new_applications.extend(preserved_apps)

with open(candidates_file, "w", encoding="utf-8") as f:
    json.dump(new_candidates, f, indent=4)

with open(applications_file, "w", encoding="utf-8") as f:
    json.dump(new_applications, f, indent=4)

print(f"Successfully generated {len(new_applications)} applications across {len(jobs)} positions.")
for job in jobs:
    apps_for_job = [a for a in new_applications if a["job_id"] == job["id"]]
    scores = [a["match_score"] for a in apps_for_job]
    print(f"Job: {job['title'][:35]} -> {len(apps_for_job)} apps, scores={scores}")
