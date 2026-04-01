class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count: int = 0
        array_product = 1
        for num in nums:
            if num == 0:
                zero_count = zero_count + 1
                if zero_count == 2:
                    return [0 for i in range(0, len(nums))]
                continue
            array_product = array_product * num

        return_array = []
        for num in nums:
            if zero_count == 1:
                return_array.append(array_product) if num == 0 else return_array.append(0)
                continue
            return_array.append(int(array_product / num))
        return return_array
