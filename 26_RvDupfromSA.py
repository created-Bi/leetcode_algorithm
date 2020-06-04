class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[prev]:
                prev += 1
                nums[prev] = nums[i]
        return prev + 1