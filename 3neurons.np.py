# dot product of 3 neurons with 4 inputs each

import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [[0.2,0.8,-0.5,1.0],
            [0.5,-0.91,0.26,-0.5],
            [-0.26,-0.27,0.17,0.87]]
biases = [2, 3, 0.5]

# np.dot() does the heavy lifting of multiplying the matrix (weights)
# by the array (inputs) and adding each bias in its array (vector addition).
# Whichever vector is arg'd first determines the final shape
# which in this case is a list of dot products (neuron outputs)
layer_output = np.dot(weights, inputs) + biases

print(layer_output)