import matplotlib, numpy
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(6,3))
fs = 44100 # sample rate
x = numpy.arange(fs)

def sinWave(frequency, amplitude, phase=0, duration = 1.0):
    sNum = fs * duration
    return amplitude * numpy.sin(2*numpy.pi*frequency*x/sNum + phase)

def createHarmonicMix(baseFreq, a1, a2, a3, p1=0, p2=0, p3=0):
    f1 = sinWave(baseFreq, a1, p1)
    f2 = sinWave(baseFreq*2, a2, p2)
    f3 = sinWave(baseFreq*3, a3, p3)
    return [f1+f2+f3, f1, f2, f3]
freq = 440
mixResult = createHarmonicMix(freq, 1.0, 0.5, 0.33, 0, 0, 0)
mix = mixResult[0]

plt.plot(x[0:1000], mix[0:1000])

plt.savefig('images/q2p1.png')
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

saveWav(mix, "sound/q3p1.wav")
return "sound/q3p1.wav"
