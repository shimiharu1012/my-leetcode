#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n=min([len(_str) for _str in strs])
        strs_len=len(strs)
        i=0
        while i<n:
            for j in range(strs_len-1):
                if strs[j][i]!=strs[j+1][i]:
                    return strs[0][:i]

            i+=1


        return strs[0][:i]
                

        
# @lc code=end

