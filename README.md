# Smart Resume Screener & Job Matcher

<img width="842" height="525" alt="image" src="https://github.com/user-attachments/assets/a04682ff-fbc8-4ecc-82d3-d1d3a0fbfac1" />


## 🚀 Overview

AI-powered web app to **analyze resumes against any job description**, extract all entities (skills, education, experience, location), and provide an intuitive dashboard with ranked match scores and full explainability.  
Built with Flask, Python, NLP, and Tailwind CSS!

---

## ✨ Features

- **Parse PDF/DOCX resumes and job descriptions**  
- **Entity extraction**: skills, education, experience, location  
- **Matching algorithm**: Skill overlap %, experience/score, location  
- **Clear explainability**: Highlights missing/extra skills  
- **Modern dashboard** with filters and live feedback  
- **No file saving required** — parses in-memory  
- **Export-ready code for deployment** (Heroku, Vercel, etc.)

---

## 🖥️ Screenshots

**Result:**  
<img width="833" height="553" alt="image" src="https://github.com/user-attachments/assets/a01cc4d1-66f8-46cd-ab6e-3906981a47c2" />



## ⚡ Quickstart

1. **Clone the repo:**
    ```
    git clone https://github.com/your-username/resume_matcher.git
    cd resume_matcher
    ```

2. **Install requirements:**
    ```
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```

3. **Run the app:**
    ```
    python app.py
    ```

4. Open your browser to [http://localhost:5000](http://localhost:5000)  
   Upload a resume (PDF/DOCX) and a Job Description (TXT/PDF/DOCX) to see instant scoring and highlights.

---

## 🧠 Scoring Logic

- **Skill Match:**  
  \[
  \text{Skill Score} = \frac{|\text{Resume Skills} \cap \text{JD Skills}|}{|\text{JD Skills}|} \times 100
  \]
- **Experience Bonus:**  
  If experience meets or exceeds JD, boosts match
- **Location Bonus:**  
  Exact match adds points  
- **Explainability:**  
  Missing and extra skills are clearly listed in results

---

## 🗂️ Dataset

- Place your domain skill list as `skill_list.csv` in the root
- For testing/demo, use files from the `dataset/` folder (resumes and JDs)
- You can expand the included skill/entity vocab for your own domain!

---

## 📦 Deploy

- Run locally as above, or add a `Procfile` for Heroku:
    ```
    web: gunicorn app:app
    ```
- You can dockerize or adapt easily for Vercel/other platforms


