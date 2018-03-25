import numpy
import matplotlib.pyplot as plt
from readData import ReadData
from NNTask3.plotIris import PlotIris

def NN(m1,m2,w1,w2,b):
    z = m1*w1 + m2*w2 + b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1+numpy.exp(-x))

def slope(b):
    return 2 * (b - 4) 

w1 = numpy.random.randn()
w2 = numpy.random.randn()
b = numpy.random.randn()
o = NN(3,1,w1,w2,b)
print(o)

print(b)
for i in range(10):
    b = b - .1 * slope(b)
    print(b)

dataset = ReadData()
dataset.readData()
X1_training = dataset.IrisX1[0:30]
X1_training.extend(dataset.IrisX1[50:80])
X1_training.extend(dataset.IrisX1[100:130])
vector = [X1_training[0],X1_training[1]]
print(vector)
x = [1 for i in range (0,5)]
x.extend([0 for i in range(1,5)])
x.extend([2 for i in range(1,5)])
print(x)
#pi = PlotIris()
#pi.plot(rd.IrisX1, rd.IrisX2, 'X1', 'X2')
'''
IrisX1 = []
IrisX2 = []
IrisX3 = []
IrisX4 = []
IrisY = []

with open('iris.txt') as irisTxt:
    irisTxt.readline()
    for line in irisTxt:
        #print(line)
        dt = line.split(',')
        IrisX1.append(float(dt[0]))
        IrisX2.append(float(dt[1]))
        IrisX3.append(float(dt[2]))
        IrisX4.append(float(dt[3]))

        if (dt[4] == 'Iris-setosa'):
            IrisY.append(0)
        elif (dt[4] == 'Iris-versicolor'):
            IrisY.append(1)
        else:
            IrisY.append(2)

plt.plot(IrisX2[0:50], IrisX4[0:50], 'ro')
plt.plot(IrisX2[50:100], IrisX4[50:100], 'go')
plt.plot(IrisX2[100:150], IrisX4[100:150], 'bo')
plt.show()'''

#-0.41842813938021917 0.394989954231887 1.0
#x1, x2 -> c1, c2, bias, eta = 0.02, epochs = 400 -> 100%
#x1, x3 -> c1, c3, bias, eta = 0.02, epochs = 400 -> 100%
#x1, x3 -> c2, c3, bias, eta = 0.02, epochs = 400 -> 90%