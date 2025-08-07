# 053. Maximum Subarray
# Difficulty: Medium

# Link: https://leetcode.com/problems/maximum-subarray/

# for this question, this is what I'm thinking
#   we'll keep a running sum, and if it ever goes negative, we'll reset it to the current num, b/c
#   negative sums only decrease future ones
# otherwise, update the max sum as needed
def solution(self, nums: list[int]) -> int:
    cur_sum = max_sum = nums[0]

    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(cur_sum, max_sum)
    
    return max_sum

def main():
    pass

if __name__ == "__main__":
    main()
