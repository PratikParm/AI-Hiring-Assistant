candidate_info = {
    "name": None,
    "email": None,
    "phone": None,
    "experience": None,
    "position": None,
    "location": None,
    "tech_stack": None,
    "questions": [],
    "salary": None
}

def update_info(key, value):
    candidate_info[key] = value

def get_info():
    return candidate_info