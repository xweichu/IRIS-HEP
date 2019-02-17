import uproot

class RootFile:

    def __init__(self, name = '', size = 0, branches = []):
        self._name = name
        self._size = size
        self._branches = branches
    
    def setName(self, name):
        self._name = name
    
    def getName(self):
        return self._name
    
    def setSize(self, size):
        self._size = size
    
    def getSize(self):
        return self._size
    
    def setBranches(self, branches):
        self._branches = branches
    
    def getBranches(self):
        return self._branches

    
    def extractMetadata(self):
        rootfile = uproot.open(self._name)
        print('Extracting metadata from the root file...')
        trees = rootfile.keys()

        for tree in trees:
            self.extractTreeMetadata(rootfile[tree])
        
        


    def extractTreeMetadata(self, tree):
        for key in tree.keys():
            mybranch = tree[key]
            subbranches = mybranch.keys()
            print(dir(mybranch))
            


        

        # print(rootFileHandler.allkeys())
        # print(rootFileHandler.allitems())
        # print(rootFileHandler.iterkeys())


