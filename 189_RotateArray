class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k1 = k % len(nums)
        nums = nums[-k1:] + nums[0:len(nums) - k1 - 1]
        return nums

p = Solution()
print(p.rotate([1, 2, 3, 4, 5, 6, 7, 8], 3))

# 反方向切片时也是从左到右【-3：-1】为-3，-2,。不包括-1
