
import spacy
import pandas as pd
import re
import os

# Load reference skills from CSV
cwd = os.path.dirname(__file__)
skill_reference = pd.read_csv(os.path.join(cwd, 'skill_list.csv'))['Skill'].str.lower().tolist()

try:
    nlp = spacy.load('en_core_web_sm')
except:
    import subprocess
    subprocess.run(['python', '-m', 'spacy', 'download', 'en_core_web_sm'])
    nlp = spacy.load('en_core_web_sm')

from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document
import io

def parse_resume(file_obj, filename):
    ext = filename.lower().split('.')[-1]
    text = ""
    file_obj.seek(0)  # ensure at start
    if ext == 'pdf':
        # get a BytesIO stream, then pass it to pdfminer
        pdf_bytes = file_obj.read()
        text = pdf_extract_text(io.BytesIO(pdf_bytes))
    elif ext == 'docx':
        # use python-docx directly from file_obj.stream
        document = Document(file_obj)
        text = "\n".join([para.text for para in document.paragraphs])
    else:
        text = file_obj.read().decode(errors='ignore')
    file_obj.seek(0)
    return text


def extract_entities(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop]

    # Extract skills
    skills = sorted(list(set([skill for skill in skill_reference if skill in text.lower()])))
    # Education: simple regex for degree words
    edu_matches = re.findall(r"(B\.?Tech|M\.?Tech|B\.?Sc|M\.?Sc|BE|ME|MBA|PhD)", text, re.I)
    education = ', '.join(set([e.upper() for e in edu_matches])) if edu_matches else ''

    # Location: naive approach
    loc_matches = re.findall(r'(Mumbai|Delhi|Bangalore|Pune|Chennai|Hyderabad)', text, re.I)
    location = loc_matches[0] if loc_matches else ''

    # Experience years: e.g., 'X years'
    exp_matches = re.findall(r'(\d+)[\s-]+years', text, re.I)
    exp_years = int(exp_matches[0]) if exp_matches else 0

    return skills, education, location, exp_years
