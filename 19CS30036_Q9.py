# 19CS30036

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import classification_report,confusion_matrix
np.random.seed(69)

def generateData():  

  y = [0]*500
  x = np.random.normal(0, 5, size=(500,2))

  # storing the classified values in y
  for i in range(x.shape[0]):

    if np.prod(x[i]) > -1:
      y[i] = 1

    else:
      y[i] = -1

  y=np.array(y)

  # storing dataframe
  Z = pd.DataFrame(x)
  Z['y']=y
 
  # plot
  sns.scatterplot(data = Z, x = 0, y = 1, hue= "y", cmap = 'virdis')

  return x, y

# function call to generate function 
X, Y = generateData()

def LeastSquare(x, y):
 
  # intialising A with appropriate dimensions (500*6)
  # 500 data samples and 6 no. of constants/variables needed to form the polynomial by matrix multiplication
  A = np.zeros((500, 6))
  
  # theta vector initialised as 6*1 vector 
  T = np.zeros((6,1))

  for i in range(500):
    # storing the polynomial terms that are variables in matrix A 
    A[i][0] = 1
    A[i][1] = x[i][0]
    A[i][2] = x[i][1]
    A[i][3] = x[i][0]*x[i][1]
    A[i][4] = x[i][0]**2
    A[i][5] = x[i][1]**2

  #least square minimization
  # A.T = y being the equation being minimized
  T, throwaway1, throwaway2, throwaway3 = np.linalg.lstsq(A, y, rcond=-1)

  print("Matrix Theta:")
  print(T)
  print("")
  
  fSOL = np.sign( A@T )

  print("Classification report \n")
  print(classification_report(fSOL, y))
  
  print("Confusion Matrix :\n")

  CMatrix = confusion_matrix(fSOL, y)
  print(CMatrix)

  # storing dataframe of Confusion Matrix
  Z = pd.DataFrame(CMatrix, range(2), range(2))
  
  # printing heatmap 
  sns.heatmap(Z, annot=True, annot_kws={"size": 14}) 

  return T

T = LeastSquare(X, Y)

print("Theta : ")
print(T)
print("")

def PlotVectors(T):
  # initialising vectors X and Y for plotting graph 
  xG = np.linspace(-10, 10, 1000)
  yG = np.linspace(-10, 10, 1000)
  

  # storing 1, x1, x2, (x1)^2, (x2)^2, x1*x2 inside zG for all x1, x2
  zG = np.array([np.sign(np.array([1, i, j, i*j, i*i, j*j])@T) for j in yG for i in xG])

  # mapping the plot axes with appropriate values
  zG = zG.reshape(1000, 1000)
  figure, axis = plt.subplots()
  CountourG = axis.contourf(xG, yG, zG)
  throwaway = figure.colorbar(CountourG)
  
  # printing the desired plot
  print("Plot \n")
  plt.show()

PlotVectors(T)
