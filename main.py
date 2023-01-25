from flask import Flask
from utils import *

app = Flask(__name__)

@app.route('/')
def main_page():
    return info_candidates(load_candidates())


@app.route('/candidates/<int:x>')
def candidate_page(x):
    picture = get_by_pk(x)["picture"]
    return f'<img src={picture}>\n{info_candidates([get_by_pk(x)])}'


@app.route('/skills/<x>')
def skills_page(x):
    skills = get_by_skill(x)
    return f'{info_candidates(skills)}'


app.run()
