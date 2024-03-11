# Neuron Code Introduction:
#
# The Neuron class represents a single neuron in a neural network. In the context of this code, 
# the neural network architecture consists of multiple layers: Input Layer, Hidden Layer 1, 
# Hidden Layer 2, and Output Layer. Each neuron in the network is responsible for processing 
# incoming signals, applying weights, biases, and activation functions to produce an output. 
#
# The purpose of this neural network is to predict whether a failure will occur or not based on 
# input data. The prediction is made by comparing the output values of the output layer neurons, 
# where the prediction with the higher value is considered the supposed prediction.
#
# The training process of the neural network involves tuning the weights and biases associated 
# with each neuron. These tunable parameters are adjusted iteratively during the training process 
# to minimize the error between the predicted and actual outputs. 
#
# Each neuron is connected to subsequent layers of neurons, forming a network structure. The 
# connections between neurons are represented by unique weights, and each neuron has a unique 
# bias associated with it. The combination of weights and biases determines how input signals 
# are processed and propagated through the network. 
#
# Throughout the training process, the values of weights and biases are adjusted to optimize the 
# performance of the neural network in making accurate predictions.
#
# This code serves as a foundational implementation of a single neuron, which can be further 
# integrated into a larger neural network architecture for various applications, including 
# classification, regression, and pattern recognition tasks.

# Explanation:
#
# We have a list of inputs: [1.2, 5.1, 2.1] and a list of weights: [3.1, 2.1, 8.7].
# Each input is multiplied by its corresponding weight, and the results are added together.
# Additionally, we have a bias of 3, which is added to the sum of the weighted inputs.
# This calculation represents how much importance each input has, weighted by its corresponding weight.
# The bias acts as an offset, affecting the final result.
# The computed sum represents the output of a simple neuron without an activation function applied.
# Finally, we print the resulting output.

import sys 
import numpy as np
import matplotlib

inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3

#output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
#print(output)

output = sum([inputs[i]* weights[i] for i in range(len(inputs))]) + bias
print(output)