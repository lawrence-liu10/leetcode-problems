# 078. Subsets
# Difficulty: Medium

# Link: https://leetcode.com/problems/subsets/description/

# backtracking problem
# the general pattern to solving backtracking is, while the problem isn't solved,
# we pick a path from the starting point, and if it's valid we recurse with it
#   then 'unchoose' it before continuing

def solution(self, nums: list[int]) -> list[list[int]]:
    
    def backtrack(start, path):
        sol.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(start + 1, path)
            path.pop()
    
    sol = []
    backtrack(0, [])
    return sol
    

def main():
    pass

if __name__ == "__main__":
    main()
