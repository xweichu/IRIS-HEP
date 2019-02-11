class MyBranch:

    def __init__(self, path = [], baskets = [], numOfBaskets = 0, size = 0):
        self._path = path
        self._baskets = baskets
        self._numOfBaskets = numOfBaskets
        self._size = size

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
        min = min(len(self.getPath()),len(other.getPath()))
        for i in range(min):
            if(self.getPath()[i] == other.getPath()[i]):
                continue
            else:
                if(self.getPath()[i] > other.getPath()[i])):
                    return true
                else:
                    return false
        
        if(len(self.getPath()) > len(other.getPath())):
            return true
        else:
            return false


    def __lt__(self, other):
        min = min(len(self.getPath()),len(other.getPath()))
        for i in range(min):
            if(self.getPath()[i] == other.getPath()[i]):
                continue
            else:
                if(self.getPath()[i] < other.getPath()[i])):
                    return true
                else:
                    return false
        
        if(len(self.getPath()) < len(other.getPath())):
            return true
        else:
            return false
    
    def __eq__(self, other):

        if(len(self.getPath()) != len(other.getPath())):
            return false

        for i in range(len(self.getPath())):
            if(self.getPath()[i] != other.getPath()[i]):
                return false
        return true
    
    def toString(self):
        path = ''
        for i in range(len(self._path)):
            path = + self._path[i] + ' '
        return path + str(self._numOfBaskets) + ',' + str(self._size) 

    def save(self, outFileHandler):
        path = ''
        for i in range(len(self._path)):
            path = + self._path[i] + ' '
        
        outFileHandler.write("Branch-Path=" + path + '\n')
        outFileHandler.write("Branch-Size=" + str(self.getSize())+'\n')
        outFileHandler.write("Branch-Baskets=" + str(self.getNumOfBaskets())+'\n')
        
        outFileHandler.write('Basket=' + str(self._number) + ',' + str(self._offset) + ',' + str(self._size) + ',' + str(self._startEntry) + ',' + str(self._endEntry) + ',' + str(self._accessTime) + '\n')
        outFileHandler.flush()


    def restore(self, inputFileHandler):
        line = inputFileHandler.readline()
        line = line.split('=')
        line = line[1]
        basket = line.split(',')
        self.setBranchPath([])
        self.setNumber(basket[0])
        self.setOffset(basket[1])
        self.setSize(basket[2])
        self.setStartEntry(basket[3])
        self.setEndEntry(basket[4])
        
        if(len(basket) == 6):
            self.setAccessTime(basket[5])
        else:
            self.setAccessTime(-1)


    