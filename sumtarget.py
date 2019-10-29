'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

'''


class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        i = 0
        j = 0
        x = True
        # print len(self.nums)
        while i < len(self.nums) and x:
            j = i + 1
            # print j
            while j < len(self.nums) and x:
                if self.nums[i] + self.nums[j] == self.target:
                    x = False
                j = j + 1
            i = i + 1
        return [i, j]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
t = 14
n = Solution(a, t)
print n.twoSum()