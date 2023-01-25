import json


def load_candidates():
    """
    функция загружает данные из файла
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    """
    функция показывает всех кандидатов
    """
    candidats = load_candidates()
    candidats_list = []
    for i in candidats:
        candidats_list.append(i["name"])
    return ', '.join(candidats_list)


def get_by_pk(pk):
    """
    функция возвращает кандидата по pk
    """
    candidats = load_candidates()
    for i in candidats:
        if pk == i['pk']:
            return i


def get_by_skill(skill_name):
    """
    функция возвращает кандидата по навыку
    """
    candidats = load_candidates()
    candidats_list = []
    for i in candidats:
        if skill_name.lower() in i['skills'].lower():
            candidats_list.append(i)
    return candidats_list


def info_candidates(list_with_candidates):
    info_str_ = ''
    for i in list_with_candidates:
        info_str_ += f'''
        Имя кандидата - {i["name"]}
        Позиция кандидата - {i["position"]}
        Навыки через запятую - {i["skills"]}    
        '''
    return f'<pre>{info_str_}</pre>'
