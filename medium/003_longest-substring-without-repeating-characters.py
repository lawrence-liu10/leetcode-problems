# 003. Longest Substring Without Repeating Characters
# Difficulty: Medium

# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# I almost got taken out by a stomach virus, couldn't do anything for a couple days
# anyways, we can initialize a left and right pointer, and keep moving the right pointer until a character repeats
# if it repeats, then we move the left pointer one
# we're done when the right reaches the end, as that will be the longest it can get
# we can probably improve time complexity by keeping track of seen letters rather than slicing each time, for future me to complete
# time to solve: 15 min
# time complexity: O(n^2)
# space complexity: O(1)
def solution(s: str) -> int:

    max = 0
    l = 0
    r = 0
    while r < len(s):
        if s[r] not in s[l:r]:
            r += 1
            if r - l > max:
                max = r - l
        else:
            l += 1
    return max

def main():
    s = "abcabcbb"#3
    print(solution(s))

    s = "bbbbb"#1

if __name__ == "__main__":
    main()
