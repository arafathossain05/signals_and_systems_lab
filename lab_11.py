import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt

# Sampling frequency
fs = 1000

# Time vector
t = np.arange(0, 1, 1/fs)

# Fundamental frequency
f0 = 10

# Generate square wave
x = sig.square(2 * np.pi * f0 * t)

# Calculate Power Spectral Density
f, Pxx = sig.periodogram(x, fs)

# -----------------------------
# Square Wave
# -----------------------------
plt.figure(figsize=(6, 3.5))

plt.plot(t, x)

plt.title("Square Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.savefig("square_wave.png", dpi=300)
plt.show()


# -----------------------------
# Power Spectral Density
# -----------------------------
plt.figure(figsize=(6, 3.5))

plt.plot(f, Pxx)

plt.title("Power Spectral Density")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power/Hz")
plt.xlim(0, 200)
plt.grid()

plt.tight_layout()
plt.savefig("psd.png", dpi=300)
plt.show()