import matplotlib, numpy
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(6,3))
fs = 44100 # sample rate
x = numpy.arange(fs)

def sinWave(frequency, amplitude, phase=0, duration = 1.0):
    sNum = fs * duration
    return amplitude * numpy.sin(2*numpy.pi*frequency*x/sNum + phase)

import wave
import struct

def saveWav(samples, filename):
    wavFile = wave.open(filename, "w")
    nchannels = 1
    sampwidth = 2
    nframes = len(samples)
    comptype = "NONE"
    compname = "not compressed"
    wavFile.setparams((nchannels, sampwidth, fs, nframes, comptype, compname))

    for sample in samples:
        clampedSample = numpy.median([sample, -1.0, 1.0])
        #clampedSample = sample
        wavFile.writeframes(struct.pack('h', int(16384.0*clampedSample)))

    wavFile.close()


c = sinWave(261.6, 1.0, phase=0, duration = 1.0)
e = sinWave(311.1, 1.0, phase=0, duration = 1.0)
g = sinWave(392, 1.0, phase=0, duration = 1.0)

melody = numpy.concatenate((c, e, g, e, g, c))

saveWav(melody, "CSC475/melody.wav")
return "CSC475/melody.wav"
