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

def likelihood(test_song, word_probs_for_genre): 
    probability_product = 1.0 
    for (i,w) in enumerate(test_song): 
        if (w==1): 
            probability = word_probs_for_genre[i]
        else: 
            probability = 1.0 - word_probs_for_genre[i]
        probability_product *= probability 
    return probability_product
def predict(test_song, probs): 
    probs = [likelihood(test_song, probs[0]), 
             likelihood(test_song, probs[1]),
             likelihood(test_song, probs[2])]
    return np.argmax(probs)
def classify(X, y, probs):
    matrix = np.zeros((3,3)) 
    accCount = 0
    for (i,song) in enumerate(X):
        prediction = predict(song,probs)
        matrix[y[i]][prediction] += 1
        if(y[i] == prediction):
            accCount += 1

    accuracy = float(accCount) / float(len(y))
    return matrix, accuracy
rapY = np.full(1000,0,dtype=np.int) 
rockY = np.full(1000,1,dtype=np.int)
countryY = np.full(1000,2,dtype=np.int) 
y = np.concatenate((rapY, rockY, countryY))
probs = (word_probs_rap,word_probs_rock,word_probs_country)
matrix, acc = classify(a[0:3000,:],y,probs)
print acc
print matrix
