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

def getBinFreq(filename):
  samples = readWavSamples(filename)

  frameNum = 2048 
  peaks = numpy.zeros(len(samples)/frameNum + 1)
  i = 0
  cur = 0 

  while cur < len(samples): 
      workingFrames = samples[cur:cur+2048]
      fft = numpy.fft.fft(workingFrames, frameNum)
      fft = fft / len(fft)
      rCount = len(fft) / 2
      realFft = numpy.abs(fft[:rCount])*2
      maxAmp = 0
      for idx in range(0, len(realFft)): 
        val = realFft[idx]
        if val > maxAmp:
          peaks[i] = idx
          maxAmp = val
      i += 1
      cur += 2048

  return peaks * 44100 / 2048
