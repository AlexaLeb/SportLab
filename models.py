from airtable import get_sport, get_section
from pprint import pprint


def shoose_sport(sport: str):
    sport_dic = get_sport()
    for element in sport_dic:
        for el in element['fields']:
            if element['fields']['Спорт'].lower() == sport:
                return element['fields']


def sport_list():
    sport_list = []
    sport_dic = get_sport()
    for element in sport_dic:
        for el in element['fields']:
            sport_list.append(element['fields']['Спорт'])
    return set(sport_list)


def choose_section(sport=None):
    sections = get_section(sport)
    return get_section()


def sections(sport=None):
    sect = []
    sports = shoose_sport(sport)
    sports_amount = sports['секции']
    sections_d = choose_section()
    # pprint(sports_amount)
    # print()
    for element in sections_d:
        if element['id'] in sports_amount:
            element['fields'].pop('Спорт')
            sect.append(element['fields'])
    text = create_text(sect)
    return text


def create_text(text):
    tx = []
    for t in text:
        a = f'<b>{t["section_name"]}</b>\n\n'
        t.pop("section_name")
        for i in t.items():
            a += (f'{i[0]}: {i[1]} \n')
        tx.append(a)
    print(tx)
    return tx


if __name__ == "__main__":
    sections('футбол')