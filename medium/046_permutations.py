# 046. Permutations
# Difficulty: Medium

# Link: https://leetcode.com/problems/permutations/description/

# base case: if we have an arr of length nums, it's a valid solution
# for our recursive step: we keep track of the numbers we used, and if we didn't use a num
#   we use it to explore, before popping and continuing
def solution(self, nums: list[int]) -> list[list[int]]:

    sol = []

    def backtrack(path, used):
        if len(path) == len(nums):
            sol.append(path.copy())
        
        for i in range(len(nums)):
            if not used[i]:
                path.append(nums[i])
                used[i] = True

                backtrack(path, used)

                path.pop()
                used[i] = False
    
    result = []
    backtrack([], [False] * len(nums))
    return result

    

def main():
    pass

if __name__ == "__main__":
    main()
