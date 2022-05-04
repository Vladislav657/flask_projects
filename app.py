from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    candidates = utils.load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<x>')
def candidate_x(x):
    candidates = utils.load_candidates_from_json('candidates.json')
    candidate = utils.get_candidate(x, candidates)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def candidate_by_name(candidate_name):
    candidates = utils.load_candidates_from_json('candidates.json')
    candidates_by_name = utils.get_candidates_by_name(candidate_name, candidates)
    return render_template('search.html', candidates=candidates_by_name, count=len(candidates_by_name))


@app.route('/skill/<skill_name>')
def candidate_by_skill(skill_name):
    candidates = utils.load_candidates_from_json('candidates.json')
    candidates_by_skill = utils.get_candidates_by_skill(skill_name, candidates)
    return render_template('skill.html', candidates=candidates_by_skill, count=len(candidates_by_skill),
                           skill=skill_name)


if __name__ == '__main__':
    app.run()
