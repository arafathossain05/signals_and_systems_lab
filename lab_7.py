import numpy as np
import matplotlib.pyplot as plt

# Input sequence
x = np.array([1, 2, 3, 4])

N = len(x)

# ---------------- DFT ----------------
X = np.zeros(N, dtype=complex)

for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

# ---------------- IDFT ----------------
x_idft = np.zeros(N, dtype=complex)

for n in range(N):
    for k in range(N):
        x_idft[n] += X[k] * np.exp(1j * 2 * np.pi * k * n / N)

x_idft = x_idft / N

# Display results
print("Original sequence x[n]:")
print(x)

print("\nDFT X[k]:")
print(np.round(X, 2))

print("\nIDFT reconstructed sequence:")
print(np.round(x_idft.real, 2))

# ---------------- Plot ----------------

plt.figure(figsize=(10, 7))

plt.subplot(3, 1, 1)
plt.stem(x)
plt.title("Original Signal x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(np.abs(X))
plt.title("Magnitude Spectrum |X[k]|")
plt.xlabel("Frequency Index k")
plt.ylabel("Magnitude")
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(x_idft.real)
plt.title("Reconstructed Signal using IDFT")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
