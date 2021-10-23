#19CS30036

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.datasets import mnist
import seaborn as sns
from sklearn.metrics import classification_report,confusion_matrix

np.random.seed(69)

# function to generate image dataset
def GenerateDataset():

  # loading MNIST data set (training and testing)
  (trainX, trainY), (testX, testY) = mnist.load_data()

  trainX = trainX.reshape(trainX.shape[0], -1)/255.0 
  testX = testX.reshape(testX.shape[0], -1)/255.0

  # temporary variables
  t = []
  target = []
  tTest=[]
  targetTest=[]

  for i in range(10):

    t.extend( trainX[np.where(trainY == i)[0][np.random.permutation(1000)]])
    target.extend([i]*1000)

    tTest.extend(testX[np.where(testY == i)[0][np.random.permutation(100)]])
    targetTest.extend([i]*100)
      
  trainData, testData  = np.hstack((np.vstack(t), np.vstack(target))), np.hstack((np.vstack(tTest), np.vstack(targetTest)))

  print(f"Training Dataset: {trainData.shape}") 
  print("")
  print(f"Testing Dataset: {testData.shape}")

  return trainData, testData

def ModelFit(train):
  
  A = train[:, :-1]
  b = train[:, -1]
  
  T = []
  
  for i in range(10):
    
    b_fit = np.zeros_like(b)
    b_fit[np.where( b == i )] = 1

    Tfit, throwaway1, throwaway2, throwaway3 = np.linalg.lstsq(A, b_fit, rcond=-1)
    T.append(Tfit)

  T = np.array(T)
  P = np.array([np.argmax([x@r  for r in T ]) for x in A])

  print(f"Classification score for the training Datset = {classification_report(b, P)}") 

  # generating confusion matrix using predictions
  CMatrix=confusion_matrix(b, P)

  print("")
  print("Confusion Matrix:")
  print(CMatrix)

  return T

def CMatrixPrediction(test, fit):

  print("")
  print("**CLASSIFICATION REPORT FOR TEST**")
  print("")

  X = test[:, :-1]
  y = test[:, -1]

  P = np.array([np.argmax([x@r for r in fit ]) for x in X])

  print(classification_report(y, P))

  CMatrix = confusion_matrix(y, P)
  print(f"Confusion Matrix : \n {CMatrix} \n")


TrainingDataset,TestDataset = GenerateDataset()
fit=ModelFit(TrainingDataset)
CMatrixPrediction(TestDataset, fit)
