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
