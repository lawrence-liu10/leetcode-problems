# 079. Word Search
# Difficulty: Medium

# Link: https://leetcode.com/problems/word-search/description/

from collections import deque

# we can define a dfs algorithm
# base cases:
#   going out of bounds, return
#   if the cell we're going to doesn't match the target's current letter, return 
#   if we visited the cell already, return
#   if the cell we're going to matches and the length is the target length, return true
# recursion:
#   each time we reach a new cell, we mark it as visited
#   then we check up, down, left, right starting from each cell
def solution(self, board: list[list[str]], word: str) -> bool:
    
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    def dfs(i, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != word[i]:
            return False
        
        if visited[row][col]:
            return False
        
        if i + 1 == len(word):
            return True
        
        visited[row][col] = True
        exists = (dfs(i + 1, row - 1, col) or
                dfs(i + 1, row + 1, col) or
                dfs(i + 1, row, col - 1) or
                dfs(i + 1, row, col + 1))
        visited[row][col] = False

        return exists
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(0, row, col):
                return True
    
    return False


def main():
    pass

if __name__ == "__main__":
    main()
