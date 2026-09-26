import matplotlib.pyplot as plt
import numpy as np

# Discrete-time index
n = np.arange(-10, 11)

# 1. Unit Sample Sequence
delta = np.where(n == 0, 1, 0)

# 2. Unit Step Signal
u = np.where(n >= 0, 1, 0)

# 3. Unit Ramp Signal
r = np.where(n >= 0, n, 0)

# Create one figure
plt.figure(figsize=(8, 10))

# 1. Unit Sample Sequence
plt.subplot(3, 1, 1)
plt.stem(n, delta)
plt.xlabel('n')
plt.ylabel('δ[n]')
plt.title('Unit Sample Sequence')
plt.grid(True)

# 2. Unit Step Signal
plt.subplot(3, 1, 2)
plt.stem(n, u)
plt.xlabel('n')
plt.ylabel('u[n]')
plt.title('Unit Step Signal')
plt.grid(True)

# 3. Unit Ramp Signal (যদি নিচে অসম্পূর্ণ থেকে থাকে)
plt.subplot(3, 1, 3)
plt.stem(n, r)
plt.xlabel('n')
plt.ylabel('r[n]')
plt.title('Unit Ramp Signal')
plt.grid(True)

plt.tight_layout()
plt.show()