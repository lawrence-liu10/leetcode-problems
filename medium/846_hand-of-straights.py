# 846. Hand Of Straights
# Difficulty: Medium

# Link: https://leetcode.com/problems/hand-of-straights/description/

# for this question, firstly the group size should evenly divide into the array length
# my idea is to make a map of the list and keep trying to make a list starting from the minimum
#   eventually we'll run out or the list won't be empty
def solution(self, hand: list[int], groupSize: int) -> bool:

    if len(hand) % groupSize != 0:
        return False

    map = {}
    for num in hand:
        map[num] = map.get(num, 0) + 1

    while map:
        start = min(map.keys())

        for i in range(groupSize):
            cur_num = start + i
            if cur_num not in map:
                return False

            map[cur_num] -= 1
            if map[cur_num] == 0:
                del map[cur_num]
    return True





def main():
    pass

if __name__ == "__main__":
    main()
