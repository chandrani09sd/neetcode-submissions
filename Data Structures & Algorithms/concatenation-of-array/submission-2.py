class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)
        ans[:n] = nums
        ans[n:] = nums
        return ans