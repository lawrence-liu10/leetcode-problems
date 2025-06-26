# 040. Combination Sum II
# Difficulty: Medium

# Link: https://leetcode.com/problems/combination-sum-ii/description/

# similar to combination sum one, but we can only use nums once
# we can almost use the same solution, but right now duplicates cause errors
# how do we avoid duplicates
# when backtracking, we pass the next element to avoid using the same element twice
# as well, if there's multiple of the same element, we only want to use each once
#   so we skip consecutive duplicate elements UNLESS it's our first time seeing them
#   if we skip without considering them we miss solutions

def solution(self, candidates: list[int], target: int) -> list[list[int]]:
    sol = []

    def dfs(start, path, sum):
        if sum == target:
            sol.append(path.copy())
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if sum + candidates[i] > target:
                break
            
            path.append(candidates[i])
            dfs(i + 1, path, sum + candidates[i])
            path.pop()
    
    dfs(0, [], 0)
    return sol
        

def main():
    pass

if __name__ == "__main__":
    main()
