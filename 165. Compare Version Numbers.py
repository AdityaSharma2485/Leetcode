class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def get_next_revision(version: str, idx: int) -> (int, int):
            if idx >= len(version):
                return 0, idx
            num = 0
            while idx < len(version) and version[idx] != '.':
                num = num * 10 + int(version[idx])
                idx += 1
            return num, idx + 1 if idx < len(version) else idx

        idx1, idx2 = 0, 0
        while idx1 < len(version1) or idx2 < len(version2):
            num1, idx1 = get_next_revision(version1, idx1)
            num2, idx2 = get_next_revision(version2, idx2)
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        return 0
        
