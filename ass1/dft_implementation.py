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
mix = createHarmonicMix(220, 1.0, 0.5, 0.2)[0]

def fft(realInput):
  n = len(realInput)
  realOutput = numpy.zeros(n) 
  imaginaryOutput = numpy.zeros(n) 

  n = len(realInput)
  #for each phasor
  for k in range(0, 700):
    # in time
    for t in range(0, n):
      angle = 2 * numpy.pi * k * t / n
      realOutput[k] += realInput[t] * numpy.cos(angle)
      imaginaryOutput[k] -= realInput[t] * numpy.sin(angle)
  return realOutput/fs, imaginaryOutput/fs

real, imag = fft(mix)
#abs value
spect = numpy.sqrt(real*real+imag*imag)

realSpecNum = len(spect) / 2
plt.plot(spect[:realSpecNum]*2)
plt.savefig('images/s2q3.png')

return 'images/s2q3.png'
