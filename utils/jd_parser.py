import re

def parse_jd(text):
    # Required skills: comma or list in JD
    skills = re.findall(r'(?:skills? required|skills?)[:\- ]*(.*)', text, re.I)
    required_skills = []
    if skills:
        required_skills = [s.strip().lower() for s in re.split(r',|\n', skills[0]) if s.strip()]
    # Experience
    exp_match = re.findall(r'(\d+)[\s-]+years', text, re.I)
    min_experience = int(exp_match[0]) if exp_match else 0
    # Location
    loc = re.findall(r'(Mumbai|Delhi|Bangalore|Pune|Chennai|Hyderabad)', text, re.I)
    location = loc[0] if loc else ''
    return required_skills, min_experience, location
