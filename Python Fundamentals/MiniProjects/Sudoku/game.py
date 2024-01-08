def show(x):
    for row in x:
        print(row)


def vertical_check(game_board:list):
    for i in range(9):
        col = []
        unique_col = []
        for row in game_board:
            row_list = []
            for subrow in row:
                for num in subrow:
                    row_list.append(num)
            col.append(row_list[i])
            if row_list[i] not in unique_col:
                unique_col.append(row_list[i])
        if len(col) != len(unique_col):
            return False
    return True


def horizontal_check(game_board):
    for row in game_board:
        row_c = []
        for subrow in row:
            row_c.append([x for x in subrow])
            unique_row_c = []
            for num in row_c:
                if num not in unique_row_c:
                    unique_row_c.append(num)
            if  len(unique_row_c) != len(row_c):
                return False
    return True    


def square_check(square_list:list):
    for square in square_list:
        sq_c = []
        unique_sq_c = []
        for row in square:
            for num in row:
                sq_c.append(num)
                if num not in unique_sq_c:
                    unique_sq_c.append(num)
        if len(unique_sq_c) != len(sq_c):
            return False
    return True
              

row1 = [[1,6,8], [4,5,7], [9,3,2]]
row2 = [[5,7,2], [3,9,1], [4,6,8]]
row3 = [[9,3,4], [6,2,8], [5,1,7]]
row4 = [[8,2,9], [7,4,3], [1,5,6]]
row5 = [[6,5,1], [2,8,9], [3,7,4]]
row6 = [[7,4,3], [5,1,6], [2,8,9]]
row7 = [[3,9,5], [8,7,2], [6,4,1]]
row8 = [[4,1,7], [9,6,5], [8,2,3]]
row9 = [[2,8,6], [1,3,4], [7,9,5]]

board = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

show(board)
    
sq1 = [row[0] for row in board[:3]]
sq2 = [row[1] for row in board[:3]]
sq3 = [row[2] for row in board[:3]]

sq4 = [row[0] for row in board[3:6]]
sq5 = [row[1] for row in board[3:6]]
sq6 = [row[2] for row in board[3:6]]
        
sq7 = [row[0] for row in board[6:]]
sq8 = [row[1] for row in board[6:]]
sq9 = [row[2] for row in board[6:]]


sq_list = [sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9]

if horizontal_check(board) and vertical_check(board) and square_check(sq_list):
    print('Valid Game')
else:
    print('Invalid')
