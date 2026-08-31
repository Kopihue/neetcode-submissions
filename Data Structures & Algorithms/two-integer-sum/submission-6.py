class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for fi, fn in enumerate(nums):
            for si, sn in enumerate(nums):
                if fn + sn == target and fi != si:
                    print(fn, sn)
                    return [fi, si]

        return [0, 0]