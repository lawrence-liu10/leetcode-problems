# 011. Container With Most Water
# Difficulty: Medium

# Link: https://leetcode.com/problems/container-with-most-water/
# missed a day to move out

# idea: we have three variables. a left height, right height, and base length (index r - l)
# the height is limited by the shorter height, so we just multiply the shorter
# height by the base each time
# what if we always move the shorter height pointer inwards
# greedy solution, assuming it always provides the best answer

# time to solve: 15 minutes
# time complexity: O(n)
# space complexity: O(1)
def solution(height = list[int]) -> int:
    
    left = 0
    right = len(height) - 1
    max_area = 0
    b = len(height) - 1

    while left < right:
        lefth = height[left]
        righth = height[right]
        cur_height = lefth if lefth < righth else righth

        if cur_height * b > max_area:
            max_area = cur_height * b
        
        b -= 1
        if lefth < righth:
            left += 1
        else:
            right -= 1

    return max_area
        



def main():
    height = [1,8,6,2,5,4,8,3,7]# 49
    print(solution(height))

    height = [1,1]# 1
    print(solution(height))


if __name__ == "__main__":
    main()
