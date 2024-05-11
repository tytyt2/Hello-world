print("Для игры вам необходмо ввести 2 числа, пример поля ниже")
print("Пример поля:")
print("     0   1   2")
print(" 0 [00][01][02]")
print(" 1 [10][11][12]")
print(" 2 [20][21][22]")
print()
print()
name_1=input("Введите имя Игрока №1:")
name_2=input("Введите имя Игрока №2:")

board=[[" " for i in range(3)] for j in range(3)]
def invite_x():
    while True:
        print(f"Ход Игорока {name_1}, у вас X:")
        print("Пример поля:")
        print("     0   1   2")
        print(" 0 [00][01][02]")
        print(" 1 [10][11][12]")
        print(" 2 [20][21][22]")
        try:
            row = int(input("row"))
            col = int(input("col"))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                elif board[row][col]=="X":
                        print("Тут вы уже поставили, выбери другое место")
                elif board[row][col]=="O":
                        print("Жульничать не хорошо, выбери другое место")
                        continue
            else:
                print("Неверное значение, введите цифру от 0 до 2х")
        except ValueError:
            print("Введите цифру от 0 до 2х")

    for new in board:
        print(new)
    print()


def invite_o():
    while True:
        print(f"Ход Игорока {name_2}, у вас O:")
        print("Пример поля:")
        print("     0   1   2")
        print(" 0 [00][01][02]")
        print(" 1 [10][11][12]")
        print(" 2 [20][21][22]")
        try:
            row = int(input("row"))
            col = int(input("col"))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = "O"
                    break
                elif board[row][col]=="O":
                    print("Тут вы уже поставили, выбери другое место")
                elif board[row][col]=="X":
                    print("Жульничать не хорошо, выбери другое место")
                    continue

            else:
                print("Неверное значение, введите цифру от 0 до 2х")
        except ValueError:
            print("Введите цифру от 0 до 2х")
    for new in board:
        print(new)
    print()


def change_winner():
    if (board[0][0] == board[0][1] == board[0][2] =="X" or
            board[1][0] == board[1][1] == board[1][2] =="X" or
            board[2][0] == board[2][1] == board[2][2] =="X" or
            board[0][0] == board[1][0] == board[2][0] =="X" or
            board[0][1] == board[1][1] == board[2][1] =="X" or
            board[0][2] == board[1][2] == board[2][2] =="X" or
            board[0][0] == board[1][1] == board[2][2] =="X" or
            board[0][2] == board[1][1] == board[2][0] =="X"):
        print(f"Выйграл игрок: {name_1} ")
        return "X"
    elif (board[0][0] == board[0][1] == board[0][2] =="O" or
          board[1][0] == board[1][1] == board[1][2] =="O" or
          board[2][0] == board[2][1] == board[2][2] =="O" or
          board[0][0] == board[1][0] == board[2][0] =="O" or
          board[0][1] == board[1][1] == board[2][1] =="O" or
          board[0][2] == board[1][2] == board[2][2] =="O" or
          board[0][0] == board[1][1] == board[2][2] =="O" or
          board[0][2] == board[1][1] == board[2][0] =="O"):
        print(f"Выйграл игрок:{name_2} ")
        return "O"
    elif (board[0][0] !=" " and board[0][1] !=" " and board[0][2] !=" " and
          board[1][0] !=" " and board[1][1] !=" " and board[1][2] !=" " and
          board[2][0] !=" " and board[2][1] !=" " and board[2][2] !=" "):
        print("Ничья")
        return "Ничья"




def play():
    while True:
        invite_x()
        invite_o()
        if change_winner():
            break


#End game#

play()
