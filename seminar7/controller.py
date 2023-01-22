import model
import view

            
def start():
    while True:
        user_inp = view.user_input(model.get_db())
        input_handler(user_inp)


def input_handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.get_db())
        case 2:
            model.read_db('database.txt')
            view.db_success(model.get_db)
        case 3:
            view.save_file('database.txt',model.get_db())
        case 4:
            new_contact=view.create_contact(model.get_db())
            model.set_db(new_contact)
            view.save_file('database.txt',model.get_db())
        case 5:    
            view.change_contact(model.get_db())
        case 6:
            view.find_contact(model.get_db())
        case 7:
            view.remove_contact(model.get_db())
        case 8:
            view.exit_program()
