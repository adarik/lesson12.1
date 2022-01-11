import json

from pip._internal.resolution.resolvelib import candidates


def get_candidates():

    """
получает из списка кондидатов
     :return:
     """
    with open("data/candidates.json", "r") as fp:
        candidates = json.load(fp)

    return candidates


def get_candidates_by_id(can_id):
    """
    Возвращает кандидата по его id из файла
    :param can_id:
    :return:
    """


    candidates = get_candidates()
    for can in candidates:
        if can_id == can["id"]:
           return can


def get_settings():
    """
    Получаем словарь с настройками
    :return:
    """
    with open("data/settings.json", "r") as fp:
        settings = json.load(fp)
    return settings


def get_candidate_by_name(name):
    candidates = get_candidates()
    settings = get_settings()

   candidates_found = []

   for can in candidates:
        if _make_search(name,can["name"], settings['case-sensitive']):
          candidates_found.append(can)

   return candidates_found


def get_candidates_by_skill(skill_name):

    candidates = get_candidates()
    settings = get_settings()

    candidates_found = []

    for can in candidates:

        if _make_search(skill_name, can["skills"], settings['case-sensitive']):
            candidates_found.append(can)

    limit = settings["limit"]

    candidates_found = candidates_found[:limit]

    return candidates_found

def _make_search(user_name, search_for, case_sensetive):
    if case-sensitive:
        if search_for in user_name:
            return True
    else:
        if search_for.lower() in user_name.lower():
          return True

    return False