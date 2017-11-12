import matplotlib, numpy
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(6,3))
fs = 44100 # sample rate
x = numpy.arange(fs)

def sinWave(frequency, amplitude, phase=0, duration = 1.0):
    sNum = fs * duration
    return amplitude * numpy.sin(2*numpy.pi*frequency*x/sNum + phase)


frequencies = []
frequencies.append(200)
frequencies.append(440)
frequencies.append(500)
amplitudes = []
amplitudes.append(0.5)
amplitudes.append(1.0)
amplitudes.append(2.0)
amplitudes.append(3.0)
sinWaves = []
for f in frequencies:
    for a in amplitudes:
        sinWaves.append({'frequency' : f, 'amplitude' : a, 'samples' : sinWave(f,a)})

  
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
data = [] 
for s in sinWaves:
    d = {}
    d['frequency'] = s['frequency']
    d['amplitude'] = s['amplitude']
    d['peak'] = peakAmplitude(s['samples'])
    d['RMS'] = peakRMS(s['samples'])
    d['expectedRMS'] = d['amplitude']/numpy.sqrt(2)
    data.append(d)
print "{:<10} {:<10} {:<20} {:<20} {:<10}".format('Frequency','Amplitude','peakAmp', 'peakRMS', 'expectedRMS')
for d in data:
  print "{:<10} {:<10} {:<20} {:<20} {:<10}".format(d['frequency'], d['amplitude'], d['peak'], d['RMS'], d['expectedRMS'] )
