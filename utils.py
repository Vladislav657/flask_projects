import json


def load_candidates_from_json(path):
    with open(path, "r", encoding='UTF-8') as data:
        return json.load(data)


def get_candidate(candidate_id, candidates):
    candidate = None
    for c in candidates:
        if c['id'] == int(candidate_id):
            candidate = c
            break
    return candidate


def get_candidates_by_name(candidate_name, candidates):
    candidates_by_name = []
    for c in candidates:
        if candidate_name.lower() in c['name'].lower():
            candidates_by_name.append(c)
    return candidates_by_name


def get_candidates_by_skill(skill_name, candidates):
    candidates_by_skill = []
    for c in candidates:
        if skill_name.lower() in c['skills'].lower():
            candidates_by_skill.append(c)
    return candidates_by_skill
