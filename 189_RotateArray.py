class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k1 = k % len(nums)
        nums = nums[-k1:] + nums[:-k1]
        return nums

p = Solution()
print(p.rotate([1], 3))
