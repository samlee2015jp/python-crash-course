v = [1, 2, 3]
r = v * 2
print(v)
print(r)

import numpy as np
v = np.array([1, 2, 3])
v * 2        # array([2, 4, 6])
v + v        # array([2, 4, 6])
np.dot(v, v)  # 14
print(v)
import torch
v = torch.tensor([1.0, 2.0, 3.0])
