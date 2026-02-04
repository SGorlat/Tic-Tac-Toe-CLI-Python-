import random



board= [[1,2,3],[4,5,6],[7,8,9]]

cpu='X'
player='O'

board[1][1]=cpu




# Mostrar tablero
def display_board(board):

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

    
    


#Movimiento jugador
def enter_move(board):
   

    while True:
     
        

        try:
            userTurn=int(input("Indica a que casilla de 1-9 desea hacer su movimiento: "))
            if userTurn <1 or userTurn >9:
                print("Numero fuera de rango,debe estar entre 1-9")
                continue
        except ValueError:
            print("Debes introducir un número entre 1-9")
            continue

        for row in range(3):
            for col in range(3):
                if board[row][col] == userTurn:
                    board[row][col] = player
                    return
        print("Casilla ocupada, elige otra.")
    

#Campos libres en tablero
def make_list_of_free_fields(board):
   
    freeMove=[] # En freeMove almacenaremos los indices/coordenadas(en forma de tuplas) donde hay movimientos libres

    # recorremos las 3 filas y dentro de cada fila recorremos sus 3 columnas.
    # validacion: si en el valor de esa posicion(board[i][j]) no es 'X' y no es 'O' significa que esta libre.
    # añadimos los indices de coordenadas en forma de tuplas a la lsita freeMove
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                freeMove.append((i,j))
                    
    return freeMove #retornamos dicha lista
        
    

#¿Hay ganador?
def victory_for(board, sign):
   
    # comprobamos filas
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        
        # comprobamos columnas
    for j in range(3):   
        if board[0][j] == sign and board[1][j] == sign and board[2][j] == sign:
            return True
         
         # comprobamos diagonales
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return True
               
    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
            return True
            
    return False    



         

#Movimiento CPU
def draw_move(board):
    
    moveOptions = make_list_of_free_fields(board)

    if len(moveOptions) == 0:
        return

    cpuTurn = random.choice(moveOptions) # .choice es una funcion del modulo random que elige un elem al azar de una secuencia, en este caso una lista de tuplas: moveOptions(contiene casillas vacias) que viene como rdo de la funcion make_list_of_free_fields(board)

    row = cpuTurn[0]
    col = cpuTurn[1]

    # actualizamos el tablero indicandole que en las coordenas esas ponga 'X'
    board[row][col]= cpu


def playGame():
    while True:
        display_board(board)

        #Turno jugador
        print("TURNO DEL JUGADOR - 'O' ")
        enter_move(board)
        if victory_for(board, player):
            display_board(board)
            print("Ganaste")
            break

        if len(make_list_of_free_fields(board)) == 0: 
            display_board(board)
            print("Empate") 
            break

        # Turno CPU
        print("TURNO DE LA CPU - 'X' ")
        draw_move(board)
        if victory_for(board, cpu): 
            display_board(board)
            print("Gana la CPU")
            break
        if len(make_list_of_free_fields(board)) == 0: 
            display_board(board)
            print("Empate") 
            break

#Esto evita que se ejecute el programa automaticamente al importar el archivo, solo arranca cuando se ejecuta "Run file...", si importamos (import main) en otro archivo.py se ejecutaria el juego y alomejor solo queremos una funcion de este archivo,con este "if __name__..." evitamos que se ejecute a no ser que llamemos a playGame()     
if __name__ == "__main__": playGame()    
    






    
