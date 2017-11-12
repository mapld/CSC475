import sklearn.datasets as skld 

def load_libsvm(path):
    data = skld.load_svmlight_file(path)
    return data[0], data[1]

X, y = load_libsvm("genres/genres3.libsvm")
import matplotlib
import numpy as np
from sklearn.model_selection import KFold

def kFold(classifier, X, y, k):
    kf = KFold(n_splits=k)
    Y = np.zeros(X.shape[0])
    for train_index, test_index in kf.split(X):
        X_test = X[test_index]
        X_train = X[train_index]
        y_train = y[train_index]
        classifier.fit(X_train,y_train)
        y_pred = classifier.predict(X_test)
        Y[test_index] = y_pred
    return Y
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def printStats(y_true,y_pred):
  print("Accuracy: " + str(100*accuracy_score(y_true, y_pred)) + "%")
  print confusion_matrix(y_true, y_pred)

np.random.seed(0)
indices = np.random.permutation(X.shape[0])
X = X[indices]
y = y[indices]


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()

Y=kFold(knn,X,y,10)
printStats(y,Y)
