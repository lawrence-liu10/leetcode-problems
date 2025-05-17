# 875. Koko Eating Bananas
# Difficulty: Medium

# Link: https://leetcode.com/problems/koko-eating-bananas/description/

# some observations,
# if h = # of inputs, then eating speed must equal the greatest # of bananas
# if it's one more, then it can equal the second most
# something I observed from the first example, we can get 4 by splitting the biggest term until terms = h
# 3,6,7,11(4)-3,6,7,4,7(5)-3,6,3,4,3,4,4(7)-3,3,3,3,4,3,4,4(8), last largest element is 4
# we split the largest element at each point into the second largest and remainder
# how do we implement this, and is this even efficient
# if we just inserted the split term, it would be O(p) h times, but p would also grow with h,
# so it's more like h^2. that's pretty bad.

# what's the brute force
# just check all k's from 1 to max in piles
# that's O(p * max(pile)), which is already better than my original thought
# the question is binary search, how can we use that
# we can just split the search space of k at each point, if k works then
# the new search space is everything below it including it, else everything above
# find the max possible k, then bin search until we get the last valid one
# O(log(max(pile)) * p)

# time to solve: 45 min
# time complexity: O(log(max pile) * n)
# space complexity: O(1)
def solution(piles: list[int], h: int) -> int:

    l = 1
    r = max(piles)

    while l < r:
        mid = (l + r) // 2
        total_hours = 0
        for p in piles:
            total_hours += (p + mid - 1) // mid
        if total_hours <= h:
            r = mid
        else:
            l = mid + 1
    return l


def main():

    piles = [3,6,7,11]
    h = 8 #4
    print(solution(piles, h))

    piles = [30,11,23,4,20]
    h = 5 #30
    print(solution(piles,h))

    piles = [30,11,23,4,20]
    h = 6 #23
    print(solution(piles,h))

if __name__ == "__main__":
    main()
