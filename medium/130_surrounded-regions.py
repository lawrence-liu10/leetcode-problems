# 130. Surrounded Regions
# Difficulty: Medium

# Link: https://leetcode.com/problems/surrounded-regions/description/

# for this problem, my general approach is this
# look for o's on the edge, and work inwards while there's os, setting them to a temporary 'a' for example
# afterwards, go through and set all remaining o's to xs, and reset the 'a's to os
def solution(self, board: list[list[str]]) -> None:
    
    rows, cols = len(board), len(board[0])

    def dfs(row, col):
        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            board[row][col] == "X" or
            board[row][col] == "a"):
            return
        
        board[row][col] = "a"

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for hor, vert in directions:
            new_row, new_col = row + hor, col + vert
            dfs(new_row, new_col)
    
    for row in range(rows):
        dfs(row, 0)
        dfs(row, cols - 1)

    for col in range(cols):
        dfs(0, col)
        dfs(rows - 1, col)

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "O":
                board[row][col] = "X"

            elif board[row][col] == "a":
                board[row][col] = "O"
    
    #done



def main():
    pass

if __name__ == "__main__":
    main()
