# 049. Group Anagrams
# Difficulty: Medium

# Link: https://leetcode.com/problems/group-anagrams/

# time to solve: 15 min

# make a hashmap, the key will be the hashmap of each word, the value will be a list
# turn each word into a hashmap and check it against each key
# if equal, append to the list

# after a little research, hashmaps cannot be used as keys
# we'll use tuples instead (different than hsm, order matters- 
#   if we just tuple a string, the order will be different
#   we first sort so the order will always be the same)

# time complexity: O(n * m log(m)) b/c of sort, m being longest string len
# space complexity: O(n * m) b/c each tuple can correspond to its own string
def solution(strs: list[str]) -> list[list[str]]:
    
    anagrams = {}

    for str in strs:
        key = tuple(sorted(str))

        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(str)
    

    # return anagrams.values() <- returns the object, we just want the listed lists
    return list(anagrams.values())


# We shouldn't have to sort each time, that's nlog(n)
# We can simply add each letter to a list and compare lists instead
# works because there's only 26 letters, each insertion is O(1) so each word is O(m) instead
# time complexity would be O(n * m) instead
def solution(strs: list[str]) -> list[list[str]]:
    # TODO
    pass



def main():

    strs1 = ["eat","tea","tan","ate","nat","bat"]
    strs2 = [""]
    strs3 = ["a"]

    print(solution(strs1))

if __name__ == "__main__":
    main()
