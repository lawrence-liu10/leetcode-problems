# 134. Gas Station
# Difficulty: Medium

# Link: https://leetcode.com/problems/gas-station/description/


# the brute force is simple, just loop through the array from each index
#   what's a more efficient approach

# first the cost must be less than or equal to the total gas, otherwise it's impossible
#   similar to the max subarray question, if a portion of the array causes
#   the tank to become negative, then it can't be the starting value, and the start must come after
#   keep going until we don't need to reset

def solution(self, gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    cur = 0
    start_ind = 0
    for i in range(len(gas)):
        cur += gas[i] - cost[i]

        if cur < 0:
            cur = 0
            start_ind = i + 1

    return start_ind



def main():
    pass

if __name__ == "__main__":
    main()
