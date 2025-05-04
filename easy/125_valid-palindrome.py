# 125. Valid Palindrome
# Difficulty: Easy

# Link: https://leetcode.com/problems/valid-palindrome/description/

# 2 pointer, move in until left and right are alphanumeric,
# then check equality
# messed up bounds, need l < r always
# time complexity: O(n)
# space complexity: O(1)
def solution(s: str) -> bool:
    
    left = 0
    right = len(s) - 1
    s = s.lower()

    while (left < right):
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True



def main():
    pass

if __name__ == "__main__":
    main()
