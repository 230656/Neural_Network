# The dot product is a mathematical operation denoted by the symbol "⋅" (dot) or by using the 
# multiplication operator "*". It takes two vectors or arrays as input and returns a scalar value.
#
# For 1D arrays (vectors):
# - If A = [a1, a2, ..., an] and B = [b1, b2, ..., bn] are two 1D arrays, the dot product 
#   is calculated as:
#
#                n
#               ___
#               \ 
#     A ⋅ B  =  /   ai * bi
#               ---
#               i=1
#
#              n
#            = ___
#              \ 
#               |  ai * bi
#              / 
#             ---
#            i=1
#
#            = a1*b1 + a2*b2 + ... + an*bn
#
# For 2D arrays (matrices):
# - If A and B are two matrices with dimensions m × n and n × p respectively, the dot product 
#   results in a new matrix C with dimensions m × p:
#
#             _
#            |         n
#            |       ___
#            |       \ 
#     C  =    |  A ⋅ B =  /   A[i][j] * B[j][k]
#            |       --- 
#            |       j=1
#            |
#            - 
#
#            m   p
#            ___ ___
#            \   \   \
#     C[i][k] =  \   \   A[i][j] * B[j][k]
#            /   /   /
#            --- ---
#            j=1 j=1
#
#            = A[0][0]*B[0][0] + A[0][1]*B[1][0] + ... + A[0][n]*B[n][0],  ... , A[m][0]*B[0][p] + A[m][1]*B[1][p] + ... + A[m][n]*B[n][p]
#
# For 3D arrays:
# - The dot product of two 3D arrays results in a 2D array. It's calculated by performing 
#   the dot product operation along the last dimension of the first array and the second-to-last 
#   dimension of the second array.
#
# Overall, the dot product is a fundamental operation used in linear algebra for various 
# mathematical computations, including matrix multiplication and calculating similarities 
# between vectors or arrays.

import sys 
import numpy as np
import matplotlib

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5] # Bias = offset value

output = np.dot(weights, inputs) + biases
print(output)