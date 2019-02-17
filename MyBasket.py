class MyBasket:

    def __init__(self, branchPath = [], number = 0, offset = 0, size = 1, startEntry = 0, endEntry = 0, accessTime = -1):
        self._branchPath = branchPath
        self._number = number
        self._offset = offset
        self._size = size
        self._startEntry = startEntry
        self._endEntry = endEntry
        self._accessTime = accessTime

    def getBranchPath(self):
        return self._branchPath
    
    def setBranchPath(self,branchPath):
        if(branchPath == None):
            print("Branch Path can't be null!")
            return
        self._branchPath = branchPath
    
    def getNumber(self):
        return self._number
    
    def setNumber(self,number):
        if(number < 0):
            print("Number can't be negative!")
            return
        self._number = number

    def getOffset(self):
        return self._offset
    
    def setOffset(self,offset):
        if(offset < 0):
            print("Offset can't be negative!")
            return
        self._offset = offset
    
    def getSize(self):
        return self._size
    
    def setSize(self,size):
        if(size < 0):
            print("Size can't be negative!")
            return
        self._size = size

    def getStartEntry(self):
        return self._startEntry
    
    def setStartEntry(self,startEntry):
        if(startEntry < -1):
            print("Start Entry can't be negative!")
            return
        self._startEntry = startEntry

    def getEndEntry(self):
        return self._endEntry
    
    def setEndEntry(self,endEntry):
        if(endEntry < -1):
            print("End Entry can't be negative!")
            return
        self._endEntry = endEntry
    
    def getAccessTime(self):
        return self._accessTime
    
    def setAccessTime(self,accessTime):
        if(accessTime < -1):
            print("Access time can't be negative!")
            return
        self._accessTime = accessTime

    def __gt__(self, other):
        return self._offset > other._offset

    def __lt__(self, other):
        return self._offset < other._offset
    
    def __eq__(self, other):
        return self._offset ==  other._offset
    
    def toString(self):
        basketPath = ''
        for i in range(len(self._branchPath)):
            basketPath = + self._branchPath[i] + ' '
        return basketPath + str(self._number) + ',' + str(self._offset) + ',' + str(self._size) + ',' + str(self._startEntry) + ',' + str(self._endEntry) + ',' + str(self._accessTime)
    
    def save(self, outFileHandler):
        outFileHandler.write('Basket=' + str(self._number) + ',' + str(self._offset) + ',' + str(self._size) + ',' + str(self._startEntry) + ',' + str(self._endEntry) + ',' + str(self._accessTime) + '\n')
        outFileHandler.flush()


    def restore(self, inputFileHandler):
        line = inputFileHandler.readline()
        line = line.split('=')
        line = line[1]
        basket = line.split(',')
        self.setBranchPath([])
        self.setNumber(int(basket[0]))
        self.setOffset(int(basket[1]))
        self.setSize(int(basket[2]))
        self.setStartEntry(int(basket[3]))
        self.setEndEntry(int(basket[4]))
        
        if(len(basket) == 6):
            self.setAccessTime(int(basket[5]))
        else:
            self.setAccessTime(-1)


    