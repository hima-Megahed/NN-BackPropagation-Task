import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from readData import ReadData
from NNTask3.plotIris import PlotIris
import NNTask3.BackPropagation
import numpy as np
from NNTask3.AdaLineAlgorithm import AdaLineAlgo

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.choosenClasses= tk.StringVar(self.root)
        self.chosenFeatures = tk.StringVar(self.root)
        self.learnRate = tk.StringVar(self.root)
        self.epochsNo = tk.StringVar(self.root)
        self.bias = tk.IntVar(self.root)
        self.bias.set(0)
        self.root.resizable(height=False, width=False)
        self.root.title("NN Task1")
        self.root.geometry("300x500")
        self.X1_training = []
        self.X2_training = []
        self.X1_testing = []
        self.X2_testing = []
        self.classlable_training = []
        self.classlable_testing = []
        self.dataset = []
        self.errorTh =tk.IntVar(self.root)
        self.plotLine = tk.IntVar(self.root)
        self.plotLine.set(0)
        self.c1 = 0
        self.c2 = 0
        self.w1 = 0
        self.w2 = 0
        self.b = 0
        self.NumberOfHiddenLayers = tk.StringVar(self.root)
        self.NumberOfNeuronsInEachLayer = tk.StringVar(self.root)
        self.activationFunction = tk.IntVar()
        self.stoppingCriteria = tk.IntVar()
        self.initializeComponents()
        self.root.mainloop()
        #######################

    def initializeComponents(self):
        def defocus(event):
            event.widget.master.focus_set()
        tk.Label(self.root,text="# Of Hidden Layers").place(relx=0.11, rely=0.05)
        HLEntry = tk.Entry(self.root,width=10 , textvariable = self.NumberOfHiddenLayers)
        HLEntry.place(relx=0.64, rely=0.05)

        tk.Label(self.root,text="# Of Neurons In Each Layer").place(relx=0.11, rely=0.14)
        NEntry = tk.Entry(self.root, width=10, textvariable = self.NumberOfNeuronsInEachLayer)
        NEntry.place(relx=0.64, rely=0.14)

        tk.Label(self.root,text="Enter Learning Rate(eta):").place(relx=0.11, rely=0.23)
        eta = tk.Entry(self.root,width=10,textvariable=self.learnRate )
        eta.place(relx=0.64, rely=0.23)

        tk.Label(self.root,text="Enter Number of Epochs:").place(relx=0.11, rely=0.32)
        epochs = tk.Entry(self.root,width=10,textvariable=self.epochsNo)
        epochs.place(relx=0.64, rely=0.32)

        tk.Label(self.root, text="Choose an activation function").place(relx=0.03, rely=0.41)
        tk.Radiobutton(self.root,
                       text="Sigmoid",
                       variable=self.activationFunction,
                       value=1).place(relx=0.03, rely=0.45)
        tk.Radiobutton(self.root,
                       text="Hyperbolic Tangent Sigmoid",
                       variable=self.activationFunction,
                       value=2).place(relx=0.03, rely=0.49)

        tk.Label(self.root, text="Bias:").place(relx=0.70, rely=0.41)
        tk.Checkbutton(self.root, variable=self.bias).place(relx=0.78,
                                                            rely=0.41)

        tk.Label(self.root, text="Choose The Stopping Criteria").place(
            relx=0.03, rely=0.58)
        tk.Radiobutton(self.root,
                       text="# of Epochs",
                       variable=self.stoppingCriteria,
                       value=1).place(relx=0.03, rely=0.62)
        tk.Radiobutton(self.root,
                       text="MSE Threshold",
                       variable=self.stoppingCriteria,
                       value=2).place(relx=0.03, rely=0.66)

        errorTh = tk.Entry(self.root, width=10, textvariable=self.errorTh)\
            .place(relx=0.64, rely=0.66)

        tk.Button(self.root, text="Plotting",width=10, fg="Black",bg="light Gray", command=lambda: self.plotFeatures()).place(relx=0.03, rely=0.80)
        tk.Button(self.root, text="Learning",width=10, fg="Black",bg="light Gray", command=lambda: self.learning()).place(relx=0.35, rely=0.80)
        tk.Button(self.root, text="Testing",width=10, fg="Black",bg="light Gray", command=lambda: self.testing()).place(relx=0.67, rely=0.80)

    def plotFeatures(self):
        chosenFeatures = self.chosenFeatures.get()
        feature1 = int(chosenFeatures[1])
        feature2 = int(chosenFeatures[6])
        choosenClasses = self.choosenClasses.get()
        c1 = int(choosenClasses[1])
        c2 = int(choosenClasses[6])
        featureX,featureY = self.initilizeData()
        pi = PlotIris()
        plot = self.plotLine.get()
        if plot == 1:
            lineX = range(int(np.min(featureX) - 2), int(np.max(featureX) + 2))
            lineY = [-(self.b + self.w1 * xi) / self.w2 for xi in lineX]
            pi.plot_(featureX, featureY, 'X'+ str(feature1), 'X'+str(feature2),c1,c2, lineX, lineY)
        else:
            pi.plot(featureX, featureY, 'X'+ str(feature1), 'X'+str(feature2),c1,c2)

    def initilizeData(self):
        chosenFeatures = self.chosenFeatures.get()
        feature1 = int(chosenFeatures[1])
        feature2 = int(chosenFeatures[6])
        learnRate = float(self.learnRate.get())
        epochsNo = int(self.epochsNo.get())
        bias = self.bias.get()
        rd = ReadData()
        rd.readData()
        featureX = self.returnFeature(feature1,rd)
        featureY = self.returnFeature(feature2,rd)
        return (featureX, featureY)
        
    def manageTrainingFeatures(self):
        #initilize X1 and X2
        featureX,featureY = self.initilizeData()
        choosenClasses = self.choosenClasses.get()
        class1 = int(choosenClasses[1])
        class2 = int(choosenClasses[6])
        self.classlable_training = []
        self.X1_training = []
        self.X2_training = []
        ####
        if class1 == 1:
            self.X1_training = featureX[0:30]
            self.X2_training = featureY[0:30]
            self.classlable_training = [1 for i in range(0,30)]
            if class2 == 2:
                self.X1_training.extend(featureX[50:80])
                self.X2_training.extend(featureY[50:80])
                self.classlable_training.extend([2 for i in range(0,30)])
            else:
                self.X1_training.extend(featureX[100:130])
                self.X2_training.extend(featureY[100:130])
                self.classlable_training.extend([3 for i in range(0,30)])
        elif class1 == 2:
            self.X1_training = featureX[50:80]
            self.X2_training = featureY[50:80]
            self.classlable_training= [2 for i in range(0,30)]
            self.X1_training.extend(featureX[100:130])
            self.X2_training.extend(featureY[100:130])
            self.classlable_training.extend([3 for i in range(0,30)])

    def manageTestingFeatures(self):
        featureX,featureY = self.initilizeData()
        choosenClasses = self.choosenClasses.get()
        class1 = int(choosenClasses[1])
        class2 = int(choosenClasses[6])
        self.c1 = class1
        self.c2 = class2
        ####
        if class1 == 1:
            self.X1_testing = featureX[30:50]
            self.X2_testing = featureY[30:50]
            self.classlable_testing = [1 for i in range(0,20)]
            if class2 == 2:
                self.X1_testing.extend(featureX[80:100])
                self.X2_testing.extend(featureY[80:100])
                self.classlable_testing.extend([2 for i in range(0,20)])
            else:
                self.X1_testing.extend(featureX[130:150])
                self.X2_testing.extend(featureY[130:150])
                self.classlable_testing.extend([3 for i in range(0,20)])
        elif class1 == 2:
            self.X1_testing = featureX[80:100]
            self.X2_testing = featureY[80:100]
            self.classlable_testing= [2 for i in range(0,20)]
            self.X1_testing.extend(featureX[130:150])
            self.X2_testing.extend(featureY[130:150])
            self.classlable_testing.extend([3 for i in range(0,20)])
    def returnFeature(self,index,rd):
        feature = []
        if index == 1:
            feature = rd.IrisX1
        elif index == 2:
            feature = rd.IrisX2
        elif index == 3:
            feature = rd.IrisX3
        else:
            feature = rd.IrisX4
        return feature
    
    def learning(self):
        adalinealgo = AdaLineAlgo()
        bias = self.bias.get()
        eta = float(self.learnRate.get())
        epochsNo = int(self.epochsNo.get())
        errorTh = float(self.errorTh)
        self.manageTrainingFeatures()
        w1,w2,b = adalinealgo.adaLineAlgoTrain(self.X1_training,self.X2_training,self.classlable_training,eta,epochsNo,bias,errorTh)
        self.w1 = w1
        self.w2 = w2
        self.b = b
        #plt.plot(w1)
    def testing(self):
        adalinealgo = AdaLineAlgo()
        #bias = self.bias.get()
        self.manageTestingFeatures()
        w = [self.w1,self.w2]
        conf = np.zeros([2,2], dtype='int32')
        for i in range(0,len(self.X1_testing)):
            y = adalinealgo.adalineAlgoTest(self.X1_testing[i],self.X2_testing[i],w,self.b)
            if (y == 1 and self.c1 == self.classlable_testing[i]):
                conf[0, 0] = conf[0, 0] + 1
            elif (y == -1 and self.classlable_testing[i] == self.c2):
                conf[1,1] = conf[1,1] + 1
            elif (y == 1 and self.classlable_testing[i] != self.c1):
                conf[0, 1] = conf[0, 1] + 1
            elif (y == -1 and self.classlable_testing[i] != self.c2):
                conf[1, 0] = conf[1, 0] + 1                

            print(self.X1_testing[i],self.X2_testing[i])
            print(y)
        print(self.classlable_testing)
        print(conf)
