class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty_map = {}

        for i, current in enumerate(nums):
            difference = target - current
            if difference in empty_map:
                return [empty_map[difference], i]
            empty_map[current] = i
            