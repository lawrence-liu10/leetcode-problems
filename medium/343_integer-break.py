# 343. Integer Break
# Difficulty: Medium

# Link: https://leetcode.com/problems/integer-break/description/

# intuitively, the best way would be to split a number to its sqrt many times, giving us 
#   the same number (+1) times itself multiple times.
#       it's similar to the logic that 10 * 1 is less than 5 * 5. we want multiple medium numbers vs some big/small
#   actually, instead of sqrt, we just always break numbers into as many 3s as possible
#       if there's 1 remainder, we make a 3-1 into 2-2. otherwise it's as expected
#       the pattern is recognizable after trying on some numbers
#   i'll just do dp for now for practice

# dp
# for the dp, dp[i] == max product at i
#   base cases of 1 and 2 are done manually, each being 1, 1 respectively (can't split 1 but for greater i's)
# otherwise, we loop from each number, and set dp[i] as the max of either
#   what it is currently,
#   both pieces broken again,
#   or one piece broken again (either left/right piece)
# 
def solution(self, n: int) -> int:

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1

    for total in range(3, n + 1):
        max_product = 0
        for part in range(1, total):
            current = part * (total - part)
            re_break = dp[part] * dp[total - part]
            left_break = dp[part] * (total - part)
            right_break = part * dp[total - part]

            cur_max = max(current, re_break, left_break, right_break)
            max_product = max(cur_max, max_product)
        dp[total] = max_product
    return dp[-1]




            
    



def main():
    pass

if __name__ == "__main__":
    main()
