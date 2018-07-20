field = [0,0,0,0,0,0,0,0,0]
player1 = 1
player2 = 2
player = 2
gameEnd = False

def playerInput():
    return int(input("Player" + str(player) +" Enter Field:"))

def placement(player, selection):
    if field[selection-1] == 0:
        field[selection-1] = player
        return True
    elif field[selection-1] != 0:
        print("Field already occupied!")
        return False

def board():
    s_field = []
    for i in field:
        if i == 0:
            s_field.append(" ")
        if i == 1:
            s_field.append("X")
        if i == 2:
            s_field.append("O")
    print(f'{s_field[6]}|{s_field[7]}|{s_field[8]}')
    print(f'{s_field[3]}|{s_field[4]}|{s_field[5]}')
    print(f'{s_field[0]}|{s_field[1]}|{s_field[2]}')

def clearBoard():
    print("\n"*100)

def gameEnd():
    if field[8] == field[5] == field[2] == player:
        print("Player" + str(player) + " won!")
        return True
    if field[6] == field[7] == field[8] == player:
        print("Player" + str(player) + " won!")
        return True
    if field[6] == field[4] == field[2] == player:
        print("Player" + str(player) + " won!")
        return True
    if field[7] == field[4] == field[1] == player:
        print("Player" + str(player) + " won!")
        return True
    if field[3] == field[4] == field[5] == player:
        print("Player" + str(player) + " won!")
        return True
    if field[8] == field[4] == field[0] == player:
        print("Player" + str(player) + " won!")
        return True
    if field[6] == field[3] == field[0] == player:
        print("Player" + str(player) + " won!")
        return True
    if field[0] == field[1] == field[2] == player:
        print("Player" + str(player) + " won!")
        return True
    if field.count(0) == 0:
        print("Tie! Better luck next time.")
        return True
    else:
        return False

def changePlayer(currPlayer):
    if currPlayer == 1:
        return 2
    else:
        return 1

while gameEnd() == False:
    board()
    player = changePlayer(player)
    selection = playerInput()
    #player = changePlayer(player)

    while placement(player, selection) == False:
        selection = playerInput()

    clearBoard()
board()
    

    
    


