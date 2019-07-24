import numpy as np
import matplotlib.pyplot as plt

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

plt.plot(t1, wave)
plt.plot(t2, np.abs(fft_result))
plt.show()
