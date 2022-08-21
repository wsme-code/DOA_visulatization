# Visualization pyaudio code from Mark Jay
## https://www.youtube.com/watch?v=AShHJdSIxkY

import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import time

CHUNK = 4000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
fs = RATE^-1

p = pyaudio.PyAudio()

chosen_device_index = -1
for x in range(0,p.get_device_count()):
    info = p.get_device_info_by_index(x)
    print(p.get_device_info_by_index(x))

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input_device_index=1,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# make stream for condensor mic
stream2 = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input_device_index=2, # index of my second mic
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)
 
plt.ion()
fig, (ax, ax2) = plt.subplots(2)
fig2, (ax3, ax4) = plt.subplots(2)

# plots width of single frame 
x = np.arange(0, CHUNK)
x_fft = np.linspace(0, RATE, CHUNK)

line, = ax.plot(x, np.random.rand(CHUNK))
line_fft, = ax2.semilogx(x_fft, np.random.rand(CHUNK))

ax.set_title("Webcam Mic")
ax.set_ylim([-1.1,1.1])
ax2.set_title("Condensor mic")
ax2.set_ylim([0, 10000000])
ax2.set_xlim([20, RATE / 2])

while True:
    data = struct.unpack(str(CHUNK) + 'h', stream.read(CHUNK))
    data2 = struct.unpack(str(CHUNK) + 'h', stream2.read(CHUNK))
    # normalize data output
    data_array = np.asarray(data)
    data_norm = data_array/2**15
    # fft of input
    y_fft = fft(data)
    line_fft.set_ydata(np.abs(y_fft[0:CHUNK])/(2*CHUNK))

    line.set_ydata(data_norm)
    line_fft.set_ydata(y_fft)
    fig.canvas.draw()
    fig.canvas.flush_events()
