import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt, find_peaks

# 1. Generate a sample PPG signal
fs = 1000  # Sampling frequency (Hz)
duration = 10  # Signal duration (seconds)

t = np.arange(0, duration, 1 / fs)

# Basic PPG-like signal
heart_rate = 72  # BPM
f_hr = heart_rate / 60  # Hz

ppg = (
    1.0 * np.sin(2 * np.pi * f_hr * t)
    + 0.25 * np.sin(4 * np.pi * f_hr * t)
    + 0.05 * np.random.randn(len(t))
)

# 2. Bandpass filtering
lowcut = 0.5
highcut = 5.0
order = 3

b, a = butter(order, [lowcut, highcut], btype="bandpass", fs=fs)

filtered_ppg = filtfilt(b, a, ppg)

# 3. Detect systolic peaks
peaks, peak_properties = find_peaks(
    filtered_ppg, distance=int(0.5 * fs), prominence=0.2
)

# 4. Detect diastolic points (Find minima by applying find_peaks to inverted signal)
diastolic_points, _ = find_peaks(
    -filtered_ppg, distance=int(0.5 * fs), prominence=0.1
)

# 5. Calculate Heart Rate
peak_times = t[peaks]

if len(peak_times) > 1:
    RR_intervals = np.diff(peak_times)
    average_RR = np.mean(RR_intervals)
    heart_rate_calculated = 60 / average_RR
else:
    heart_rate_calculated = 0

# 6. Display results
print("Number of Systolic Peaks:", len(peaks))
print("Number of Diastolic Points:", len(diastolic_points))
print("Estimated Heart Rate:", round(heart_rate_calculated, 2), "BPM")

# 7. Plot PPG signal and extracted features
plt.figure(figsize=(12, 5))

plt.plot(t, filtered_ppg, label="Filtered PPG")
plt.plot(t[peaks], filtered_ppg[peaks], "ro", label="Systolic Peaks")
plt.plot(
    t[diastolic_points],
    filtered_ppg[diastolic_points],
    "go",
    label="Diastolic Points",
)

plt.xlabel("Time (seconds)")
plt.ylabel("PPG Amplitude")
plt.title("PPG Feature Extraction")

plt.legend()
plt.grid()
plt.show()