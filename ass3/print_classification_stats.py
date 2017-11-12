from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def printStats(y_true,y_pred):
  print("Accuracy: " + str(100*accuracy_score(y_true, y_pred)) + "%")
  print confusion_matrix(y_true, y_pred)
