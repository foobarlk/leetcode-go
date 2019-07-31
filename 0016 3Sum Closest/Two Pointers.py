class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort()

        import sys
        dist = sys.maxsize
        res = 0
    
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == target:
                    return sum
                
                if abs(target - sum) < dist:
                    dist = abs(target - sum)
                    res = sum
                
                if sum < target:
                    j += 1
                else:
                    k -= 1
            
        return res
