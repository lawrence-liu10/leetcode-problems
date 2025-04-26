# 001. Two Sum
# Difficulty: Easy

# Link: https://leetcode.com/problems/two-sum/description/
# problem: return indices of two numbers that add to a target num


# brute-force solution, check all pairs
# time: O(n^2)
# space: O(1)
def solution1(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i, j]
                return result
            

# hash-map solution, add a num and its index to a map
# check each new num to see if its complement is in the map
# time: O(n)
# space: O(n)
def solution2(nums, target):

    indices = {}
    indices[nums[0]] = 0;

    for i in range(1, len(nums)):
        complement = target - nums[i]
        if complement in indices:
            answer = [indices[complement], i]
            return answer
        else:
            indices[nums[i]] = i




def main():
    nums1 = [2,7,11,15] #[0, 1]
    target1 = 9

    nums2 = [3,2,4] #[1,2]
    target2 = 6


    nums3 = [3,3] #[0,1]
    target3 = 6

    #result = solution1(nums1, target1)
    result = solution2(nums3, target3)

    
    print(f"answer: {result}")


if __name__ == "__main__":
    main()