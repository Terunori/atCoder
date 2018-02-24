# -*- coding: utf-8 -*-
#%%
def canDeerGo(strinp):
    t, n1, n2 = map(int, strinp.split())
    var1 = t + n1 + n2
    var2 = n1 + n2
    ans = True
    if var1 % 2 != 0 or var2 > t:
        ans = False
    return ans
#%%
def diffData(s,ss):
    t, n1, n2 = map(int, s.split())
    t2,n12,n22 = map(int, ss.split())
    l = [t2-t,n12-n1,n22-n2]
    canDeerGo(' '.join((list(map(str,l)))))
#%%
num = int(input())
ss =''
for i in range(num):
    s = input()
    if ss != '':
        diffData(s,ss)
    ans = canDeerGo(s)
    if ans == False:
        ans = 'No'
        break
    elif i == num-1:
        ans = 'Yes'
    ss = s
print(ans)