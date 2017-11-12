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
