# -*- coding: utf-8 -*-
import numpy as np
#%%
a = input()
b = a.split()
b = b[0]+b[1]
a = int(b)
#%%
rta = np.sqrt(a)
sa = rta - int(rta)
if sa > 0:
    print('no')
else:
    print('sq')
