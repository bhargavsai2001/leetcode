class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        count = 0
        res, l = 0, len(nums)
        for i in range(0, l):
            if nums[i]==0:
                res = max(res, left+count)
                left = count
                count = 0
            else:
                count+=1
        return count-1 if count==l else max(res, left+count) 