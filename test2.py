import numpy as np
from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Read the file (rate and data):
rate, data = wavfile.read('tone2.wav') # See source

# Compute PSD:
f, P = signal.periodogram(data, rate) # Frequencies and PSD

# Display PSD:
fig, (axe, ax) = plt.subplots(2)
axe.semilogy(f, P)
axe.set_xlim([0,500])
axe.set_ylim([1e-8, 1e10])
axe.set_xlabel(r'Frequency, $\nu$ $[\mathrm{Hz}]$')
axe.set_ylabel(r'PSD, $P$ $[\mathrm{AU^2Hz}^{-1}]$')
axe.set_title('Periodogram')
axe.grid(which='both')

# Display FFT
xf = np.linspace(0, rate, len(data))
ax.loglog(xf, np.abs(fft(data)/len(data)))
ax.grid()
plt.show()

