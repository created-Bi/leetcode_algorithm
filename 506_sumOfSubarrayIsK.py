class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = 0
        hashmap = {0:1}
        summ = 0
        for x in nums:
            summ += x
            if summ - k in hashmap:
                res += hashmap[summ - k]
            if summ in hashmap:
                hashmap[summ] += 1
            else:
                hashmap[summ] = 1
        return res