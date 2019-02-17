from MyBasket import MyBasket
class MyBranch:

    def __init__(self, path = [], baskets = [], numOfBaskets = 0, size = 0):
        self._path = path
        self._baskets = baskets
        self._numOfBaskets = numOfBaskets
        size = 0
        for basket in self._baskets:
            size += basket.getSize()

        self._size = size
        self.setNumOfBaskets(len(self._baskets))

    def getPath(self):
        return self._path
    
    def setPath(self,path):
        if(path == None):
            print("Path can't be None!")
            return
        self._path = path
    
    def getSize(self):
        return self._size
    
    def setSize(self,size):
        if(size < 0):
            print("Size can't be negative!")
            return
        self._size = size

    def getNumOfBaskets(self):
        return self._numOfBaskets
    
    def setNumOfBaskets(self, numOfBaskets):
        if(numOfBaskets < 0):
            print("Number of baskets can't be negtive!")
            return
        self._numOfBaskets = numOfBaskets
        
    def getBaskets(self):
        return self._baskets

    def setBaskets(self,baskets):
        self._baskets = baskets


    def __gt__(self, other):
        minvalue = min(len(self.getPath()),len(other.getPath()))
        for i in range(minvalue):
            if(self.getPath()[i] == other.getPath()[i]):
                continue
            else:
                if(self.getPath()[i] > other.getPath()[i]):
                    return True
                else:
                    return False
        
        if(len(self.getPath()) > len(other.getPath())):
            return True
        else:
            return False


    def __lt__(self, other):
        minvalue = min(len(self.getPath()),len(other.getPath()))
        for i in range(minvalue):
            if(self.getPath()[i] == other.getPath()[i]):
                continue
            else:
                if self.getPath()[i] < other.getPath()[i]:
                    return True
                else:
                    return False
        
        if(len(self.getPath()) < len(other.getPath())):
            return True
        else:
            return False
    
    def __eq__(self, other):

        if(len(self.getPath()) != len(other.getPath())):
            return False

        for i in range(len(self.getPath())):
            if(self.getPath()[i] != other.getPath()[i]):
                return False
        return True
    
    def toString(self):
        path = ''
        for i in range(len(self._path)):
            path = + self._path[i] + ' '
        return path + str(self._numOfBaskets) + ',' + str(self._size) 

    def save(self, outFileHandler):
        path = ''
        for i in range(len(self._path)):
            path += self._path[i] + ' '
        
        outFileHandler.write("Branch-Path=" + path + '\n')
        outFileHandler.write("Branch-Size=" + str(self.getSize())+'\n')
        outFileHandler.write("Branch-Baskets=" + str(self.getNumOfBaskets())+'\n')
        basketsOfBranch = self.getBaskets()

        for basket in basketsOfBranch:
            basket.save(outFileHandler)
        outFileHandler.flush()


    def restore(self, inputFileHandler):
        line = inputFileHandler.readline()
        line = line.split('=')
        line = line[1]
        path = line.split(' ')
        self.setPath(path)

        line = inputFileHandler.readline()
        line = line.split('=')
        size = line[1]
        self.setSize(int(size))

        line = inputFileHandler.readline()
        line = line.split('=')
        basketNo = int(line[1])
        self.setNumOfBaskets(basketNo)

        baskets = []
        for i in range(basketNo):
            mybasket = MyBasket()
            mybasket.restore(inputFileHandler)
            mybasket.setBranchPath(self._path)
            baskets.append(mybasket)
        
        self.setBaskets(baskets)












        # basket = line.split(',')
        # self.setBranchPath([])
        # self.setNumber(basket[0])
        # self.setOffset(basket[1])
        # self.setSize(basket[2])
        # self.setStartEntry(basket[3])
        # self.setEndEntry(basket[4])
        
        # if(len(basket) == 6):
        #     self.setAccessTime(basket[5])
        # else:
        #     self.setAccessTime(-1)


    