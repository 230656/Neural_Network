# We compute the output of each neuron in a neural network layer by performing a weighted sum of the inputs, 
# adding the bias, and applying an activation function (not included in this code).
#
# For each neuron:
# - We multiply each input by its corresponding weight.
# - We sum the products of inputs and weights.
# - We add the bias to the sum.
# - We obtain the output of the neuron.
#
# Finally, we store the outputs of all neurons in a list and print the result.
#

import sys 
import numpy as np
import matplotlib

inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

# Compute the output of each neuron
output = [
    inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
    inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
    inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3
]

# Output the results
print(output)