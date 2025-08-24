# 338. Counting Bits
# Difficulty: Easy

# Link: https://leetcode.com/problems/counting-bits/
import math

# let's try the dp approach
# [0, 1, 1, 2, 1, 2, 2, 3, 1]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
#   has to do with powers of two
#       it resets at each power of two
#   if it's 2^n - 1, we add one to the one before it before resetting after
#       we can simplify this. basically it's equal to n // 2 (+ 1 IF the last digit is 1, or when it's 2^n - 1)
#       we'll bit shift for less overhead
def solution(self, n: int) -> list[int]:
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)

    return dp

def main():
    pass

if __name__ == "__main__":
    main()
