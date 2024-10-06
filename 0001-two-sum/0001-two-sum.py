class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Check = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in Check:
                return [Check[diff], i]
            Check[n] = i
        return