# 739. Daily Temperatures
# Difficulty: Medium

# Link: https://leetcode.com/problems/daily-temperatures/description/

# feels like we should iterate backwards, checking from the right if
# right > right - 1, only works for one day ahead though
# end of arr will always be 0

# idea: we iterate right to left on the arr.
# we keep track of the largest int we've seen, and how far away we've gotten from it
# we also push all numbers onto a stack
# if arr[r] > arr[r-1], set sol arr to 1
# we can pop until we find the closest one that's bigger, but what do we do after?

# can we use two stacks, and pop from one into the other?
# is there a point in doing that? might as well just iterate for each term then

# let's just do a brute force solution first
# almost correct, just the case where n - 1 > n is wrong
# too slow

# go left to right, add to stack, if n < n - 1, pop and set to index distance in stack vs array
# any time we can't instantly pop, keep a running counter of how many things we've seen between
# this only really works for one item though
# nevermind, we can have each stack item also contain the index
# time to solve: 1 hour
# time complexity: O(n)
# space complexity: O(n)

def solution(temperatures: list[int]) -> list[int]:

        sols = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                sols[stack_i] = index - stack_i
            stack.append([temp, index])

        return sols


def main():
    temperatures = [73,74,75,71,69,72,76,73]# [1,1,4,2,1,1,0,0]
    print(solution(temperatures))

    temperatures = [30,40,50,60]# [1,1,1,0]
    print(solution(temperatures))

if __name__ == "__main__":
    main()
