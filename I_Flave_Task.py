import math

def josephus (n,k):
    arr = []
    res = []
    for i in range(1,n+1):
        arr.append(i)

    while(len(arr)>0):
        i = 0
        m = (n+1) // k
        for j in range(1,m):
            res.append (arr[(j-1)*k])

        for j in res:
            arr.remove(j)
        
    return res

res = josephus(6,2)

print(res)
