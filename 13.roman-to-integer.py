#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        romans_dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        n=len(s)
        i=0
        sum=0
        while i<n:
            if i==n-1:
                sum+=romans_dict[s[i]]
                i+=1
                continue
            
            if s[i]=="I":
                if s[i+1]=="V":
                    sum+=4
                    i+=2
                elif s[i+1]=="X":
                    sum+=9
                    i+=2
                else:
                    sum+=romans_dict[s[i]]
                    i+=1
            elif s[i]=="X":
                if s[i+1]=="L":
                    sum+=40
                    i+=2
                elif s[i+1]=="C":
                    sum+=90
                    i+=2
                else:
                    sum+=romans_dict[s[i]]
                    i+=1
            elif s[i]=="C":
                if s[i+1]=="D":
                    sum+=400
                    i+=2
                elif s[i+1]=="M":
                    sum+=900
                    i+=2
                else:
                    sum+=romans_dict[s[i]]
                    i+=1
            else:
                sum+=romans_dict[s[i]]
                i+=1

            
        return sum

            
# @lc code=end

