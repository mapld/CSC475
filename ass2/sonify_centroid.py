import matplotlib, numpy
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import wave
import struct
from scipy.io.wavfile import read as wavread
fig=plt.figure(figsize=(6,3))
fs = 44100 # sample rate
def readWavSamples(filename):
    [samplerate, vals] = wavread(filename)

    if isinstance(vals[0], numpy.ndarray):
      print "reading stereo file"
      samples = (vals[:,0]/2 + vals[:,1]/2 ) / 31
    else:
      print "reading mono file"
      samples = vals / 31
    return samples
def getCentroid(freqs):
  fsum = 0
  asum = 0
  for freq in range(0,len(freqs)): 
    amp = freqs[freq]
    fsum += freq * amp * amp 
    asum += amp * amp 
  return fsum / asum
def getCentroidOverTime(filename):
    samples = readWavSamples(filename)
    frameNum = 2048
    
    centroids = numpy.zeros(len(samples)/frameNum + 1)
    cur = 0
    i = 0
    
    while cur < len(samples):
       workingFrames = samples[cur:cur+2048]
       fft = numpy.fft.fft(workingFrames, frameNum)
       fft = fft / len(fft)
       rCount = len(fft) / 2
       realFft = numpy.abs(fft[:rCount])*2
       centroids[i] = getCentroid(realFft)
       cur += frameNum
       i += 1
    return centroids * 44100 / frameNum
    
import matplotlib, numpy
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import wave
import struct
from scipy.io.wavfile import read as wavread
fig=plt.figure(figsize=(6,3))
fs = 44100 # sample rate
fs = 44100 # sample rate

def sinWave(frequency, amplitude, phase=0, duration = 1.0):
    print phase
    sNum = fs * duration
    x = numpy.arange(sNum)
    return amplitude * numpy.sin(2*numpy.pi*frequency*x/fs + phase)
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

def getSonifiedCentroid(centroids, outfile):
  frameNum = len(centroids)
  frameLen = 2048
  samples = numpy.zeros(frameNum * frameLen)
  phase = 0 
  for i in range (0,frameNum):
    dur = float(frameLen) / 44100
    s = sinWave(centroids[i], 1.0, phase, dur) 
    samples[i*frameLen:(i+1)*frameLen] = s
    sampleLength = (44100/centroids[i])
    phase += ((2048 % sampleLength) / sampleLength) * (2*numpy.pi)
    phase = phase % (2*numpy.pi)

  saveWav(samples, outfile)
