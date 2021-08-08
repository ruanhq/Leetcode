#Three LayerNN:
class ThreeLayerNN:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.Yh = np.zeros((1, Y.shape[1]))
        self.param = {}
        self.ch = {}
        self.loss = []
        self.lr = 0.005
        self.nSample = self.Y.shape[1]
        self.dims = [X.shape[1], X.shape[1] // 2, X.shape[1] // 8, 1]
    def nInit(self):
        np.random.seed(10)
        self.param["W1"] = np.random.randn(self.dims[1], self.dims[0])/ np.sqrt(self.dims[0])
        self.param["b1"] = np.zeros((self.dims[1], 1))
        self.param["W2"] = np.random.randn(self.dims[2], self.dims[1])/ np.sqrt(self.dims[1])
        self.param["b2"] = np.zeros((self.dims[2], 1))
        self.param["W3"] = np.random.randn(self.dims[3], self.dims[2])/ np.sqrt(self.dims[2])
        self.param["b3"] = np.zeros((self.dims[3], 1))
        return
    def sigMoid(self, z):
        result = 1/ (1 + np.exp(-z))
        return result
    def Relu(self, z):
        return np.maximum(0, z)
    def nLogLoss(self, Yh):
        lossFunction = (1. / self.nSample) * (-np.dot(self.Y, np.log(Yh).T) - np.dot(1 - self.Y, np.log(1 - Yh).T))
        return lossFunction
    def forward():
        Z1 = self.param["W1"].dot(self.X) + self.param["b1"]
        A1 = self.Relu(Z1)
        self.ch["A1"], self.ch["Z1"] = A1, Z1        
        Z2 = self.param["W2"].dot(A1) + self.param["b2"]
        A2 = self.Relu(Z2)
        self.ch["A2"], self.ch["Z2"] = A2, Z2
        Z3 = self.param["W3"].dot(A2) + self.param["b3"]
        A3 = self.sigMoid(Z3)
        self.ch["Z3"] = Z3
        self.Yh = A3
        loss = self.nLogLoss(A3)
        return self.Yh, loss
    def dRelu(self, z):
        z[z <= 0] = 0
        z[z > 0] = 1
        return z
    def dSigmoid(self, z):
        s = 1/ (1 + np.exp(-z))
        dZ = s * (1 - s)
        return dZ
    def backward(self):
        np.random.seed(42)
        dLoss_Yh = - (np.divide(self.Y, self.Yh) - np.divide(1 - self.Y, 1 - self.Yh))
        dLoss_Z2 = dLoss_Yh * dSigmoid(self.ch["Z2"])
        dLoss_A1 = np.dot(self.param["W2"].T, dLoss_Z2)
        dLoss_W2 = 1./ self.ch["A1"].shape[1] * np.dot(dLoss_Z2, self.ch["A1"].T)
        dLoss_b2 = 1./ self.ch["A1"].shape[1] * np.dot(dLoss_Z2, np.ones([dLoss_Z2.shape[1], 1]))
        dLoss_Z1 = dLoss_A1 * dRelu(self.ch["Z1"])
        dLoss_A0 = np.dot(self.param["W1"].T, dLoss_Z1)
        dLoss_W1 = 1./ self.X.shape[1] * np.dot(dLoss_Z1, self.X.T)
        dLoss_b1 = 1./ self.X.shape[1] * np.dot(dLoss_Z1, np.ones([dLoss_Z1.shape[1], 1]))
        self.param["W1"] = self.param["W1"] - self.lr * dLoss_W1
        self.param["b1"] = self.param["b1"] - self.lr * dLoss_b1
        self.param["W2"] = self.param["W2"] - self.lr * dLoss_W2
        self.param["b2"] = self.param["b2"] - self.lr * dLoss_b2
    def gd(self, X, Y, iter = 3000):
        np.random.seed(1)
        self.nInit()
        for i in range(iter):
            Yh, loss = self.forward()
            self.backward()
            if i % 500 == 0:
                print("Cost after iteration %i: %f" %(i, loss))
                self.loss.append(loss)
        return

#the difference between different activation functions:
#the method is too fast, converge rapidly, rectifies vanishing
#learning rate with high-variance.


def TwoSum(self, numbers: List[int], target: int) -> List[int]:
    currentMap = {}
    result = []
    for i, value in enumerate(numbers):
        remaining = target - numbers[i]
        if remaining in currentMap:
            currentMap.append([currentMap[remaining] + 1, i + 1])
        else:
            currentMap[value] = i
    return list(currentMap)

def TwoSum(self, numbers: List[int], target: int) -> List[int]:
    currentMap = {}
    result = []
    for i, value in enumerate(numbers):
        remaining = target - numbers[i]
        if remaining in currentMap:
            currentMap.append([currentMap[remaining] + 1, i + 1])
        else:
            currentMap[value] = i
    return list(currentMap)

#Construct a dictionary with residualHashMap[0],
#residualHashMap[88% 60]

########
def numPairsDivisibleBy60(time):
    result = 0
    residualHashMap = collections.defaultdict(int)
    for i in range(len(time)):
        if time[i] % 60 == 0:
            result += residualHashMap[0]
        else:
            result += residualHashMap[60 - (time[i] % 60)]
        residualHashMap[time[i] % 60] += 1
    return result


















































