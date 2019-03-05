import numpy as np
import matplotlib.pyplot as plt

ts_length = 100
values    = []

for i in range(ts_length):
    e = np.random.randn()
    values.append(e)

plt.plot(values)
plt.show()
