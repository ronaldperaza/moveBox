"""
### **Descripción**

La idea es buscar la solución a un juego, en que una persona mueve una caja dentro de una bodega. El juego consiste en una matriz de tamaño `m x n`, donde los elementos pueden ser muralla, piso, persona, caja y destino.

El objetivo es mover la caja `C` al destino `D`. Las reglas:

- El jugador se representa por el caracter `P`.
- El piso se representa por el caracter `.`.
- La muralla se representa por el caracter `#`.
- Existe sólo una caja en el juego, representada por el caracter `C`.
- Existe sólo un destino en el juego, representado por el caracter `D`.
- El jugador no puede caminar arriba de la caja (pero si moverla y posicionarse en el espacio).
- La caja solo se puede mover si el jugador está junto a ella.
- El jugador se puede mover para arriba, abajo izquierda y derecha siempre y cuando se mueva sobre el piso.

### **Tipo de respuesta**

La respuesta tiene que ser un arreglo que muestre las secuencias que el jugador realiza.

- Si el jugador **se mueve** hacia la derecha, se agrega `p-r` al arreglo.
- Si el jugador **se mueve** hacia la izquierda, se agrega `p-l` al arreglo.
- Si el jugador **se mueve** hacia arriba, se agrega `p-u` al arreglo.
- Si el jugador **se mueve** hacia abajo, se agrega `p-d` al arreglo.
- Si el jugador **mueve la caja** hacia la derecha, se agrega `c-r` al arreglo.
- Si el jugador **mueve la caja** hacia la izquierda, se agrega `c-l` al arreglo.
- Si el jugador **mueve la caja** hacia arriba, se agrega `c-u` al arreglo.
- Si el jugador **mueve la caja** hacia abajo, se agrega `c-d` al arreglo.

El tipo de respuesta que debe generar el código es `output = ["p-r", "c-u", "p-r", "c-u", "p-u", "c-u"]`

### Entregable

Al email [recruiting@reversso.cl](mailto:recruiting@reversso.cl), un archivo que contenga el código para ejecutar el programa. La idea es que el archivo tenga la función `search_path(grid)` y al ejecutarla retorne el arreglo.

**Nota:** No necesariamente hay que encontrar el óptimo, solo hay que encontrar un camino factible

**Bonus:** Si encuentras el/los óptimo(s)

### **Ejemplo**

```python
Input:
grid = [["#","#","#","#","#"],
        ["#","#","#","D","#"],
        ["#","#","#",".","#"],
        ["#","#","#",".","#"],
        ["#","P",".","C","#"],
        ["#","#","#","#","#"]]

Output:
> buscar_camino(grid)
> ["p-r", "c-u", "p-r", "c-u", "p-u", "c-u"]
```

### **Cosas a evaluar**

- Que el código funcione para este y otros ejemplos
- Sintaxis del código
- Solución propuesta
- Explicación de la solución


grid = [["#","#","#","#","#"],
        ["#","#","#","D","#"],
        ["#","#","#",".","#"],
        ["#","#","#",".","#"],
        ["#","P",".","C","#"],
        ["#","#","#","#","#"]]  

""" 

# import copy

# levels = [
#     {
#         'board': [["#", "#", "#", "#", "#", "#", "#", "#"],  # 0     

#                   ["#", " ", " ", " ", "#", " ", " ", "#"],  # 1

#                   ["#", " ", "#", " ", "#", " ", " ", "#"],  # 2

#                   ["#", " ", " ", " ", " ", " ", " ", "#"],  # 3

#                   ["#", " ", "#", " ", "#", " ", " ", "#"],  # 4

#                   ["#", " ", " ", " ", "#", " ", " ", "#"],  # 5

#                   ["#", "#", "#", "#", "#", " ", " ", "#"],  # 6

#                   [" ", " ", " ", " ", "#", "#", "#", "#"]],  # 7,
#                 #   0    1    2    3    4    5    6    7
                
#         'state': # objectos en el tablero  
#         {
#             'player': [6, 5], # lugar donde inicia el jugador
#             'goals': [4, 6],
#             'boxes': [3, 5]
#         }
#     },
# ]
# posicion_actual = 0

# posicion = levels[posicion_actual]['state']
# jugador = levels[posicion_actual]['state']['player']
# posicion_caja = levels[posicion_actual]['state']['boxes']
# meta = levels[posicion_actual]['state']['goals']


# def mostrar_tablero():

#     tablero_temporal = copy.deepcopy(levels)  # creamos una copia del tablero

#     tablero_temporal[jugador[0]] [jugador[1]] = "P"   #lugar del jugador en el tablero

#     for i in range(len(meta)):        
#         # iteramos la posicion de la meta en el tablero
#         tablero_temporal[meta[i][0]] [meta[i][1]] = "D"
    
#     for i in range(len(posicion_caja)):        
#         # iteramos la posicion de la caja en el tablero
#         tablero_temporal[posicion_caja[i][0]] [posicion_caja[i][0]] = "C"

#     matchList = [x for x in posicion_caja if x in meta]
#     for i in range(len(matchList)):
#         tablero_temporal[matchList[i][0]][matchList[i][1]] = "*"


#     x = 0
#     for i in tablero_temporal:
#         print(" ".join(tablero_temporal[x]))
#         x += 1


# # def move():
    
# #     global directions
# #     directions = input("Por favor realiza un movimiento usando (a,s,w,d)")

# #     if directions == "d":
# #         buscar_camino.append('p-r')

# #     if directions == "a":
# #         buscar_camino.append('p-l')

# #     if directions == "w":
# #         buscar_camino.append('p-u')

# #     if directions == "s":
# #         buscar_camino.append('p-d')





# # play = True
# print(mostrar_tablero()) 

# # while True:
# #     # move()
# #     print ( buscar_camino)
import copy


levels = [
    {
        'board': [["#", "#", "#", "#", "#", "#", "#", "#"],  # 0     #level 1

                  ["#", " ", " ", " ", "#", " ", " ", "#"],  # 1

                  ["#", " ", "#", " ", "#", " ", " ", "#"],  # 2

                  ["#", " ", " ", " ", " ", " ", " ", "#"],  # 3

                  ["#", " ", "#", " ", "#", " ", " ", "#"],  # 4

                  ["#", " ", " ", " ", "#", " ", " ", "#"],  # 5

                  ["#", "#", "#", "#", "#", " ", " ", "#"],  # 6

                  [" ", " ", " ", " ", "#", "#", "#", "#"]],  # 7,

        'state':  # POSICION DE OBJETOS EN EL TABLERO
        {
            'player': [6, 5],
            'goals': [[2, 6]],
            'boxes': [[2, 5]]
        }
        
    },

]
search_path = []

direction = ""  # assigned in the move function and used in the moveCheck as a reference to undo invalid moves
currentGo = 0  # used to increment levels list item to change level

# assign key placeholder values to reduce complexity of move and check functions
level = levels[currentGo]['board']
positions = levels[currentGo]['state']
player = levels[currentGo]['state']['player']
boxPos = levels[currentGo]['state']['boxes']
goalPos = levels[currentGo]['state']['goals']


def printBoard():  # prints the board to the screen

    tempBoard = copy.deepcopy(level)  # creates a tempboard

    tempBoard[player[0]][player[1]] = "P"  # places player on the board

    for i in range(len(goalPos)):
        # iterate through the board placing goals
        tempBoard[goalPos[i][0]][goalPos[i][1]] = "D"

    for i in range(len(boxPos)):
        # iterate through the board placing boxes
        tempBoard[boxPos[i][0]][boxPos[i][1]] = "C"

    
    x = 0
    for i in tempBoard:
        print(" ".join(tempBoard[x]))  # formats and prints the board
        x += 1



def moveMaker():

    global direction
    direction = (input("Realiza Movimientos usando (a,s,w,d): "))

    if direction == "a":
            
        levels[currentGo]['state']['player'][1] = levels[currentGo]['state']['player'][1] - 1  
        search_path.append('p-l')

    if direction == "w":

        levels[currentGo]['state']['player'][0] = levels[currentGo]['state']['player'][0] - 1  
        search_path.append('p-u')

    if direction == "d":

        levels[currentGo]['state']['player'][1] = levels[currentGo]['state']['player'][1] + 1  
        search_path.append('p-r')

    if direction == "s":

        levels[currentGo]['state']['player'][0] = levels[currentGo]['state']['player'][0] + 1 
        search_path.append('p-d')



def moveCheck():  # checks if move was valid

    if direction == "a":
        potentialMove = [player[0], player[1] - 1]  # one step ahead placeholder

        if levels[currentGo]['board'][player[0]][player[1]] == "#":
            # INVALID wall.
            levels[currentGo]['state']['player'][1] = levels[
                currentGo]['state']['player'][1] + 1

        elif levels[currentGo]['board'][player[0]][player[1] - 1] == "#":  # INVALID box to wall
            if player in boxPos:
                levels[currentGo]['state']['player'][1] = levels[
                    currentGo]['state']['player'][1] + 1

        elif player in boxPos and potentialMove in boxPos:  # INVALID box to Box
            levels[currentGo]['state']['player'][1] = levels[
                currentGo]['state']['player'][1] + 1  # undo

        elif player in boxPos:  # box to space
            x = boxPos.index(player)
            boxPos[x][1] = boxPos[x][1] - 1

    if direction == "d":
        potentialMove = [player[0], player[1] + 1]  # one step ahead placeholder

        if levels[currentGo]['board'][player[0]][player[1]] == "#":
            # INVALID wall.
            levels[currentGo]['state']['player'][1] = levels[
                currentGo]['state']['player'][1] - 1

        elif levels[currentGo]['board'][player[0]][player[1] + 1] == "#":  # INVALID box to wall
            if player in boxPos:
                levels[currentGo]['state']['player'][1] = levels[
                    currentGo]['state']['player'][1] - 1

        elif player in boxPos and potentialMove in boxPos:  # INVALID box to Box
            levels[currentGo]['state']['player'][1] = levels[
                currentGo]['state']['player'][1] - 1  # undo

        elif player in boxPos:  # box to space
            x = boxPos.index(player)
            boxPos[x][1] = boxPos[x][1] + 1  # needs to be changed for other moves

    if direction == "w":
        potentialMove = [player[0] - 1, player[1]]  # one step ahead

        if levels[currentGo]['board'][player[0]][player[1]] == "#":
            levels[currentGo]['state']['player'][0] = levels[
                currentGo]['state']['player'][0] + 1  # INVALID wall

        elif levels[currentGo]['board'][player[0] - 1][player[1]] == "#":
            if player in boxPos:
                levels[currentGo]['state']['player'][0] = levels[
                    currentGo]['state']['player'][0] + 1

        elif player in boxPos and potentialMove in boxPos:  # INVALID box to Box
            levels[currentGo]['state']['player'][0] = levels[
                currentGo]['state']['player'][0] + 1

        elif player in boxPos:  # box to space
            x = boxPos.index(player)
            boxPos[x][0] = boxPos[x][0] - 1

    if direction == "s":
        potentialMove = [player[0] + 1, player[1]]  # one step ahead

        if levels[currentGo]['board'][player[0]][player[1]] == "#":
            print("line 1")
            levels[currentGo]['state']['player'][0] = levels[currentGo][
                'state']['player'][0] - 1  # INVALID into a wall

        elif levels[currentGo]['board'][player[0] + 1][player[1]] == "#":  # box to wall
            print("line 2")
            if player in boxPos:
                levels[currentGo]['state']['player'][0] = levels[
                    currentGo]['state']['player'][0] - 1

        elif player in boxPos and potentialMove in boxPos:  # box to box
            print("line 3")
            levels[currentGo]['state']['player'][0] = levels[currentGo][
                'state']['player'][0] - 1  # INVALID box to box

        elif player in boxPos:  # VALID box to space
            print("line 4")
            x = boxPos.index(player)
            boxPos[x][0] = boxPos[x][0] + 1  # needs to be changed for other moves


def champCheck():  # checks if level is complete

    global currentGo
    global goalPos
    global boxPos
    # global player
    # global positions  # change  ####
    # global level
    # global play

    if sorted(boxPos) == sorted(goalPos):  # checks if goal and box coordinates match
        print("Congratulations you have completed the level.")
        # currentGo += 1  # increments to the next level
        # level = levels[currentGo]['board']  # updates the placeholder vlaues
        # positions = levels[currentGo]['state']
        # player = levels[currentGo]['state']['player']
        # boxPos = levels[currentGo]['state']['boxes']
        # goalPos = levels[currentGo]['state']['goals']
        # if currentGo == 2:  # if level 2 is completed play will be set to false ending the game
        #     play = False


play = True


while play:

    printBoard()
    moveMaker()
    # moveCheck()
    champCheck()
    print(search_path)
