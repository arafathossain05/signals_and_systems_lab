import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
fs = 4000

# Time vector
t = np.arange(0, 0.05, 1/fs)

# Multi-frequency signal
x = (np.cos(2 * np.pi * 100 * t) + np.cos(2 * np.pi * 500 * t) + np.cos(2 * np.pi * 700 * t))

# Frequency range
f = np.arange(0, 900, 1)

# Numerical Fourier Transform
Xf = np.array([np.sum(x * np.exp(-1j * 2 * np.pi * fi * t)) * (1/fs)  for fi in f ])

# Create figure
plt.figure(figsize=(11, 3.5))

# 1. Time-domain signal
plt.subplot(1, 2, 1)
plt.plot(t * 1000, x)
plt.title("Multi-frequency Signal x(t)")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.grid(True)

# 2. Amplitude spectrum
plt.subplot(1, 2, 2)
plt.plot(f, np.abs(Xf))
plt.title("Amplitude Spectrum |X(f)|")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.tight_layout()

# Save
plt.savefig("exp13.png")

# Display
plt.show()