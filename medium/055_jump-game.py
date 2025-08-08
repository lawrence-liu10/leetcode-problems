# 055. Jump Game
# Difficulty: Medium

# Link: https://leetcode.com/problems/jump-game/description/

# fun solution
# we can keep track of the maximum reachable index, and if we ever pass that, we can't reach the end
#   otherwise, if we reach the last index then we're good
def solution(self, nums: list[int]) -> bool:
    max_ind = 0
    for i in range(len(nums)):
        if i > max_ind:
            return False
        if i == len(nums) - 1:
            return True
        max_ind = max(i + nums[i], max_ind)

def main():
    pass

if __name__ == "__main__":
    main()
