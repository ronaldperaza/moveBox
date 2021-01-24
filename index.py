import copy


levels = [
    {
        'board': [["#", "#", "#", "#", "#", "#", "#", "#"],  # 0 

                  ["#", ".", ".", ".", "#", ".", ".", "#"],  # 1

                  ["#", ".", "#", ".", "#", ".", ".", "#"],  # 2

                  ["#", ".", ".", ".", ".", ".", ".", "#"],  # 3

                  ["#", ".", "#", ".", "#", ".", ".", "#"],  # 4

                  ["#", ".", ".", ".", "#", ".", ".", "#"],  # 5

                  ["#", "#", "#", "#", "#", ".", ".", "#"],  # 6

                  [".", ".", ".", ".", "#", "#", "#", "#"]],  # 7,
                #   0    1    2    3    4    5    6    7

        'state':  # POSICION DE OBJETOS EN EL TABLERO
        {
            'player': [6, 5],
            'goals': [[2, 6]],
            'boxes': [[2, 5]]
        }
        
    },

]
search_path = []

direction = ""  
current_go = 0  

 
level = levels[current_go]['board']
positions = levels[current_go]['state']
player = levels[current_go]['state']['player']
box_pos = levels[current_go]['state']['boxes']
goal_pos = levels[current_go]['state']['goals']

# prints el tablero en la pantalla
def print_board():  

    temp_board = copy.deepcopy(level)  # creamos una copia del tablero 

    # coloca al jugador en el tablero
    temp_board[player[0]] [player[1]] = "P"  

    for i in range(len(goal_pos)):
        # iteramos en el tablero para mostrar la posicion de destino
        temp_board[goal_pos[i] [0]][goal_pos[i] [1]] = "D"

    for i in range(len(box_pos)):
        # iteramos en el tablero mostrando la posicion de la caja 
        temp_board[box_pos[i] [0]] [box_pos[i] [1]] = "C"

    
    # Formateamos e imprimimos el tablero
    x = 0
    for i in temp_board:
        print(" ".join(temp_board[x]))
        x += 1


# Realizar movientos 
def move_maker():

    global direction
    direction = (input("Realiza Movimientos usando (a,s,w,d): "))

    if direction == "a":
            
        levels[current_go]['state']['player'][1] = levels[current_go]['state']['player'][1] - 1  
        search_path.append('p-l') # jugador a la izquieda se agrega al arreglo

    if direction == "w":

        levels[current_go]['state']['player'][0] = levels[current_go]['state']['player'][0] - 1  
        search_path.append('p-u') # jugador arriba se agrega al arreglo

    if direction == "d":

        levels[current_go]['state']['player'][1] = levels[current_go]['state']['player'][1] + 1  
        search_path.append('p-r') # jugador a la derecha se agrega al arreglo

    if direction == "s":

        levels[current_go]['state']['player'][0] = levels[current_go]['state']['player'][0] + 1 
        search_path.append('p-d') # jugador abajo se agrega al arreglo


# chequeamos si los moviemtos son validos 
def move_check():  

    if direction == "a":
        # mover un paso atras de su posicion
        potential_move = [player[0], player[1] - 1]  
        
        """
            Chequeamos que el jugador al cruzar a la izquierda y 
            al haber una una pared, no pueda seguir avanzando        
        """
        if levels[current_go]['board'][player[0]][player[1]] == "#":
            levels[current_go]['state']['player'][1] = levels[current_go]['state']['player'][1] + 1
        
         #   Chequeamos que el jugador no pueda cruzar a la izquierda con la caja 
         #   al haber una una pared, no puede seguir avanzando        
        
        elif levels[current_go]['board'][player[0]][player[1] - 1] == "#":
            if player in box_pos:
                levels[current_go]['state']['player'][1] = levels[current_go]['state']['player'][1] + 1

        
        # poder mover la caja cuando el jugador este al lado de ella
        elif player in box_pos: 
            x = box_pos.index(player)
            box_pos[x][1] = box_pos[x][1] - 1
            search_path.append('c-l') # caja a la izquieda se agrega al arreglo

    if direction == "d":
        potential_move = [player[0], player[1] + 1]  # mover un paso adelante de su posicion

        #    Chequeamos que el jugador al cruzar a la derecha y 
        #    al haber una una pared, no pueda seguir avanzando        
        if levels[current_go]['board'][player[0]][player[1]] == "#":
            levels[current_go]['state']['player'][1] = levels[current_go]['state']['player'][1] - 1

        #   Chequeamos que el jugador no pueda cruzar a la derecha con la caja 
         #   al haber una una pared, no puede seguir avanzando        
        elif levels[current_go]['board'][player[0]][player[1] + 1] == "#":
            if player in box_pos:
                levels[current_go]['state']['player'][1] = levels[current_go]['state']['player'][1] - 1

        # poder mover la caja cuando el jugador este al lado de ella
        elif player in box_pos: 
            x = box_pos.index(player)
            box_pos[x][1] = box_pos[x][1] + 1
            search_path.append('c-r') # caja a la derecha se agrega al arreglo

    if direction == "w":
        potential_move = [player[0] - 1, player[1]]  # mover un paso arriba

        if levels[current_go]['board'][player[0]][player[1]] == "#":
            levels[current_go]['state']['player'][0] = levels[current_go]['state']['player'][0] + 1 

        elif levels[current_go]['board'][player[0] - 1][player[1]] == "#":
            if player in box_pos:
                levels[current_go]['state']['player'][0] = levels[current_go]['state']['player'][0] + 1

        elif player in box_pos:
            x = box_pos.index(player)
            box_pos[x][0] = box_pos[x][0] - 1
            search_path.append('c-u') # caja arriba se agrega al arreglo

    if direction == "s":
        potential_move = [player[0] + 1, player[1]]  # mover un paso abajo

        if levels[current_go]['board'][player[0]][player[1]] == "#":
            levels[current_go]['state']['player'][0] = levels[current_go]['state']['player'][0] - 1  

        elif levels[current_go]['board'][player[0] + 1][player[1]] == "#":
            if player in box_pos:
                levels[current_go]['state']['player'][0] = levels[current_go]['state']['player'][0] - 1
        

        elif player in box_pos:            
            x = box_pos.index(player)
            box_pos[x][0] = box_pos[x][0] + 1 
            search_path.append('c-d') # caja abajo se agrega al arreglo


def level_completed():

    global current_go
    global goal_pos
    global box_pos
    
# chequeamos que la posisicon de la caja y la de la meta esten en el mismo sitio
    if sorted(box_pos) == sorted(goal_pos):
        print("********************************************")
        print("*Felicitaciones el nivel ha sido completado*")
        print("********************************************")
        print("Estos fueron los movimientos realizados: ", search_path)
        
        

while True:

    print_board()
    move_maker()
    move_check()
    level_completed()
    