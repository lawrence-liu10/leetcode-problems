# 001. Two Sum
# Difficulty: Easy

# Link: https://leetcode.com/problems/two-sum/description/
# problem: return indices of two numbers that add to a target num


# brute-force solution, check all pairs
def solution1(nums, target):
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result = {i, j}
                return result




def main():
    nums = [2,7,11,15]
    target = 9

    result = solution1(nums, target)
    
    print(f"answer: {result}")


if __name__ == "__main__":
    main()