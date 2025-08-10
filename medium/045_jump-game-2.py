# 045. Jump Game 2
# Difficulty: Medium

# Link: https://leetcode.com/problems/jump-game-ii/description/

# at first my solution was to simply add a counter to jump game 1
#   doesn't work though, may unnecessarily increment the counter
# instead, we'll only update the counter when we've reached the current max
#   we'll only update the current max to the possible max when we hit the limit
def solution(self, nums: list[int]) -> int:
    cur_max = next_max = 0
    count = 0
    for i in range(len(nums)):
        if cur_max >= len(nums) - 1:
            return count
        next_max = max(next_max, i + nums[i])
        if i == cur_max:
            count += 1
            cur_max = next_max
    return -1

def main():
    pass

if __name__ == "__main__":
    main()
