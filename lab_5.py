import numpy as np
import matplotlib.pyplot as plt

# Input sequence
x = np.array([1, 2, 3,4])

# Impulse response
h = np.array([1, 2])

# Convolution
y = np.convolve(x, h)
n = np.arange(len(x))
print("x(n) =", x)
print("h(n) =", h)
print("y(n) =", y)

# Plot x(n)
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(n,x)
plt.title("Input Sequence x(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# Plot h(n)
plt.subplot(3, 1, 2)
plt.stem(n,h)
plt.title("Impulse Response h(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# Plot y(n)
plt.subplot(3, 1, 3)
plt.stem(n,y)
plt.title("Convolution Output y(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
