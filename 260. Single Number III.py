class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lis = []
        hm= {}

        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        for key, value in hm.items():
            if value == 1:
                lis.append(key)
        return lis
