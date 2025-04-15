import math

def josephus (n,k):
    arr = []
    res = []
    for i in range(1,n+1):
        arr.append(i)

    index = 0

    while(len(arr)>0):

        

        if k > len(arr):
            arr_copy = arr.copy()
            while (k//(len(arr)+1)) > 0:
                arr.extend(arr_copy)
            

        m = (len(arr)) // k
        
        for j in range(0, m):
            index = (j+1) * k -1

            if arr[index] not in res:
                    res.append(arr[index])


        new_arr = []
        for l in range(arr.index(res[-1]) + 1, len(arr)):
            if arr[l] not in new_arr and arr[l] not in res:
                new_arr.append(arr[l])

        for j in res:
            if j in arr:
                arr.remove(j)
        
        for g in arr:
            if g not in new_arr and g not in res:
                new_arr.append(g)

        arr = new_arr
        
    return res

result = josephus(4,3)

print(result)
