import matplotlib, numpy
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(6,3))
fs = 44100 # sample rate
x = numpy.arange(fs)

def sinWave(frequency, amplitude, phase=0, duration = 1.0):
    sNum = fs * duration
    return amplitude * numpy.sin(2*numpy.pi*frequency*x/sNum + phase)

def innerProdAmp(freq, signal, duration=1.0, phase=0):
    unitSin = sinWave(freq, 1.0, phase, duration)
    return numpy.dot(signal,unitSin) * 2 / len(unitSin)
