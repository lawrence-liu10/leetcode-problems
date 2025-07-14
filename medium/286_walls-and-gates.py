# 286. Walls And Gates
# Difficulty: Medium

# Link: https://neetcode.io/problems/islands-and-treasure

from collections import deque

# looks like we can do it with a queue
# we start from each treasure chest, 0 and explore
#   if out of bounds or a water cell, return
#   when we reach a land cell, if the steps to reach it + 1 is lower than it, replace it
#       as well, continue exploring from it and mark it as explored
def solution(self, grid: list[list[int]]) -> None:
    
    queue = deque()
    visited = set()
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                queue.append((row, col))
                visited.add((row, col))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        row, col = queue.popleft()
        
        for hor, vert in directions:
            r, c = row + hor, vert + col
            if (r >= 0 and r < rows and
                c >= 0 and c < cols and
                grid[r][c] != -1):
                if (r, c) not in visited:
                    grid[r][c] = grid[row][col] + 1
                    visited.add((r, c))
                    queue.append((r,c))


def main():
    pass

if __name__ == "__main__":
    main()
