# 853. Car Fleet
# Difficulty: Medium

# Link: https://leetcode.com/problems/car-fleet/

# initial thoughts:
# we can graph this as a bunch of lines, where once two lines intersect, we only keep the one with the lower slope
# how can we use this to code it

# first, will lines always intersect at whole numbers? for now I'll assume yes to simplify iterating
# let's look at the input [2,4,1,1,3], pos [10,8,0,5,3]
# can we sort by the highest speeds [4,3,2,1,1], giving us [8,3,10,0,5]
# this won't tell us if we pass another car though

# what if we sort by distances, and calculate the time taken for each
# intersection points don't matter then
# to reach the end, that gives us [10,8,5,3,0], time taken for each is
# [1,1,7,3,12] (target - pos) / speed
# if the left value is less than the right value, it's ahead of and faster than the next car
# if it's equal or greater than the right value, we keep going right until we get a value larger than it
# all of the ones we popped are a fleet, because they were faster than the slowest car, but started behind it so slowed to its speed.

# time to solve: 45 min
# time complexity: O(nlogn)
# space complexity: O(n)

def solution(target: int, position: list[int], speed: list[int]) -> int:

    fleets = 0
    cars = dict(sorted(zip(position, speed))) # cars sorted by initial position
    stack = []

    for pos, s in (cars.items()):
        stack.append((target - pos) / s)

    cur_max = -1
    while stack:
        temp = stack.pop()
        if temp > cur_max:
            fleets += 1
            cur_max = temp

    return fleets





def main():
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3] #3
    print(solution(target, position, speed))

    target = 100
    position = [0,2,4]
    speed = [4,2,1] #1
    print(solution(target, position, speed))

if __name__ == "__main__":
    main()
