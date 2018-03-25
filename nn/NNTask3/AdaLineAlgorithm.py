import numpy as np


class AdaLineAlgo:
    def __init__(self):
        pass

    def adaLine_algorithm_train(self, featureX, featureY, classlabel, eta, m, bias, erroTh):
        i = 0
        error = 1
        c1 = classlabel[0]
        c2 = classlabel[len(featureX)-1]
        print ('c1 = ', c1 , ' --- c2 = ', c2)
        #print(featureX,featureY,classlabel,eta,m,bias)
        epoch = 0
        w1 = np.random.rand(1)[0]
        w2 = np.random.rand(1)[0]
        w3 = np.random.rand(1)[0]
        print(w1,w2,w3)
        w = [w1,w2,w3]
        #w = [0.8,0.3,0.6]
    
        while  epoch < m:
            #MSE = 0
            #errorMSE = 0
            #lMSE = 0
            for i in range(0,len(featureX)):
                x = [featureX[i],featureY[i]]
                d = classlabel[i]
                v = self.net_input(x,w,bias)
                #y = self.signum(v)
                y = v
                if d == c1:
                    d = 1
                else:
                    d = -1
                error = d - y
                w[0] = w[0] + eta * error
                w[1] = w[1] + eta * error * x[0]
                w[2] = w[2] + eta * error * x[1]
                #MSE_ = (error**2)
                #MSE = MSE + MSE_
                #if epoch !=1:
                #    w[0] = w[0] + eta * errorMSE
                #    w[1] = w[1] + eta * errorMSE * x[0]
                #    w[2] = w[2] + eta * errorMSE * x[1]
                
            epoch = epoch + 1
            errorMSE = self.updateError(w, bias, featureX, featureY, classlabel)
            w1 = w[1]
            w2 = w[2]
            b  = w[0] * bias
            #errorMSE = MSE / (2*len(featureX))
            '''if errorMSE > lMSE:
                errorMSE = lMSE
            else:
                lMSE = errorMSE'''
            if errorMSE < erroTh:
                break
        print(errorMSE)
        print(w1,w2,b)
        print('Done!')
        return (w1,w2,b)



    def updateError(self,weight,bias, featureX, featureY, classlabel):
        MSE = 0
        for i in range(0,len(featureX)):
            x = [featureX[i],featureY[i]]
            d = classlabel[i]
            v = self.net_input(x,weight,bias)
            y = v 
            error = d - y
            MSE_ = (error**2)
            MSE = MSE + MSE_
        MSE = MSE / (2*len(featureX))
        return MSE

    def adalineAlgoTest(self,featureX,featureY,w,bias):
        x = [featureX,featureY]
        v = self.net_inputTest(x,w,bias)
        y = self.signum(v)
        return y
    def net_input(self,X,weight,bias):
        """Calculate net input"""
        v = bias * weight[0] + weight[1]*X[0]+weight[2]*X[1]
        return v
    def net_inputTest(self,X,weight,bias):
        """Calculate net input"""
        v = bias + weight[0]*X[0]+weight[1]*X[1]
        return v
    
    def signum(self,v):
        d = 0
        if(v>=0.0):
            d = 1
        else:
            d = -1  
        return d