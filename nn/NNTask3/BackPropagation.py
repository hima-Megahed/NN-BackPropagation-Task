import numpy as np
import math


class BackPropagation:


    def __init__(self):
        self.weights_inputs=[];
        self.weights=[];
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
                    error = self.propagate_error(weights_inputs, weights,
                                                 num_hidden_layer,
                                                 num_neurons_layer,
                                                 YOut, activation_function)

                    weights = self.update_weights(weights_inputs, weights, num_hidden_layer
                       ,num_neurons_layer, eta, error)

        else:  # Threshold MSE
            MSE = 10000000.0
            while MSE > threshold:
               for j in range(len(features["X1"])):
                    # getting input vector
                    X = [features["X1"][j], features["X2"][j],
                         features["X3"][j], features["X4"][j]]
                    YOut = features["Y"][j]
                    weights_inputs = self.NetInput(X, weights, weights_inputs,
                                                   bias, num_hidden_layer,
                                                   num_neurons_layer,
                                                   activation_function)
                    error = self.propagate_error(weights_inputs, weights,
                                                 num_hidden_layer,
                                                 num_neurons_layer,
                                                 YOut, activation_function)

                    weights = self.update_weights(weights_inputs, weights, num_hidden_layer
                       ,num_neurons_layer, eta, error)

                    MSE = self.ComputeMeanSquareError(error)

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
    def ComputeMeanSquareError(self,error):
        sum = 0.0
        for i in range(len(error)):
            sum += error[i]**2
        return sum/len(error)
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
        error = [0] * len(weights_inputs)
        ind = len(weights_inputs) - 1
        for i in reversed(range(num_hidden_layer+1)):
            print(i)
            if i != num_hidden_layer:
                for j in range(num_neurons_layer):
                    sum = 0.0
                    if i+1 == num_hidden_layer:
                        for k in range(3):
                            sum += weights_inputs[(i+1)*num_neurons_layer+k]*error[(i+1)*num_neurons_layer+k]
                    else:
                        for k in range(num_neurons_layer):
                            sum += weights_inputs[(i + 1) * num_neurons_layer + k]*error[(i+1)*num_neurons_layer+k]

                    error[ind] = sum * self.drivative_transfer(activation_function,weights_inputs[ind])
                    ind -= 1

            else:
                for j in range(3):
                    y = YOut - weights_inputs[ind]
                    error[ind]=y* self.drivative_transfer(activation_function,weights_inputs[ind])
                    ind -= 1

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


    def MainAlgorithmTesting(self,features,bias,activation_function,num_hidden_layer,num_neurons_layer):
        Output = []
        for j in range(len(features["X1"])):
                    # getting input vector
                    X = [features["X1"][j], features["X2"][j],
                         features["X3"][j], features["X4"][j]]
                    YOut = features["Y"][j]
                    weights_inputs = self.NetInput(X, self.weights, self.weights_inputs,
                                                   bias, num_hidden_layer,
                                                   num_neurons_layer,
                                                   activation_function)
                    Length = len(weights_inputs)
                    if weights_inputs[Length - 1] > weights_inputs[Length - 2] & \
                        weights_inputs[Length - 1] > weights_inputs[Length -3]:
                        Output.append(1)
                    elif weights_inputs[Length - 2] > weights_inputs[Length - 1] & \
                        weights_inputs[Length - 2] > weights_inputs[Length -3]:
                        Output.append(2)
                    else:
                        Output.append(3)
        return Output
