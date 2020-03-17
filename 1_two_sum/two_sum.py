class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, x in enumerate(nums):

            # The complement that is needed to meet the target
            dx = target - x
            
            # Does the complement already exists in our sequence (so far)
            if dx in num_dict:
                return sorted([idx, num_dict[dx]])
            
            # Add this to observed occurrences
            num_dict[x] = idx