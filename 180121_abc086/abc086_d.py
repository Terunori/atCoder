# -*- coding: utf-8 -*-
#%%
def wOrB(strinp,a,b,k):
    [x,y,c] = strinp.split()
    x,y = int(x),int(y)
    x -= a
    y -= b
    if x%(2*k) <= k:
        if y%(2*k) <= k:
            col = 'W'
        else:
            col = 'B'
    else:
        if y%(2*k) <= k:
            col = 'B'
        else:
            col = 'W'
    if col == c:
        ans = 1
    else:
        ans = 0
    return ans

#%%
lst,lstinp = [],[]
n,k = map(int, input().split())
for i in range(n):
    lstinp.append(input())
for a in range(k):
    for b in range(k):
        count = 0
        for i in range(n):
            inp = lstinp[i]
            count += wOrB(inp,a,b,k)
        lst.append(count)
print(max(lst))
