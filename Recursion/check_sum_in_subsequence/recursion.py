from typing import *

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    # Write your code here.
    def f(i,summ):
        if i>=n:
            if summ == k:
                return True
            return False
        l = f(i+1,summ+a[i])
        r = f(i+1,summ)
        return l or r
    
    return f(0,0)