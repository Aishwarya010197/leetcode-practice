def twoSum(l, t):
    cmp = {}
    for i in range(len(l)): 
        if (l[i]) in cmp:
            return (cmp[l[i]], i) 
        else: 
            cmp[t-l[i]] = i

print(twoSum([3,4,5,6,7], 7))