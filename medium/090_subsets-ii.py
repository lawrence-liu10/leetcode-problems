# 090. Subsets Ii
# Difficulty: Medium

# Link: https://leetcode.com/problems/subsets-ii/

# this seems very similar to combination sum II
# let's start by sorting to avoid duplicates
# we implement the same logic from combination sum II, where if there's consecutive same numbers,
#   we only count the first one in each recursive step to avoid duplicates
# otherwise, we explore a new option and pop after each exploration
def solution(self, nums: list[int]) -> list[list[int]]:

    sol = []
    nums.sort()

    def dfs(start, path):
        sol.append(path.copy())

        for i in range(start, len(nums)):
            if nums[i] == nums[i - 1] and i != start:
                continue

            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
    
    dfs(0, [])
    return sol

def main():
    pass

if __name__ == "__main__":
    main()
