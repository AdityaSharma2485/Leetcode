class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        occurrence_set = set()
        for value in hashmap.values():
            if value in occurrence_set:
                return False
            occurrence_set.add(value)
        return True
