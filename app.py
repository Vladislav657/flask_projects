from flask import Flask, render_template
import json


app = Flask(__name__)
with open("candidates.json", "r", encoding='UTF-8') as data:
    candidates = json.load(data)


@app.route('/')
@app.route('/index')
def index():
    with open("candidates.json", "r", encoding='UTF-8') as data:
        candidates = json.load(data)
    return render_template('index.html', candidates=candidates)


@app.route('/candidates/<x>')
def candidate(x):
    with open("candidates.json", "r", encoding='UTF-8') as data:
        candidates = json.load(data)
    for candidate in candidates:
        if str(candidate['id']) == str(x) or candidate['name'].lower() == str(x).lower():
            return render_template('candidate.html', candidate=candidate)


@app.route('/skills/<x>')
def skill(x):
    skills = []
    with open("candidates.json", "r", encoding='UTF-8') as data:
        candidates = json.load(data)
    for candidate in candidates:
        if str(x).lower() in candidate['skills'].lower().split(', '):
            skills.append(candidate)
    return render_template('skill.html', skills=skills, x=x.lower())


if __name__ == '__main__':
    app.run()
