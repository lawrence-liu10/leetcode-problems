# 015. 3Sum
# Difficulty: Medium

# Link: https://leetcode.com/problems/3sum/description/

# first idea is to sort. we have base pointer (starts at 0, goes to n - 2), l, r
# we want a[r] - a[l] == base
# if equal, and distinct (we'll sort the tuples), we add to the list
# I believe we can do things with tuples and sets to make it faster,
# but I'll try just implementing it first

# slight update on implementation, we're going to keep moving base, l and r
# while they equal the one in front of them
# I lied, this doesn't account for two of the same number being in the solution

# nums[l] + nums[r] = -nums[b]
# my solution works, but it's too slow
# need to optimize
# let's look back at the equaling one in front idea
# we need to implement this somehow
# the base can always be moved until it's unique

def solution(nums: list[int]) -> list[list[int]]:

    nums = sorted(nums)
    b = 0
    l = 1

    triplets = []

    for b in range(len(nums)):
        if b > 0 and nums[b] == nums[b - 1]: # only unique nums
            continue
        l = b + 1
        r = len(nums) - 1
        while l < r:
            if nums[r] + nums[l] + nums[b] == 0:
                ans = [nums[b], nums[l], nums[r]]
                triplets.append(ans)
                l += 1
                while l < r and nums[l] == nums[l - 1]: # unique
                    l += 1
            elif nums[r] + nums[l] + nums[b] > 0:
                r -= 1
            else:
                l += 1
        b += 1

    return triplets

def main():

    nums = [-1,0,1,2,-1,-4] #[[-1,-1,2],[-1,0,1]]
    print(solution(nums))

    nums = [0,1,1]# []
    print(solution(nums))

if __name__ == "__main__":
    main()
