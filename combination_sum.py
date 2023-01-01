# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # If n is less than k or n is greater than 24, terminate
        # If thum i found to be greater than 10 then terminate
        self.result =[]
        self.helper([],1,k,n)
        return self.result
    
    def helper(self,path,start,k,target):
        
        if k ==0 and target==0:
            self.result.append(path)
            return 
        
        if k == 0 or target <= 0:
            return
        
        for i in range(start,10):
            self.helper(path+[i],i+1,k-1,target-i)
        