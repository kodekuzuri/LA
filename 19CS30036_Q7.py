 #19CS30036

import numpy as np

def IterativeLeastSquare(N):

  print("\n")
  print("**START**")
  print("\n")

  # generating random matrix A, dimensions: 30*10
  A = np.random.rand(30, 10)

  # generating random vector b, dimensions: 30*1
  b = np.random.rand(30, 1)

  # least square minimization for Ax = b with the solution as LSx
  LSx, throwaway, rankA, throwaway1 = np.linalg.lstsq(A ,b, rcond = -1)

  # if rank of A is not 10 it is not a full rank matrix 
  if rankA != 10:
    print(f"Rank(A) = {rankA}, A is not a full rank matrix")

  # if rank(A) = 10 , it is a full rank matrix 
  else:
    print(f"Rank(A) = {rankA}, A is a full rank matrix")

  print("")

  # initialising x(1) as a 10*1 vector with all zeroes (given in the question) 
  x = np.zeros((10, 1))

  # calculating x(r) iteratively by using value of x(r-1)
  for i in range(N):

    # using the formula given in the question to calculate x(r) using x(r-1)
    xr = x - A.T@(A@x-b) / np.square( np.linalg.norm( A, 2 ) )

    # x(r-1) for the next iteration is the x(r) calculated in this iterations
    x = xr

  print(f"x calculated after {N} iterations is {x.T}")
  print("")

  print(f"x calculated using the least squares minimization is {LSx.T}")
  print("")
  
  print(f"||xLS - xLSiteration|| = { np.linalg.norm(LSx - x, 2) }")
# end of function

print("2-norm calculated for numerical convergence proof \n")
# running the iterative function for 100 iterations
IterativeLeastSquare( N = 100 )

print("Proof of convergence: The calculated gets more closer to the Least square solution for increasing number of iterations (the 2-norm difeerence decreases)\n")
# running the iterative function for 500 iterations
IterativeLeastSquare( N = 500 )

# running the iterative function for 1000 iterations
IterativeLeastSquare( N = 1000 ) 
