def findUnique(arr, n) :
    #Your code goes here
    res = arr[0]
    for i in range(1, n):
        res = res ^ arr[i]
        print(res)
    return res
