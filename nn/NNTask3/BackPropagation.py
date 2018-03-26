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
        weights, weights_inputs = self.initialize(num_hidden_layer, num_neurons_layer)

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
                                                   num_neurons_layer,
                                                   activation_function)
                   # error = self.propagate_error(weights_inputs, weights,
                    #                             num_hidden_layer,
                     #                            num_neurons_layer,
                      #                           YOut, activation_function)
                    error = [1,2,3,4,5,6,7,8,9]
                    weights = self.update_weights(weights_inputs, weights, num_hidden_layer
                       ,num_neurons_layer, eta, error)

        else:  # Threshold MSE
            y = 5
            # TODO: Implement Threshold as stopping condition
        return 1

    def NetInput(self, X, weight, weights_inputs, bias, num_hidden_layer,
                 num_neurons_layer, activation_function):
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

                    Y = self.activate(activation_function, V)
                    weights_inputs[ind-1] = Y
                    ind += 1
            elif i == num_hidden_layer:
                for j in range(3):
                    V = bias * weight["w"+str(ind)][0]
                    for k in range(1, num_neurons_layer + 1):
                        V += weights_inputs[ind_WInput + k - 1] * weight["w"+str(ind)][k]

                    Y = self.activate(activation_function, V)
                    weights_inputs[ind-1] = Y
                    ind += 1
            else:
                for j in range(num_neurons_layer):
                    V = bias * weight["w" + str(ind)][0]
                    for k in range(1, num_neurons_layer + 1):
                        V += weights_inputs[ind_WInput + k - 1] * \
                             weight["w" + str(ind)][k]
                    Y = self.activate(activation_function, V)
                    weights_inputs[ind-1] = Y
                    ind += 1
                ind_WInput += num_neurons_layer
        return weights_inputs

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    @staticmethod
    def Hyperbolic_tangent(x):
        return np.tanh(x)

    def activate(self,activation_function, x):
        if activation_function == 1:
            return self.sigmoid(x)
        else:
            return self.Hyperbolic_tangent(x)

    @staticmethod
    def initialize(num_hidden_layer, num_neurons_layer):
        weights = {}
        weights_inputs = []
        ind = 1
        for i in range(num_hidden_layer + 1):  # num of hidden layers and output layer
            if i == 0:
                for j in range(num_neurons_layer):
                    weights["w" + str(ind)] = [np.random.rand(1)[0]
                                               for k
                                               in range
                                               (5)]
                    weights_inputs.append(0)
                    ind += 1
            elif i == num_hidden_layer:
                for j in range(int(3)):
                    weights["w" + str(ind)] = [np.random.rand(1)[0]
                                               for k
                                               in range
                                               (
                                                   num_neurons_layer + 1)]  # inputs to neuron number of last neurons + bias
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
    # TODO: Implement backward error propagation
        return weights, weights_inputs

    def drivative_transfer(self, activation_function, x):
        if activation_function == 1:
            return self.sigmoid_derivative(x)
        else:
            return self.Hyperbolic_tangent_derivative(x)

    @staticmethod
    def sigmoid_derivative(x):
        return x * (1-x)

    @staticmethod
    def Hyperbolic_tangent_derivative(x):
        return 1- np.power(np.tanh(x),2)

    def propagate_error(self, weights_inputs, weight, num_hidden_layer,
                        num_neurons_layer, YOut, activation_function):
        error = list(len(weights_inputs))
        ind = len(weights_inputs) - 1
        for i in reversed(range(num_hidden_layer)):
            if i != num_hidden_layer:
                for j in range(num_neurons_layer):
                    sum = 0.0
                    if i+1 == num_hidden_layer:
                        for k in range(2):
                            sum += weights_inputs((i+1)*num_neurons_layer+k)*error[(i+1)*num_neurons_layer+k]
                    else:
                        for k in range(num_neurons_layer):
                            sum += weights_inputs[(i + 1) * num_neurons_layer + k]*error[(i+1)*num_neurons_layer+k]
                    error[i*num_hidden_layer+j] = sum * self.drivative_transfer(activation_function,weights_inputs[i*num_neurons_layer+j]);
            else:
                for j in range(2):
                    y = YOut - weights_inputs[ind]
                    ind -= 1
                    error[num_hidden_layer*num_neurons_layer+(3-j)]=y* self.drivative_transfer(activation_function,weights_inputs[num_hidden_layer*num_neurons_layer+(3-j)])
        return error

    def update_weights(self, weights_inputs, weight, num_hidden_layer
                       ,num_neurons_layer, eta, error):
        ind = len(weight)
        ind_WInput = len(weights_inputs) - 1
        ind_E = len(error) - 1
        for i in reversed(range(num_hidden_layer + 1)):
            # output layer weights
            if i == num_hidden_layer:
                for j in range(3):
                    weight["w" + str(ind)] = eta * weights_inputs[ind_WInput]\
                                             * error[ind_E]
                    ind -= 1
                    ind_WInput -= 1
                    ind_E -= 1
            else:
                for j in range(num_neurons_layer):
                    weight["w" + str(ind)] = eta * weights_inputs[ind_WInput]\
                                             * error[ind_E]
                    ind -= 1
                    ind_WInput -= 1
                    ind_E -= 1
        return weight