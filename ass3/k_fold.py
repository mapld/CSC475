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
