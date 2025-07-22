# 213. House Robber Ii
# Difficulty: Medium

# Link: https://leetcode.com/problems/house-robber-ii/description/

# extremely similar to house robber
# we'll just add one more check, where we won't rob the last house if it started on the first house and vice versa
#   otherwise it's the same. it's not that elegant, but I'll do that for now
def solution(self, nums: list[int]) -> int:
    
    if len(nums) == 1:
        return nums[0]
    
    def rob(sub_arr):
        prev2, prev1 = 0, 0
        for num in sub_arr:
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp
        return prev1
    
    return max(rob(nums[1:]), rob(nums[:-1]))



def main():
    pass

if __name__ == "__main__":
    main()
