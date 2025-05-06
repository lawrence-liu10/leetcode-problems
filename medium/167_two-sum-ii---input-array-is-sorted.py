# 167. Two Sum Ii - Input Array Is Sorted
# Difficulty: Medium

# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# two pointer problem
# check if arr[r] - arr[l] <, =, > the target
# shift right pointer if too big, vice versa

# time to solve: 10 min
# O(n) time
# O(1) space
def solution(numbers: list[int], target: int) -> list[int]:
    
    left = 0
    right = len(numbers) - 1

    while (left < right):
        if numbers[right] + numbers[left] == target:
            return [left + 1, right + 1]
        elif numbers[right] + numbers[left] > target:
            right -= 1
        else:
            left += 1


def main():
    
    numbers = [2,7,11,15]
    target = 9

    numbers2 = [2,3,4]
    target2 = 6

    print(solution(numbers, target))
    print(solution(numbers2, target2))


if __name__ == "__main__":
    main()
