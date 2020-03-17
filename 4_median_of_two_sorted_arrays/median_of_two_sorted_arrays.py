import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Combine and Sort
        collective = sorted(nums1 + nums2)
                    
        # Get the mid point
        midpoint = (len(collective)-1)/ 2
        
        # Indexify ;) Generic for both even and odd lengthed sequence
        x = int(math.floor(midpoint))
        y = int(math.ceil(midpoint))
        return (collective[x] + collective[y]) / 2