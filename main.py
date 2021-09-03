# функция отрисовывает игровое поле после каждого хода,
# отображая поставленный игроком знак на нужных координатах
def wall_builder(value):
    roof = ' --- --- --- '
    wall_element = ' | '
    line = 0
    row = 0
    wall = '| '
    while line < 3:
        print(roof)
        while row < 3:
            wall = wall + f'{value[line][row]}' + wall_element
            row += 1
        print(wall)
        wall = '| '
        row = 0
        line += 1
    print(roof)

# проверяет наличие победы на поле
def line_checker(game):
    # смотрим горизонтальные
    for line in range(3):
        if game[line][0] != 0:
            if game[line][0] == game[line][1] == game[line][2]:
                print (f'{game[line][0]} won!')
                return True
    # смотрим вертикальные
    for row in range(3):
        if game[0][row] != 0:
            if game[0][row] == game[1][row] == game[2][row]:
                print (f'{game[0][row]} won!')
                return True
    # смотрим диагональные
    if game[1][1] != 0:
        if game[0][0] == game[1][1] == game[2][2]:
            print (f'{game[0][0]} won!')
        elif game[1][1] == game[2][0] == game[0][2]:
            print (f'{game[2][0]} won!')
            return True
    return False

# проверяет наличие свободных клеток на поле
# для остановки игры в случае ничьей
def any_turns_left(board):
    for line in board:
        if 0 in line:
            return True
    print('its a draw, well played')
    return False

# передает ход следующему игроку
def turn_change(old_turn):
    if old_turn == 'x':
        new_turn = 'o'
    elif old_turn == 'o':
        new_turn = 'x'
    global turn
    turn = new_turn
    return turn

# проверяет не выходят ли за границы поля координаты пользователя
def check_if_in_range(user_coordinate):
    if int(user_coordinate[0]) not in range(1, 4) or int(user_coordinate[1]) not in range(1, 4):
        return False
    return True

# останавливает игру
def stop_the_game():
    global triggered
    triggered = True
    return triggered

# проверка на корректность ввода пользователя
def is_input_ok(user_input):
    check = True
    for n in user_input:
        if n!=',':
            try:
                check = int(n)
                print (n)
            except ValueError:
                check = False
                print (check)
                break
    if user_input != 'stop' and check == False:
        print('i dont know what to do with it, gimme coordinates or ask me to stop, im really busy atm')
        return False
    return True

# реализация хода игрока
def player_turn(symbol, board):
    # прием координат
    user_coordinate = input()

    while is_input_ok(user_coordinate) == False:
        user_coordinate = input()
        is_input_ok(user_coordinate)
        if user_coordinate == 'stop':
            stop_the_game()
            return

    # остановка игры при вводе команды stop, вместо координат
    if user_coordinate == 'stop':
        stop_the_game()
        return
    else:
        user_coordinate = user_coordinate.split(',')
    # проверка на выход за границы
    while check_if_in_range(user_coordinate) == False:
        print('Вы вышли за границу поля, попробуйте другие координаты')
        user_coordinate = input()
        if user_coordinate == 'stop':
            stop_the_game()
            return
        else:
            user_coordinate = user_coordinate.split(',')
    # перевод координат игрока из str в int
    user_coordinate_int = []
    for n in user_coordinate:
        n = int(n) - 1
        user_coordinate_int.append(int(n))
    board_square = board[user_coordinate_int[0]][user_coordinate_int[1]]
    # проверка на возможность сделать ход по координатам пользователя
    if board_square != 0:
        print(f'{symbol} not allowed here')
        turn_change(symbol)
        return
    else:
        board[user_coordinate_int[0]][user_coordinate_int[1]] = symbol
        wall_builder(board)


board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
wall_builder(board)
turn = 'x'
triggered = False

while any_turns_left(board) and triggered == False and line_checker(board) == False:
    player_turn(turn, board)
    turn_change(turn)