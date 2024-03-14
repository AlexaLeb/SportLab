from airtable import get_sport, get_section
from pprint import pprint


def shoose_sport(sport: str):
    sport_dic = get_sport()
    for element in sport_dic:
        for el in element['fields']:
            if element['fields']['Спорт'].lower() == sport:
                return element['fields']


def sport_list():
    sport_lis = []
    sport_dic = get_sport()
    for element in sport_dic:
        for el in element['fields']:
            sport_lis.append(element['fields']['Спорт'])
    sport_lists = sorted(set(sport_lis))
    return sport_lists


def choose_section(sport=None):
    sections = get_section(sport)
    return get_section()


def advise_sport(kinds: dict):
    sports = get_sport()
    pool = []
    choosen = []
    end = []
    for element in kinds.items():
        choosen.append(element)
    for element in sports:
        di = {}
        name = element['fields'].pop('Спорт')
        c = element['fields']
        po = []
        for i in c.items():
            po.append(i)
        di[name] = po
        pool.append(di)
    for element in pool:
        same = []
        for k, v in element.items():
            for i in v:
                if i in choosen:
                    same.append(i)
            if len(same) > 12:  # Параметр отвечает за сходство рекомендательной работы
                end.append(k)
    print(end)
    print(len(end))
    return sorted(end)


def sections(sport=None):
    try:
        sect = []
        sports = shoose_sport(sport)
        sports_amount = sports['секции']
        sections_d = choose_section()
        for element in sections_d:
            if element['id'] in sports_amount:
                element['fields'].pop('Спорт')
                sect.append(element['fields'])
        text = create_text(sect)
        return text
    except:
        return ['В нашей базе данных нет этого спорта или секции. Может быть ты написал свой запрос с ошибкой, проверь']


def create_text(text):
    tx = []
    for t in text:
        a = f'<b>{t["section_name"]}</b>\n\n'
        t.pop("section_name")
        for i in t.items():
            a += f'{i[0]}: {i[1]} \n'
        tx.append(a)
    print(tx)
    return tx


d = {
    'Есть ракетка?': 'нет',
    'Командный?': 'нет',
    'С клюшкой?': 'да',
    'С мячом?': 'да',
    'Связан с борьбой?': 'да',
    'Сезонность': 'зима',
    'Сильно физически активный?': 'нет',
    'Стихия': 'горы',
    'в помещении или на улице': 'помещение',
    'достаточно большие финансовые вложения': 'да',
    'популярный в России': 'нет',
    'связан с животными': 'нет',
    'связан с оружием?': 'да',
    'травмоопасный?': 'нет'
}

if __name__ == "__main__":
    advise_sport(d)
