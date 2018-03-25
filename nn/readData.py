class ReadData: 
    def __init__(self):
        self.IrisX1 = []
        self.IrisX2 = []
        self.IrisX3 = []
        self.IrisX4 = []
        self.IrisY = []

    def readData(self):
        with open('./iris.txt') as irisTxt:
            irisTxt.readline()
            for line in irisTxt:
                dt = line.split(',')
                self.IrisX1.append(float(dt[0]))
                self.IrisX2.append(float(dt[1]))
                self.IrisX3.append(float(dt[2]))
                self.IrisX4.append(float(dt[3]))
    
                if (dt[4] == 'Iris-setosa'):
                    self.IrisY.append(0)
                elif (dt[4] == 'Iris-versicolor'):
                    self.IrisY.append(1)
                else:
                    self.IrisY.append(2)
    