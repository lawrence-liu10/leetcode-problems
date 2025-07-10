# 417. Pacific Atlantic Water Flow
# Difficulty: Medium

# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/description/

# checking every cell to see if it can reach both is extremely inefficient

# lets get the cells that can reach the atlantic and pacific separately
#   and then return the overlap
# for our dfs, when exploring, if the height is >= what it was called on, we mark it as reachable
#   and continue searching
# finally, we'll start from the edges (NW pacific SE atlantic) and explore inwards using the dfs we defined
def solution(self, heights: list[list[int]]) -> list[list[int]]:
    
    rows, cols = len(heights), len(heights[0])
    reaches_atlantic = [[False for _ in range(cols)] for _ in range(rows)] #SE
    reaches_pacific = [[False for _ in range(cols)] for _ in range(rows)] #NW

    def dfs(row, col, reaches):
        if reaches[row][col]:
            return
        
        reaches[row][col] = True
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for hor, vert in directions:
            new_row, new_col = row + hor, col + vert

            if (new_row >= 0 and new_row < rows and
                new_col >= 0 and new_col < cols and
                heights[new_row][new_col] >= heights[row][col]):
                dfs(new_row, new_col, reaches)

    # pacific, NW
    for row in range(rows):
        dfs(row, 0, reaches_pacific)
    for col in range(cols):
        dfs(0, col, reaches_pacific)

    # atlantic, SE
    for row in range(rows):
        dfs(row, cols - 1, reaches_atlantic)
    for col in range(cols):
        dfs(rows - 1, col, reaches_atlantic)

    sol = []
    for row in range(rows):
        for col in range(cols):
            if reaches_atlantic[row][col] and reaches_pacific[row][col]:
                sol.append([row, col])

    return sol

def main():
    pass

if __name__ == "__main__":
    main()
