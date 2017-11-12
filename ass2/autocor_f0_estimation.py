def getAutoCorellation(samples, size=2048):
  fft = numpy.fft.rfft(samples, size)
  # reverse fft of fft * its complex conjugate 
  p1 = fft * numpy.conj(fft)
  p2 = p1 * numpy.conj(p1)
  return numpy.fft.irfft(p2 , size) 
def getMaxPeak(samples):
  maxVal = 0
  maxI = 0 
  start = False 
  for i in range(1,len(samples)/2):
    if samples[i] < 0:
      start = True
    if not start:
      continue
    if samples[i] > samples[i-1] and samples[i] > samples[i+1]:
       if(samples[i] > maxVal):
         maxVal = samples[i]
         maxI = i
  return maxI
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
def autoCorFreqEstimateOverTime(filename):
    samples = readWavSamples(filename) 
    frameNum = 2048 
    
    peaks = numpy.zeros(len(samples)/frameNum + 1)
    i = 0
    cur = 0 

    while cur < len(samples):
      workingFrames = samples[cur:cur+2048]
      acor = getAutoCorellation(workingFrames)
      #return acor
      peaks[i] = getMaxPeak(acor)
      cur += frameNum
      i += 1 
    return 44100 / peaks
