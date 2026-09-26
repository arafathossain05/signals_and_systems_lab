import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
Fs = 1000

# Time
t = np.arange(0, 1, 1/Fs)

# Given signal
x = (0.25
     + 2*np.sin(2*np.pi*5*t)
     + np.sin(2*np.pi*12.5*t)
     + 1.5*np.sin(2*np.pi*20*t)
     + 0.5*np.sin(2*np.pi*35*t))

# Number of samples
N = len(x)

# DFT using FFT
X = np.fft.fft(x)

# Frequency axis
f = np.fft.fftfreq(N, 1/Fs)

# Shift zero frequency to center
X_shift = np.fft.fftshift(X)
f_shift = np.fft.fftshift(f)

# Magnitude spectrum
magnitude = np.abs(X_shift) / N

# Plot
plt.figure(figsize=(10, 5))
plt.plot(f_shift, magnitude)

plt.title("Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("|X(f)|")
plt.xlim(-50, 50)
plt.grid()

plt.show()
