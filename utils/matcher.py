def score_resume(resume_dict, jd_dict):
    resume_skills = set([s.lower() for s in resume_dict['skills']])
    jd_skills = set([s.lower() for s in jd_dict['required_skills']])
    overlap = len(resume_skills & jd_skills)
    total = len(jd_skills) if jd_skills else 1
    skill_score = (overlap / total) * 100

    if jd_dict['min_experience']:
        exp_score = min(((resume_dict['experience_years'] / jd_dict['min_experience'])*100), 100)
    else:
        exp_score = 50

    location_bonus = (resume_dict['location'].lower() == jd_dict['location'].lower()) if resume_dict['location'] and jd_dict['location'] else 0
    final_score = round(skill_score*0.6 + exp_score*0.3 + (10 if location_bonus else 0), 1)
    missing_skills = list(jd_skills - resume_skills)
    extra_skills = list(resume_skills - jd_skills)
    return {
        'score': final_score,
        'missing': missing_skills,
        'extra': extra_skills,
        'skill_score': round(skill_score, 1),
        'exp_score': round(exp_score, 1)
    }
