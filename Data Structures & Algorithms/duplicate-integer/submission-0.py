class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict: dict = {}
        for i in range (0, len(nums)):
            if not nums[i] in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                return True

        return False
