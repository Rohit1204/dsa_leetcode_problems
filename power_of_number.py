n=int(input())
x=int(input())

# first and fastest way to find power
def power(n,x):
    if x==0:
        return 1
    elif(x%2==0):
        return power(n,x//2) * power(n,x//2)
    else:
        return n * power(n,x//2) * power(n,x//2)
        
a=power(n,x)
print(a)
