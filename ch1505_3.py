import numpy as np
import matplotlib.pyplot as plt

# Unique identifiers for each figure
FIGURE1 = 1
FIGURE2 = 2

# Wave parameters
FREQUENCY = 3
SAMPLING_RATE = 100
TIME_STEP = 1.0 / SAMPLING_RATE

# Like range() for floating point
t1 = np.arange(0.0, 5.0, TIME_STEP)

# Compute a sine wave
wave = np.sin(FREQUENCY*2*np.pi*t1)

# Compute Fast Fourier Transform (FFT)
fft_result = np.fft.fft(wave)

# Compute x-axis values for frequency domain
t2 = np.fft.fftfreq(len(t1), TIME_STEP)

plt.subplot(3, 3, 1)  # 3 rows, 1 column. Use loc 1
plt.plot(t1, wave)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.axis([-1, 6, -1.2, 1.2])  # Empty space buffer

plt.subplot(3, 3, 6)  # 2 rows, 1 column. Use loc 2
plt.plot(t2, np.abs(fft_result))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

# Set plot axis ranges [min_x, max_x, min_y, max_y]
plt.axis([-5, 5, 0, 260])

plt.show()
