import numpy as np
import math

class BackPropagation:
    def __init__(self):
        pass

    def MainAlgorithm(self, features, eta, epochs, bias, threshold,
                      stopping_criteria, activation_function,
                      num_hidden_layer, num_neurons_layer):
        """This function will run the back propagation algorithm"""

        # Initializing weight vector with random values
        weights = {}
        weights_inputs = []
        ind = 1
        for i in range(num_hidden_layer + 1):
            if i == 0:
                for j in range(num_neurons_layer):
                    weights["w" + str(ind)] = [np.random.rand(1)[0]
                                                     for k
                                                     in range
                                                     (5)]
                    weights_inputs.append(0)
                    ind += 1
            elif i == num_hidden_layer :
                for j in range(int(3)):
                    weights["w" + str(ind)] = [np.random.rand(1)[0]
                                                     for k
                                                     in range
                                                     (num_neurons_layer +1)]
                    weights_inputs.append(0)
                    ind += 1
            else:
                for j in range(int(num_neurons_layer)):
                    weights["w" + str(ind)] = [np.random.rand(1)[0]
                                                     for k
                                                     in range
                                                     (num_neurons_layer + 1)]
                    weights_inputs.append(0)
                    ind += 1


        if stopping_criteria == 1:  # Number of epochs
            # loop through number of epochs
            for i in range(epochs):
                # loop through number of samples
                for j in range(len(features["X1"])):
                    # getting input vector
                    X = [features["X1"][j], features["X2"][j],
                         features["X3"][j], features["X4"][j]]
                    YOut = features["Y"][j]
                    weights_inputs = self.NetInput(X, weights, weights_inputs,
                                                   bias, num_hidden_layer,
                                                   num_neurons_layer)
                    yu=0

        else:  # Threshold MSE
            y = 5
            # TODO: Implement Threshold as stopping condition
        return 1

    def NetInput(self, X, weight, weights_inputs, bias, num_hidden_layer,
                 num_neurons_layer):
        """This function will get the Net of each neuron """
        ind = 1
        ind_WInput = 0
        for i in range(num_hidden_layer + 1):
            if i == 0:
                for j in range(num_neurons_layer):
                    V = bias * weight["w"+str(ind)][0] \
                        + X[0] * weight["w"+str(ind)][1] \
                        + X[1] * weight["w"+str(ind)][2] \
                        + X[2] * weight["w"+str(ind)][3] \
                        + X[3] * weight["w"+str(ind)][4]
                    Y = self.sigmoid(V)
                    weights_inputs[ind-1] = Y
                    ind += 1
            elif i == num_hidden_layer:
                tmp=2
            else:
                for j in range(num_neurons_layer):
                    V = bias * weight["w"+str(ind)][0] \
                        + weights_inputs[ind_WInput] * weight["w"+str(ind)][1] \
                        + weights_inputs[ind_WInput + 1] * weight["w"+str(ind)][2] \
                        + weights_inputs[ind_WInput + 2] * weight["w"+str(ind)][3]
                    ind_WInput += 3
                    Y = self.sigmoid(V)
                    weights_inputs[ind-1] = Y
                    ind += 1
        return weights_inputs

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))