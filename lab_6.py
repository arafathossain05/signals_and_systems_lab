import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
fs = 1000

# Time duration
t = np.linspace(0, 1, fs)

# Different frequencies
f1 = 2
f2 = 5
f3 = 10

# Generate sinusoidal signals
x1 = np.sin(2 * np.pi * f1 * t)
x2 = np.sin(2 * np.pi * f2 * t)
x3 = np.sin(2 * np.pi * f3 * t)

# Plot 2 Hz signal
plt.figure(figsize=(10, 7))

plt.subplot(3, 1, 1)
plt.plot(t, x1)
plt.title("Sinusoidal Wave - 2 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Plot 5 Hz signal
plt.subplot(3, 1, 2)
plt.plot(t, x2)
plt.title("Sinusoidal Wave - 5 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Plot 10 Hz signal
plt.subplot(3, 1, 3)
plt.plot(t, x3)
plt.title("Sinusoidal Wave - 10 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
