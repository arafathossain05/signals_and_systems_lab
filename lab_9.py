import numpy as np
import matplotlib.pyplot as plt

# a. Generate a pure sine wave of 440 Hz

fs = 4000                 # Sampling frequency
duration = 1              # Signal duration in seconds
f = 440                   # Sine wave frequency

t = np.arange(0, duration, 1/fs)

# Pure 440 Hz sine wave
clean_signal = np.sin(2 * np.pi * f * t)
# b. Add random noise

np.random.seed(10)

noise = 0.5 * np.random.randn(len(t))

noisy_signal = clean_signal + noise
# c. Apply DFT

N = len(noisy_signal)

# DFT
X = np.fft.fft(noisy_signal)

# Frequency axis
freq = np.fft.fftfreq(N, 1/fs)
# d. Remove noise by filtering high frequencies

cutoff = 600     # Cutoff frequency = 600 Hz

# Create frequency-domain filter
X_filtered = X.copy()

# Remove frequencies above cutoff
X_filtered[np.abs(freq) > cutoff] = 0
# e. Apply Inverse DFT

cleaned_signal = np.fft.ifft(X_filtered)

# Take real part
cleaned_signal = np.real(cleaned_signal)
# Plot results

plt.figure(figsize=(12, 10))

# Original clean signal
plt.subplot(4, 1, 1)
plt.plot(t[:500], clean_signal[:500])
plt.title("Original 440 Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Noisy signal
plt.subplot(4, 1, 2)
plt.plot(t[:500], noisy_signal[:500])
plt.title("Noisy Audio Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Frequency spectrum
plt.subplot(4, 1, 3)

positive_freq = freq[:N//2]
magnitude = np.abs(X[:N//2])

plt.plot(positive_freq, magnitude)
plt.xlim(0, 2000)
plt.title("DFT Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()

# Cleaned signal
plt.subplot(4, 1, 4)
plt.plot(t[:500], cleaned_signal[:500])
plt.title("Cleaned Signal after IDFT")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
