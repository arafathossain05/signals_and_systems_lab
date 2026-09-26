import numpy as np
import matplotlib.pyplot as plt

# --------------------------------
# User Defined Functions
# --------------------------------

# 1. Addition
def addition(x1, x2):
    return x1 + x2


# 2. Folding
def folding(x):
    return x[::-1]


# 3. Shifting
def shifting(x, k):
    return np.roll(x, k)


# --------------------------------
# Input Signals
# --------------------------------

n = np.arange(-2, 3)

x1 = np.array([1, 2, 3, 2, 1])
x2 = np.array([2, 1, 2, 1, 2])


# --------------------------------
# Signal Operations
# --------------------------------

# Addition of two signals
y_add = addition(x1, x2)

# Folding of two signals
y_fold1 = folding(x1)
y_fold2 = folding(x2)

# Shifting of two signals
k = 2
y_shift1 = shifting(x1, k)
y_shift2 = shifting(x2, k)

# Shifted time index
n_shift = n + k


# --------------------------------
# Plotting
# --------------------------------

plt.figure(figsize=(10, 10))

# x1[n]
plt.subplot(5, 2, 1)
plt.stem(n, x1)
plt.title("Input Signal x1[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# x2[n]
plt.subplot(5, 2, 2)
plt.stem(n, x2)
plt.title("Input Signal x2[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# Addition
plt.subplot(5, 1, 3)
plt.stem(n, y_add)
plt.title("Addition: x1[n] + x2[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# Folding
plt.subplot(5, 1, 4)
plt.stem(-n, y_fold1, label="Folded x1[n]")
plt.stem(-n, y_fold2, label="Folded x2[n]")
plt.title("Folding: x[-n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Shifting
plt.subplot(5, 1, 5)
plt.stem(n_shift, y_shift1, label="Shifted x1[n]")
plt.stem(n_shift, y_shift2, label="Shifted x2[n]")
plt.title("Right Shifting: x[n-2]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()