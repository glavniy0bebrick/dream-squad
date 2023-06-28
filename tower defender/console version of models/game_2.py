import numpy as np
while True:
    field = np.array([[1,0,0,0,0,0,2],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [3,0,0,0,0,0,4]])
    players_x = np.array([[1,7,1,7]])
    players_y = np.array([[1,1,4,4]])
    player = 0
    turn = 0
    if turn == player:
        move = input("выберите куда идти:")
        if move == 1:
            if players_x[player] >= 2:
                players_x[player] -= 1
        elif move == 2:
            if players_y[player] <= 2:
                players_y[player] += 1
        elif move == 3:
            if players_x[player] <= 6:
                players_x[player] += 1
        elif move == 4:
            if players_y[player] >= 3:
                players_y[player] -= 1
        x = np.transpose(np.nonzero(field == 1))
        #x = np.argwhere(field == player + 1)
        print(x)
        field[x[0]][x[1]] = 5
        print(field[x[0]][x[1]])
        print(field)
