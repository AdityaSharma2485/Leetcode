class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        return sorted(nums, key = lambda x : (hashmap[x],-x))
