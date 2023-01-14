# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

deskpot =[i for i in range(1,10)]

def draw_desk(deskpot):
    print('------------')
    for i in range(3):
        print ('|', deskpot[0+i*3], '|' , deskpot[1+i*3], '|' ,  deskpot[2+i*3], '|' )
        print('------------')

def take_input(player):
    valid=False
    while not valid:
        answer=int(input(("Поставь " + player + " в любую свободную ячейку ")))
        if answer>=1 and answer <= 9:
            if (str(deskpot[answer-1]) not in "X0"):
                deskpot[answer-1]=player
                valid=True
            else:
                print("Эта клетка занята, попробуй еще")
        else:
            print("Некорректный ввод. Введите от 1 до 9")

def check_win(board):
    win_coord= ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8),(2,4,6))
    for i in win_coord:
        if board[i[0]]==board[i[1]]==board[i[2]]:
            return board[i[0]]
    return False

def main(board):
    win = False
    count = 0
    while not win:
        draw_desk(board)
        if count % 2==0:
            take_input("X")
        else:
            take_input("0")
        count +=1

        if count>4:
            tmp=check_win(board)
            if tmp:
                win=True
                print(tmp, "выиграл!")
                break
        if count==9:
            print("Ничья")
            break
    draw_desk(board)
main(deskpot)

         

