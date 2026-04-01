class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict: dict = {}
        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)

        freq_arr = [[] for i in range(len(nums)+1)]
        for num, freq in freq_dict.items():
            freq_arr[freq].append(num)

        ret_arr = []
        for i in range(len(freq_arr)-1, 0, -1):
            for j in freq_arr[i]:
                ret_arr.append(j)
                if len(ret_arr) == k:
                    return ret_arr
        
        return ret_arr