"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    triplets = set()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate values of the first number
        firstNum = nums[i]
        j, k = i + 1, len(nums) - 1
        while j < k:
            secondNum, thirdNum = nums[j], nums[k]
            potentialSum = firstNum + secondNum + thirdNum 
            if potentialSum > 0:
                k -= 1
            elif potentialSum < 0:
                j += 1
            else:
                triplets.add((firstNum, secondNum, thirdNum))
                j, k = j + 1, k - 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1  # Skip duplicate values of the second number
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1  # Skip duplicate values of the third number
    return triplets