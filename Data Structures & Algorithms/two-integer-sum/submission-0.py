class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict: dict = {}
        counter = 0
        for num in nums:
            difference = target - num
            if num in diff_dict:
                return [diff_dict[num], counter]
            diff_dict[difference] = counter
            counter += 1