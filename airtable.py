from pyairtable import Api
from pprint import pprint


api = Api('patSxQtpMd6a4iKOq.83e528e67458f9fbce584126c80b9f5fd518401f5aa629591a7264ecbba04082')
sport_table = api.table('appeNb48kX0169buS', 'tblS4WhViKaVEWkcO')
section_table = api.table('appeNb48kX0169buS', 'tblVQ1TvSKcuT8j9f')

DB_ID = 'appeNb48kX0169buS'
sport_id = 'tblS4WhViKaVEWkcO'
section_id = 'tblVQ1TvSKcuT8j9f'

curl = f'https://api.airtable.com/v0/{DB_ID}/%D0%A1%D0%BF%D0%BE%D1%80%D1%82?maxRecords=3&view=Main%20View'

headers = {
    'Authorization': f"Bearer ",
    'Content-Type': 'application/json'
}
# connepatSxQtpMd6a4iKOq.d7963b47ef518290e0df426945ddbe6cad681d6a0234bdf3c6a555c43d9c0df1ction (User ID: usrB0Qw3hx2CRgHQL)

def get_sport():
    return sport_table.all()


# print()

def get_section(sport=None):
    if sport is None:
        return section_table.all()
    else:
        return 'в разработке'



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
