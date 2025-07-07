# 695. Max Area Of Island
# Difficulty: Medium

# Link: https://leetcode.com/problems/max-area-of-island/description/

# it's similar to number of islands
# we can run dfs from each square, and when we find an island, we explore each cell and set to zero,
# incrementing the island size
def solution(self, grid: list[list[int]]) -> int:
    
    rows = len(grid)
    cols = len(grid[0])

    max_area = 0

    def dfs(row, col) -> int:

        if (row < 0 or col < 0 or
            row >= rows or col >= cols or
            grid[row][col] == 0):
            return 0
        
        grid[row][col] = 0

        return (1 + dfs(row - 1, col) +
                dfs(row + 1, col) +
                dfs(row, col - 1) + 
                dfs(row, col + 1))
    
    for row in range(rows):
        for col in range(cols):
            size = dfs(row, col)
            max_area = max(max_area, size)

    return max_area


    


def main():
    pass

if __name__ == "__main__":
    main()
