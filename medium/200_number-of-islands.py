# 200. Number Of Islands
# Difficulty: Medium

# Link: https://leetcode.com/problems/number-of-islands/description/

# let's go through with a dfs, and at each step, check if a square is a one or zero
# if it's a one, we'll set it to a zero and keep exploring around it
# if it's a zero, return
# after we've gone around the whole area and there's only zeros, we'll increment our island count
# we have to run dfs starting from every single square though, there might be more efficient approaches
def solution(self, grid: list[list[str]]) -> int:
    
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    def dfs(row, col):

        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            grid[row][col] == "0"):
            return
        
        grid[row][col] == "0"
        
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                dfs(row, col)
                count += 1
    
    return count

def main():
    pass

if __name__ == "__main__":
    main()
