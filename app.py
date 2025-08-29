from flask import Flask, render_template, request
from utils.resume_parser import parse_resume, extract_entities
from utils.jd_parser import parse_jd
from utils.matcher import score_resume

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    result = None
    if request.method == 'POST':
        resume_file = request.files['resume']
        jd_file = request.files['jd']
        resume_text = parse_resume(resume_file, resume_file.filename)
        jd_text = jd_file.read().decode(errors="ignore")
        skills, edu, loc, exp = extract_entities(resume_text)
        req_skills, min_exp, jd_loc = parse_jd(jd_text)
        match = score_resume(
            {'skills': skills, 'experience_years': exp, 'location': loc},
            {'required_skills': req_skills, 'min_experience': min_exp, 'location': jd_loc}
        )
        result = {
            'skills': skills,
            'education': edu,
            'location': loc,
            'experience_years': exp,
            'req_skills': req_skills,
            'min_exp': min_exp,
            'jd_loc': jd_loc,
            **match
        }
    return render_template('dashboard.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
