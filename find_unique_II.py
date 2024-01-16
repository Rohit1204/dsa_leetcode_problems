""" 
this code will find unique item from a list
where each other item contains thrice
"""
def singleNumber(nums: list) -> int:
    res1=res2=0
    for i in nums:
        res1 = (res1^i) & ~res2
        res2 = (res2^i) & ~res1
    return res1