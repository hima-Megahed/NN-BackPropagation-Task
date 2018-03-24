import matplotlib.pyplot as plt

class PlotIris:
    def __init__(self):
        pass
        
    def plot(self,x1,x2,x1_label,x2_lable,c1,c2):
        
        if c1 ==1 and c2 == 2:
            plt.plot(x1[0:50],   x2[0:50], 'ro')
            plt.plot(x1[50:100], x2[50:100], 'go')
        elif c1 == 2 and c2 == 3:
            plt.plot(x1[50:100], x2[50:100], 'go')
            plt.plot(x1[100:150],x2[100:150], 'bo')
        else:
            plt.plot(x1[0:50],   x2[0:50], 'ro')
            plt.plot(x1[100:150],x2[100:150], 'bo')
        plt.title('plotting of features')
        plt.xlabel(x1_label)
        plt.ylabel(x2_lable)
        plt.title('plotting of features')
        plt.show()
    def plot_(self,x1,x2,x1_label,x2_lable,c1,c2, lineX, lineY):
        
         
        '''plt.plot(x1[0:50],   x2[0:50], 'ro')
        plt.plot(x1[50:100], x2[50:100], 'go')
        plt.plot(x1[100:150],x2[100:150], 'bo')'''

        if c1 ==1 and c2 == 2:
            plt.plot(x1[0:50],   x2[0:50], 'ro')
            plt.plot(x1[50:100], x2[50:100], 'go')
        elif c1 == 2 and c2 == 3:
            plt.plot(x1[50:100], x2[50:100], 'go')
            plt.plot(x1[100:150],x2[100:150], 'bo')
        else:
            plt.plot(x1[0:50],   x2[0:50], 'ro')
            plt.plot(x1[100:150],x2[100:150], 'bo')

        plt.plot(lineX, lineY)
        plt.xlabel(x1_label)
        plt.ylabel(x2_lable)
        plt.title('plotting of features')
        plt.show()