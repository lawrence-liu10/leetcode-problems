# 994. Rotting Oranges
# Difficulty: Medium

# Link: https://leetcode.com/problems/rotting-oranges/description/

from collections import deque

# my initial idea is to dfs through every single square until changes stop occuring
# when changes stop occurring, one more loop to check if it's only rotten/empty
# it seems pretty inefficient, O(k * m * n) for k steps
# i'll implement it for now until i can think of something better

# actually dfs doesn't work because we need the minimum number of minutes
# dfs might not take the most efficient path to spread

# let's implemnt using bfs
# the idea for bfs is to start from any rotten oranges, and keep exploring while there's fresh oranges
# at the end, if there's still any fresh oranges, we return false

# should have used a directions array to remove repetitive code, but otherwise works

def solution(self, grid: list[list[int]]) -> int:
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()

    # helper bounds checker
    def inBounds(row, col):
        if (row < 0 or row >= rows or
            col < 0 or col >= cols):
            return False
        return True


    # initialize deque and orange count
    fresh = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                queue.append([row, col])
            if grid[row][col] == 1:
                fresh += 1

    steps = 0
    while fresh > 0 and queue:
        steps += 1

        for i in range(len(queue)):
            row, col = queue.popleft()

            if inBounds(row - 1, col) and grid[row - 1][col] == 1:
                grid[row - 1][col] = 2
                queue.append([row - 1, col])
                fresh -= 1

            if inBounds(row + 1, col) and grid[row + 1][col] == 1:
                grid[row + 1][col] = 2
                queue.append([row + 1, col])
                fresh -= 1

            if inBounds(row, col + 1) and grid[row][col + 1] == 1:
                grid[row][col + 1] = 2
                queue.append([row, col + 1])
                fresh -= 1

            if inBounds(row, col - 1) and grid[row][col - 1] == 1:
                grid[row][col - 1] = 2
                queue.append([row, col - 1])
                fresh -= 1

    return -1 if fresh else steps





def main():
    pass

if __name__ == "__main__":
    main()
