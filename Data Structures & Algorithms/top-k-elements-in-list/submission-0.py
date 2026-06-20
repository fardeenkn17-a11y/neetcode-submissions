from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Build frequency dictionary
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Sort by frequency (descending)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: Take top k elements
        result = [item[0] for item in sorted_items[:k]]
        
        return result

        