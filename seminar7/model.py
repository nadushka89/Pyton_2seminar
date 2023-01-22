db_list = []

"""Возврат списка контактов"""
def get_db() -> list:
    global db_list
    return db_list

def read_db(path: str):
    with open(path, 'r', encoding='UTF-8') as data:
        data_list = data.readlines()
        for line in data_list:
            contact_info = line.strip().split(';')
            key_info = ['ID', 'Lastname', 'Firstname', 'phone', 'Comment']
            dict_contact = dict(zip(key_info, contact_info))
            set_db(dict_contact)

"""Добавление элемента в список контактов"""
def set_db(new_data: dict) -> list:
    db_list.append(new_data)
    return db_list












