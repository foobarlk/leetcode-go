class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        if nums[0] > 0:
            return []

        res = set()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                
                if sum == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                if sum < 0:
                    j += 1
                else:
                    k -= 1

        return list(res)
