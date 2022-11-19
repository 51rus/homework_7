import json


def load_students(filename):
    """Загружает список студентов из файла"""
    with open(filename, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def load_professions(filename):
    """Загружает список профессий из файла"""
    with open(filename, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_student_by_pk(pk, data):
    """Получает словарь с данными студента по его pk"""
    for i in data:
        if pk == i['pk']:
            return i


def get_profession_by_title(title, data):
    """Получает словарь с инфо о профе по названию"""
    for i in data:
        if title == i['title']:
            return i


def check_fitness(student, profession):
    """Возвращает словарь получив студента и профессию"""
    set_student = set(student['skills'])
    set_profession = set(profession['skills'])

    has_skills = set_student.intersection(set_profession)
    lacks_skills = set_profession.difference(set_student)

    fit_percent = round(len(has_skills) / len(set_profession) * 100)

    dict_result = {
        'has': has_skills,
        'lacks': lacks_skills,
        'fit_percent': fit_percent,
    }
    return dict_result


def show_result(data, name):
    """Выводит результаты"""
    str_has = ', '.join(data['has'])
    str_lacks = ', '.join(data['lacks'])
    str_output = f'Пригодность {data["fit_percent"]}%\n' \
                 f'{name} знает {str_has}\n' \
                 f'{name} не знает {str_lacks}\n'
    return str_output
