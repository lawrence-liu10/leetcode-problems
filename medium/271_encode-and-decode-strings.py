# 271. Encode And Decode Strings
# Difficulty: Medium

# Link: https://leetcode.com/problems/encode-and-decode-strings/description/

# time to solve: 30 min
# I lowkey saw a reel about this a week or two ago, have to see if I can remember
# turn each string into num of letters + a delimiter symbol + the string
# and concatenate all of them, then reverse that
# works because long word lengths, symbols, etc. don't matter
# time complexity: O(l), l being total length of all strings
# space complexity: O(l)
def encode(strs: list[str]) -> str:

    code = ""
    for str in strs:
        length = len(str)
        encoded_word = f"{length}#{str}"
        code += encoded_word
    
    return code

# time complexity: O(l)
# space complexity: O(l)
def decode(s: str) -> list[str]:
    
    words = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        word = s[i:j]
        words.append(word)
        i = j
    return words



def main():
    
    input1 = ["neet","code","love","you"]
    input2 = ["😊", "こんにちは", "🚀🌕"]

    en1 = encode(input1)
    de1 = decode(en1)
    print(de1)

    en2 = encode(input2)
    de2 = decode(en2)
    print(de2)


if __name__ == "__main__":
    main()
