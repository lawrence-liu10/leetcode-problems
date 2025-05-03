# 036. Valid Sudoku
# Difficulty: Medium

# Link: https://leetcode.com/problems/valid-sudoku/description/

# time to solve: 30 min
# looks pretty simple, we can loop through each row, column, and then box
# use a hsm to store values, if there's ever a duplicate, invalid
# time complexity: O(1) (# of squares is capped)
# space complexity: O(1)
# let's code a simple solution first and see if it can be improved after
def solution(board: list[list[str]]) -> bool:
    
    #rows
    for row in range(9):
        row_check = {}
        for col in range(9):
            cell = board[row][col]
            if cell == ".":
                continue
            if row_check.get(cell, 0) != 0:
                return False
            row_check[cell] = 1

    #cols
    for col in range(9):
        col_check = {}
        for row in range(9):
            cell = board[row][col]
            if cell == ".":
                continue
            if col_check.get(cell, 0) != 0:
                return False
            col_check[cell] = 1

    # boxes
    # quad nested loop💀
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            box_check = {}
            for x in range(3):
                for y in range(3):
                    cell = board[i + x][j + y]
                    if cell == ".":
                        continue
                    if box_check.get(cell, 0) != 0:
                        return False
                    box_check[cell] = 1
    
    return True

# you can definitely just make a list of sets
# and only do one passthrough of the whole board rather than 3
# for future me to do
def solution2():
    # TODO
    pass



def main():
    
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]] #true
    print(solution(board))

    board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]] #false
    print(solution(board2))

if __name__ == "__main__":
    main()


# tried multiplying i and x, would just give 0
# used this to think about indices
#[0,0][0,1][0,2]...[0,6][0,7][0,8]
#...
#[3,0][3,1][3,2]...