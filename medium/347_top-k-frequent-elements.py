# 347. Top K Frequent Elements
# Difficulty: Medium

# Link: https://leetcode.com/problems/top-k-frequent-elements/description/

# first thought was to bucket sort the input array
# not very efficient, range of values similar to the input size
# also inputs might not be evenly distributed

# hashmap to count each unique element
# make list of lists, add the unique elements to their corresponding count
# backwards iterate the final list and keep popping until we reach k elements
# bucket sort but flipping the numbers and counts
# time to solve- 45 min
# time complexity: O(n)
# space complexity: O(n)
def solution(nums: list[int], k :int) -> list[int]:
    
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    frequencies = [[] for _ in range(len(nums) + 1)]
    for key, val in counts.items():
        frequencies[val].append(key)
    
    k_freq = []
    for i in range (len(nums), -1, -1):
        while frequencies[i] and k != 0:
            k_freq.append(frequencies[i].pop())
            k -= 1
            if k == 0:
                return k_freq




def main():

    nums1 = [1,1,1,2,2,3] #[1,2]
    k1 = 2

    nums2 = [1]
    k2 = 1

    print(solution(nums1, k1))
    print(solution(nums2, k2))



if __name__ == "__main__":
    main()
