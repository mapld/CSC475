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
import matplotlib, numpy
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(6,3))
fs = 44100 # sample rate
x = numpy.arange(fs)

def sinWave(frequency, amplitude, phase=0, duration = 1.0):
    sNum = fs * duration
    return amplitude * numpy.sin(2*numpy.pi*frequency*x/sNum + phase)

import matplotlib, numpy
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(6,3))
def peakAmplitude(samples):
    highest = 0;
    for s in samples:
        n = numpy.absolute(s)
        if n > highest:
            highest = n
    return highest

def peakRMS(samples):
    return numpy.sqrt(numpy.mean(numpy.square(samples)))
def createNoise(db, signalAmplitude, duration):
    ampRatio = numpy.power(10., db/20)
    noiseAmplitude = signalAmplitude / ampRatio;
    r = numpy.random.uniform(-1.0,1.0,duration*fs)
    # rms amplitude to peak amplitude ratio for uniform distribution 
    return r * noiseAmplitude * numpy.sqrt(3)

def createNoisySinWave(freq, amp, db, duration = 1.0):
    s = sinWave(freq, amp)  
    y = createNoise(db, peakRMS(s), duration)
    return s + y

noisySinWave = createNoisySinWave(440, 1.0, -20)


noisySinWave = createNoisySinWave(440, 1.0, 100)

saveWav(noisySinWave , "sound/q4p1.wav")
return "sound/q4p1.wav"
