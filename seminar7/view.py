'''Модуль ввода и вывода.'''


def main_menu() -> int:
    '''Главное меню'''
    print('Главное меню.')
    menu_list = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Найти контакт',
                 'Удалить контакт',
                 'Выход'
                 ]
    for i, value in enumerate(menu_list, start=1):
        print(f'\t{i}. {value}')
    print()

def user_input(db: list):
    '''Выбор пользователя'''
    while True:
        try:
            main_menu()
            command = int(input('Введите номер команды -> '))
            if command < 1 or command > 8:
                print('\nВы ввели {command}! Введите номер команды от 1 до 8.\n')
            elif db and command == 2:
                print('\nТелефонный справочник уже открыт!')
            else:
                return command
        except ValueError:
            print('\nНекорректный ввод! Введите номер команды.\n')



def show_all(db: list):
    '''1. Показать все контакты'''
    if db:
        print('\nСписок контактов:')
        for i in range(len(db)):
            print(f'\t{i+1}.', end=' ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()
    else:
        print('\nТелефонный справочник пуст или не открыт.')



def db_success(db: list):
    '''2. Открыть файл'''
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False

     
def save_file(path: str, db: list):
    '''3.Сохранить файл'''  
    print('Вы хотите сохранить изменения?')
    while True:
        user_answer= input("Введите: да или нет  ").lower()
        if user_answer=='да':
            new_data=[]
            for i in range(len(db)):
                new_contact = ''
                for value in db[i].values():
                    new_contact += value + ';'
                new_contact = new_contact[:-1] + '\n'
                new_data.append(new_contact)
            with open(path, 'w', encoding='UTF-8') as data:
                for i in range(len(new_data)):
                    data.write(new_data[i])
            print('\nИзменения сохранены.')
            break
        if user_answer == 'нет':
            print('\nИзменения не сохранены.')
            break
        else:
            print('\nВведите да или нет.\n')


def create_contact(db:list):
    '''4.Создать контакт'''
    print('Создание нового контакта.')
    new_contact = dict()
    new_contact['ID'] = 'id:' + str(len(db) + 1)
    new_contact['lastname'] = input('\tВведите фамилию >: ')
    new_contact['firstname'] = input('\tВведите имя >: ')
    new_contact['phone'] = input('\tВведите телефон >: ')
    new_contact['comment'] = input('\tВведите комментарий >: ')
    print('\nКонтакт добавлен.')
    return new_contact


def change_contact(db: list):
    '''5. Изменить контакт'''
    print('\nИзменение контакта.')
    print('1.Найти контакт\n2. Ввести ID\n3. Отмена.\n')
    while True:
        try:
            answer = int(input('Введите номер команды: '))
            if answer<1 or  answer> 3:
                print('\nНеправильная команда. Введите номер команды от 1 до 3.\n')
            else:
                match answer:
                    case 1:
                        find_contact(db)
                        print('\n1. Найти контакт\n2. Ввести ID\n3. отмена\n')
                    case 2:
                        id = input('Введите ID: ')
                        if id.isdigit() and 1 <= int(id) <= len(db):
                            print(f'\nВнесите данные контакта: id_{id} '
                                  f'{db[int(id) - 1]["Lastname"]} '
                                  f'{db[int(id) - 1]["Firstname"]} '
                                  f'{db[int(id) - 1]["phone"]} '
                                  f'{db[int(id) - 1]["Comment"]}:\n')
                            db[int(id) - 1]['Lastname'] = input('Фамилия: ')
                            db[int(id) - 1]['Firstname'] = input('Имя: ')
                            db[int(id) - 1]['phone'] = input('Номер телефона: ')
                            db[int(id) - 1]['Comment'] = input('Комментарий: ')
                            for i, value in enumerate(db):
                                value['ID'] = 'id:' + str(i + 1)
                            print('\nКонтакт изменен.')
                            return
                        else:
                            print('\nID введен некорректно или отсутствует!')
                            return
                    case 3:
                        print('\nИзменение отменено\n')
                        return
        except ValueError:
            print('\nНекорректный ввод! Введите номер команды\n')


def find_choice() -> tuple:
    '''Поиск по критериям'''
    print('\nКритерии поиска:')
    find_list = [
        'Фамилия',
        'Имя',
        'Фамилия и имя',
        'Номер телефона',
        'ID контакта (численное значение)'
    ]
    for i, value in enumerate(find_list, start=1):
        print(f'\t{i}. {value}')
    print()
    while True:
        try:
            user_choice = int(input('Выберите номер критерия поиска: '))
            if user_choice < 1 or user_choice > 5:
                print('\nВведите номер команды от 1 до 4.\n')
            else:
                find_data = input('Введите данные для поиска в соответствии с критерием: ')
                if user_choice < 5:
                    return user_choice, find_data
                if user_choice == 5 and find_data.isdigit():
                    find_data = 'id:' + str(find_data)
                    return user_choice, find_data
                else:
                    print('\nНекорректный ID!')
        except ValueError:
            print('\nНекорректный ввод!')


def find_contact(db: list):
    '''6.Найти контакт'''
    def show_contact():
        keys = ['Lastname', 'Firstname', 'Lastname_firstname', 'phone', 'ID']
        print('\nКонтакт(ы): ')
        count = 0
        for i in range(len(db)):
            if db[i][keys[find_tuple[0] - 1]].lower() == find_tuple[1].lower():
                print(f'\t{count + 1}', end=' ')
                count += 1
                for value in db[i].values():
                    print(f'{value}', end=' ')
                print()
        if count == 0:
            print('\tКонтакт не найден!')
    if db:
        find_tuple = find_choice()
        match find_tuple[0]:
            case 1:
                show_contact()
            case 2:
                show_contact()
            case 3:
                find_fio = list(find_tuple[1].split())
                if len(find_fio) == 2:
                    print('\nКонтакт(ы): ')
                    count = 0
                    for i in range(len(db)):
                        if db[i]['Lastname'].lower() == find_fio[0].lower() and \
                                db[i]['Firstname'].lower() == find_fio[1].lower():
                            print(f'\t{count + 1}', end='. ')
                            count += 1
                            for value in db[i].values():
                                print(f'{value}', end='. ')
                            print()
                    if count == 0:
                        print('\tКонтакт не найден!')
                else:
                    print('\nНекорректный ввод! Вводите фамилию и имя через пробел!')
            case 4:
                show_contact()
            case 5:
                show_contact()
    else:
        print('\nТелефонный справочник пуст или не открыт.')



def remove_contact(db:list):
    '''7.Удаление контакта'''
    print('Удаление контакта.')
    print('1. Найти контакт\n2. Ввести ID контакта\n3. Отмена.\n')
    # rem = str(input("Пожалуйста, введите ID контакта,который хотите удалить: "))
    while True:
        try:
            num_com = int(input('Введите номер команды: '))
            if num_com<1 or num_com> 3:
                print('\nВведите номер команды от 1 до 3.\n')
            else:
                match num_com:
                    case 1:
                        find_contact(db)
                        print('\n1. Найти контакт\n2. Ввести ID\n3. отмена\n')
                    case 2:
                        id = input('Введите ID: ')
                        if id.isdigit() and 1 <= int(id) <= len(db):
                            db.pop(int(id) - 1)
                            for i, value in enumerate(db):
                                value['ID'] = 'id:' + str(i + 1)
                            print('\nКонтакт удален.\nID контактов обновлены.\n')
                            return
                        else:
                            print('\nID введен некорректно или отсутствует!\n')
                            return
                    case 3:
                        print('\nУдаление отменено\n')
                        return
        except ValueError:
            print('\nНекорректный ввод! Введите номер команды\n')


'''8.Выход'''
def exit_program():
    print('Завершение программы.')
    exit()



    

    




    

