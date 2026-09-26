import numpy as np
import matplotlib.pyplot as plt

# Discrete-time index
n = np.arange(-7, 8)

# Unit impulse function
delta_n_plus_2 = (n + 2 == 0).astype(int)
delta_n_minus_4 = (n - 4 == 0).astype(int)

# x(n) = 2δ(n+2) - δ(n-4)
x = 2 * delta_n_plus_2 - delta_n_minus_4

# Plot
plt.stem(n, x)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title(r'$x(n) = 2\delta(n+2) - \delta(n-4)$')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)

plt.show()
