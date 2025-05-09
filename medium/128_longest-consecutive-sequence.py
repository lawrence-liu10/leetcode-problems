# 128. Longest Consecutive Sequence
# Difficulty: Medium

# Link: https://leetcode.com/problems/longest-consecutive-sequence/description/

# inital thought is to sort and iterate, but we need O(n) algorithm
# counting sort runs in O(k + n), but the range is massive compared to the input size

# idea: make a hashmap, check if nums[n] - 1 exists at each point
# how would we keep track of the max count?
# actually this doesn't work because they don't have to appear in linear order
# building off the idea, what if we use a set, recursively checking if n + 1 and n - 1 exist
# before returning the largest number. this would revisit too many values though

# idea 2: add all the values to a set.
# pick a value randomly, then keep popping i + 1 if it exists, and i - 1 into the new set
# actually we don't need to keep the set, just the length
# if the current length is greater than the max, replace

# O(n) time
# O(n) space
# time to solve: 30 minutes

def solution(nums: list[int]) -> int:
    values = set(nums) # just learned about this function
    #for num in nums:
    #    values.add(num)

    longest = 0
    while values:
        cur_length = 1
        base = values.pop()

        upper = base + 1
        while upper in values and values:
            values.remove(upper)
            cur_length += 1
            upper += 1

        lower = base - 1
        while lower in values and values:
            values.remove(lower)
            cur_length += 1
            lower -= 1
        
        if cur_length > longest:
            longest = cur_length

    return longest

def main():
    nums = [100,4,200,1,3,2] # 4
    nums1 = [0,3,7,2,5,8,4,6,0,1] # 9
    nums2 = [1,0,1,2] # 3

    print(solution(nums))
    print(solution(nums1))
    print(solution(nums2))


if __name__ == "__main__":
    main()
