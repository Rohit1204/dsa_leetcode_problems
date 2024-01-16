""" 
this code will find unique item from a list
where each other item contains twice
"""
def findUnique(arr, n) :
    #Your code goes here
    res=0
    for i in arr:
        res ^= i
    return res