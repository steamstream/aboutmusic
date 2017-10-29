
import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(11)]
y = [i / 10 for i in range(11)]

x, y = np.meshgrid(x, y)

t = np.random.rand(100)
t = np.sort(t)
t = t.reshape(10, 10)
intensity = np.random.rand(10, 10)
#intensity = t

plt.pcolormesh(x, y, intensity, cmap="Blues")
plt.colorbar()
plt.tight_layout()
plt.show()