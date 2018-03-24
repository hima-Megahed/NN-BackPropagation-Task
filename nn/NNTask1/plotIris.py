import matplotlib.pyplot as plt

class PlotIris:
    def __init__(self):
        pass
        
    def plot(self,x1,x2,x1_label,x2_lable, lineX, lineY):
        plt.plot(x1[0:50],   x2[0:50], 'ro')
        plt.plot(x1[50:100], x2[50:100], 'go')
        plt.plot(x1[100:150],x2[100:150], 'bo')
        plt.plot(lineX, lineY)
        plt.xlabel(x1_label)
        plt.ylabel(x2_lable)
        plt.title('plotting of features')
        plt.show()