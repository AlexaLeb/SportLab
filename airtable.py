from pyairtable import Api
from pprint import pprint


api = Api('patSxQtpMd6a4iKOq.83e528e67458f9fbce584126c80b9f5fd518401f5aa629591a7264ecbba04082')


DB_ID = 'appeNb48kX0169buS'
sport_id = 'tblS4WhViKaVEWkcO'
section_id = 'tblVQ1TvSKcuT8j9f'
user_id = 'tblKa5uPzW1YDGIco'

sport_table = api.table(DB_ID, sport_id)
section_table = api.table(DB_ID, section_id)
user_table = api.table(DB_ID, user_id)


def get_sport():
    return sport_table.all()


# print()

def get_section(sport=None):
    if sport is None:
        return section_table.all()
    else:
        return 'в разработке'


def create_data(data):
    list_data = get_data()
    for i in list_data:
        if i['fields']['Name'] == str(data):
            user_table.delete(i['id'])
            user_table.create({'Name': data, 'счетчик для опроса': 0})
            return True
    return user_table.create({'Name': data, 'счетчик для опроса': 0})


def get_data():
    return user_table.all()


def update_data(data: list):
    a, b = data
    return user_table.update(str(a), b)

def update_data1(data: list):
    a, b = data
    list_data = get_data()
    for i in list_data:
        if i['fields']['Name'] == str(a):
            user_table.update(i['id'], b)
            print("обновил")
            return True
    return ['Ошибка']




# if __name__ == "__main__":
#     pprint(get_data())
#     data = ['bob', 'счетчик для опроса', 5]
#     print(update_data(data))




    # pprint(section_table.all())
    # pprint(api.base("appeNb48kX0169buS"))
# table.all()
# [
#     {
#         "id": "rec5eR7IzKSAOBHCz",
#         "createdTime": "2017-03-14T22:04:31.000Z",
#         "fields": {
#             "Name": "Alice",
#             "Email": "alice@example.com"
#         }
#     }
# ]
# table.create({"Name": "Bob"})
# {
#     "id": "recwAcQdqwe21asdf",
#     "createdTime": "...",
#     "fields": {"Name": "Bob"}
# }
# table.update("recwAcQdqwe21asdf", {"Name": "Robert"})
# {
#     "id": "recwAcQdqwe21asdf",
#     "createdTime": "...",
#     "fields": {"Name": "Robert"}
# }
# table.delete("recwAcQdqwe21asdf")
# {'id': 'recwAcQdqwe21asdf', 'deleted': True}
