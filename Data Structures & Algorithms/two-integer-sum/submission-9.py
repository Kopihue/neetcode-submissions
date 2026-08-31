class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for idx, num in enumerate(nums):
            numbers[num] = idx

        for idx, num in enumerate(nums):
            search_for = target - num
            if search_for in numbers:
                diff = numbers.get(search_for)
                if idx != diff: 
                    return [idx, diff]

        return [0, 0]

