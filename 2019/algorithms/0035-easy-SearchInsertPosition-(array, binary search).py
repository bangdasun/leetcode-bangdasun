class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 1:
            return 0
        
        left, right = 0, n - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] > target:
                right = m - 1
            elif nums[m] < target:
                left = m + 1
            else:
                return m
            
        return left
