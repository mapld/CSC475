import matplotlib
import numpy as np
import pickle

data = np.load('data/data.npz')
a = data['arr_0']
# reduce the problem to whether or not the word occurs instead of how many
a[a > 0] = 1

a = a[0:3000,:] 
rap_rows = a[0:1000,:]
rock_rows = a[1000:2000,:]
country_rows = a[2000:3000,:] 

labels = np.load('data/labels.npz')
labels = labels['arr_0'] 

dictionary = pickle.load(open('data/dictionary.pck','rb'))
word_indices = np.load('data/words.npz')['arr_0']
words = [dictionary[r] for r in word_indices]

tracks = pickle.load(open('data/tracks.pck','rb'))

def get_word_probs(occur):
  return (occur.sum(axis=0).astype(float) + 1.0) / (len(occur)+1.0)

word_probs_rap = get_word_probs(rap_rows)
word_probs_rock = get_word_probs(rock_rows)
word_probs_country = get_word_probs(country_rows)

def generateRandomLyrics(word_probs, words):
  # words in random order
  indices = np.random.permutation(len(words))
  r_probs = word_probs[indices]
  r_words = np.array(words)[indices]

  # pick words
  s = ""
  r = np.random.rand(30)
  for (i,word) in enumerate(r_words):
    if r[i] < r_probs[i]:
      s += word + " " 
  return s
for i in range(0,5):
  print "rap sample: " + generateRandomLyrics(word_probs_rap, words) 
  print "rock sample: " + generateRandomLyrics(word_probs_rock, words) 
  print "country sample: " + generateRandomLyrics(word_probs_country, words)
