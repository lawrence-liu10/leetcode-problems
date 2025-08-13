# 763. Partition Labels
# Difficulty: Medium

# Link: https://leetcode.com/problems/partition-labels/description/

# we need the first letter to only appear in its own section,
#   we'll take a right pointer and set it to the last appearance of the left letter
#   as well, we'll find which char from left to right pointer appears the latest in the string,
#       using that as the point to partition from
# we'll continue with that process until the end
def solution(self, s: str) -> list[int]:
    sol = []
    left = 0
    while left < len(s):
        right = s.rindex(s[left])

        cur = left + 1
        while cur < right:
            rightC = s.rindex(s[cur])
            if rightC > right:
                right = rightC
            cur += 1

        sol.append(right - left + 1)
        left = right + 1
    return sol




def main():
    pass

if __name__ == "__main__":
    main()
