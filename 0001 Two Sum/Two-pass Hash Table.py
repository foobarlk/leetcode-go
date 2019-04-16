class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            mapping[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapping and mapping[complement] != i:
                return [i, mapping[complement]]
        
        return []