# 039. Combination Sum
# Difficulty: Medium

# Link: https://leetcode.com/problems/combination-sum/description/

# my initial thought is to make a decision tree, split while the path isn't larger than the target,
# but this would lead to duplicate lists
# choice, constraint, goal
# start with choice
#   we either choose the current index candidate, or exclude it and move on
# next we check if it's within our constraints
#   constraints: sum is <= target, we return and continue backtracking
#   otherwise, it's a valid solution
# goals (base cases)
#   if the current sum equals the target, we append it to our solutions
#   otherwise we backtrack
# for this problem we need to sort to ensure our combinations are strictly increasing
# without sorting, there could be duplicates in different orders
def solution(self, candidates: list[int], target: int) -> list[list[int]]:
    
    sol = []
    candidates.sort()

    def dfs(i, sum, cur_list):
        if sum == target:
            sol.append(cur_list.copy())
            return
        
        for j in range(i, len(candidates)):
            if sum + candidates[j] > target:
                return
            cur_list.append(candidates[j])
            dfs(j, sum + candidates[j], cur_list)
            cur_list.pop()
    
    dfs(0, 0, [])
    return sol

def main():
    pass

if __name__ == "__main__":
    main()
