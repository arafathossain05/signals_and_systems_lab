import matplotlib.pyplot as plt
import numpy as np

# Time
t = np.linspace(0, 2, 1000)

# Fundamental angular frequency
omega_0 = 2 * np.pi


# Fourier Series function
def fourier_square_wave(t, N):
    x = np.zeros_like(t)

    for n in range(1, N + 1, 2):
        x += (1 / n) * np.sin(n * omega_0 * t)

    return (4 / np.pi) * x


# Create figure
plt.figure(figsize=(12, 8))


# N = 1
plt.subplot(2, 2, 1)
plt.plot(t, fourier_square_wave(t, 1))
plt.title("N = 1")
plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.grid(True)


# N = 3
plt.subplot(2, 2, 2)
plt.plot(t, fourier_square_wave(t, 3))
plt.title("N = 3")
plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.grid(True)


# N = 5
plt.subplot(2, 2, 3)
plt.plot(t, fourier_square_wave(t, 5))
plt.title("N = 5")
plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.grid(True)


# N = 7
plt.subplot(2, 2, 4)
plt.plot(t, fourier_square_wave(t, 7))
plt.title("N = 7")
plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.grid(True)


# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig("fourier_square_wave.png", dpi=300)

# Show plot
plt.show()