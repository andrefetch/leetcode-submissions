# Q217: contains duplicate
# Approach: use set since they discard duplicated values for O(1) time
# Time: O(1) | Worst: O(n)

class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False
        