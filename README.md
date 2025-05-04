# SHL Assessment Recommendation Engine

This project recommends SHL assessments based on job role and skills.

## How It Works
- Python + FastAPI backend
- Streamlit frontend
- Uses SHL's product catalogue (CSV)
- Recommends assessments using rule-based filtering

## API Endpoint
POST /recommend

Example Input:
```json
{
  "job_role": "Software Developer",
  "key_skills": ["Problem Solving", "Coding"]
}
