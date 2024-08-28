from matplotlib import pyplot as plt
import numpy as np

a = np.array([20, 87, 4, 40, 53, 74, 56, 51, 11, 20, 40, 15, 79, 25, 27])
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title("histogram")
plt.show()

plt.hist(a, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.title("histogram")
plt.show()
