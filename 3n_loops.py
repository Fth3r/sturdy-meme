#! /usr/bin/python3

# Hand-coding three neurons using loops

inputs = [1, 2, 3, 2.5]

weights = [[0.2,0.8,-0.5,1.0],
            [0.5,-0.91,0.26,-0.5],
            [-0.26,-0.27,0.17,0.87]]

biases = [2, 3, 0.5]

# Output of the current layer
layer_outputs = []

# Looping each neuron
for n_weights, n_bias in zip(weights, biases):
    # zeroed neuron output
    n_output = 0
    # for each input and weight to the neuron
    for n_input, weight in zip(inputs, n_weights):
        # multiply the input by the associated weight
        # and add to the neuron's output variable
        n_output += n_input * weight
    # add bias
    n_output += n_bias
    # append result to the layer outputs list
    layer_outputs.append(n_output)

print(layer_outputs)