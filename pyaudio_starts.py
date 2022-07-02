from tkinter import Tk
import matplotlib
import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib Tk

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
)

data = stream.read(CHUNK)
print(struct.unpack(str(CHUNK) + 'I', data))
data_int = np.array(struct.unpack(str(CHUNK) + 'I', data), dtype='b') + 127
print(data_int)

fig, ax = plt.subplots()
ax.plot(data_int, '-')
ax.set_ylim(-255, 255)
plt.show()