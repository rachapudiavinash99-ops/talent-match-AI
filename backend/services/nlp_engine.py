from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return ' '.join(text.split())

def extract_skills_from_text(text: str, known_skills: list[str]) -> list[str]:
    text_norm = normalize_text(text)
    found = []
    for skill in known_skills:
        if normalize_text(skill) in text_norm:
            found.append(skill)
    return found

def calculate_match_score(job_desc: str, req_skills: list[str], pref_skills: list[str], resume_text: str, candidate_skills: list[str]) -> dict:
    job_norm = normalize_text(job_desc)
    resume_norm = normalize_text(resume_text)
    
    # TF-IDF similarity on description
    vectorizer = TfidfVectorizer()
    try:
        tfidf_matrix = vectorizer.fit_transform([job_norm, resume_norm])
        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    except Exception:
        cosine_sim = 0.0

    # Skill match score
    req_matched = [s for s in req_skills if normalize_text(s) in [normalize_text(cs) for cs in candidate_skills] or normalize_text(s) in resume_norm]
    pref_matched = [s for s in pref_skills if normalize_text(s) in [normalize_text(cs) for cs in candidate_skills] or normalize_text(s) in resume_norm]
    
    req_missing = [s for s in req_skills if s not in req_matched]
    
    req_score = len(req_matched) / len(req_skills) if req_skills else 1.0
    pref_score = len(pref_matched) / len(pref_skills) if pref_skills else 1.0

    # Weighted overall score: 50% required skills, 20% pref skills, 30% cosine similarity
    overall_score = (req_score * 0.5) + (pref_score * 0.2) + (cosine_sim * 0.3)
    
    return {
        "overall_score": round(overall_score * 100, 2),
        "cosine_similarity": round(cosine_sim * 100, 2),
        "required_skills_matched": req_matched,
        "required_skills_missing": req_missing,
        "preferred_skills_matched": pref_matched
    }
