# 005. Longest Palindromic Substring
# Difficulty: Medium

# Link: https://leetcode.com/problems/longest-palindromic-substring/description/

# for this question, we'll check starting from each character what the longest palindrome is
# to check, we'll treat s[i] as the string's middle and work our way outwards
#   if a char on the left == the char on the right, we'll update our current palindrome
# we actually also need to consider even and odd length strings
#   we'll run our function on both and take the longer string
# this is a greedy solution though, not dp
def solution(self, s: str) -> str:
    def expand(s, left, right) -> int:
        while (left >= 0 and right < len(s) and
            s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1

    start = 0
    end = 0
    for i in range(len(s)):
        len_odd = expand(s, i, i)
        len_even = expand(s, i, i + 1)
        max_len = max(len_odd, len_even)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def main():
    pass

if __name__ == "__main__":
    main()
