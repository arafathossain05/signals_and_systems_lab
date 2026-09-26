import numpy as np
import matplotlib.pyplot as plt

# Discrete-time sequence
x = np.array([1, 2, 3, 4, 5])

# 501 equispaced frequency points from 0 to pi
w = np.linspace(0, np.pi, 501)

# DTFT calculation
n = np.arange(len(x))
X = np.array([
    np.sum(x * np.exp(-1j * wi * n))
    for wi in w
])

# Magnitude
magnitude = np.abs(X)

# Angle / Phase
angle = np.angle(X)

# Real part
real_part = np.real(X)

# Imaginary part
imag_part = np.imag(X)

# Create plots
plt.figure(figsize=(10, 8))

# 1. Magnitude
plt.subplot(2, 2, 1)
plt.plot(w, magnitude)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('|X(e^jω)|')
plt.grid()

# 2. Angle
plt.subplot(2, 2, 2)
plt.plot(w, angle)
plt.title('Angle Spectrum')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('∠X(e^jω)')
plt.grid()

# 3. Real part
plt.subplot(2, 2, 3)
plt.plot(w, real_part)
plt.title('Real Part')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Re{X(e^jω)}')
plt.grid()

# 4. Imaginary part
plt.subplot(2, 2, 4)
plt.plot(w, imag_part)
plt.title('Imaginary Part')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Im{X(e^jω)}')
plt.grid()

plt.tight_layout()
plt.savefig("exp14.png")
plt.show()

