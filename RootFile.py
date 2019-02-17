import uproot
from MyBasket import MyBasket 
from MyBranch import MyBranch

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
            subBranches = mybranch.values()
            basketBytes = mybranch._fBasketBytes
            basketEntries = mybranch._fBasketEntry
            numOfBaskets = len(basketBytes)
            branchPath = []

            branchPath.append(str(key))
            branchPath.append(str(mybranch.name))


            branchBaskets = []
            for i in range(numOfBaskets - 1 ):
                offset = mybranch._fBasketSeek[i]
                size = basketBytes[i]
                startEntry = basketEntries[i]
                endEntry = basketEntries[i + 1] -1;
                mybasket = MyBasket([], i , offset, size , startEntry, endEntry )
                branchBaskets.append(mybasket)
            
            # print(branchPath)
            newbranch =  MyBranch(branchPath, branchBaskets)
            self._branches.append(newbranch)
            self.extractBranchMetadata(subBranches, branchPath, 1+ 1)

    
    def extractBranchMetadata(self, subBranches, branchName, level):
        # print(subBranches )
        
        for mybranch in subBranches:
            # print(dir(mybranch))
            subSubBranches = mybranch.values()
            basketBytes = mybranch._fBasketBytes
            basketEntries = mybranch._fBasketEntry
            numOfBaskets = len(basketBytes)
            branchPath = []
            for pre_path in branchName:
                branchPath.append(pre_path)

            branchPath.append(str(mybranch.name))

            branchBaskets = []

            for i in range(numOfBaskets - 1):
                offset = mybranch._fBasketSeek[i]
                size = basketBytes[i]
                startEntry = basketEntries[i]
                endEntry = basketEntries[i + 1] -1
                mybasket = MyBasket([], i , offset, size , startEntry, endEntry )
                branchBaskets.append(mybasket)
            
            newbranch =  MyBranch(branchPath, branchBaskets)
            self._branches.append(newbranch)
            self.extractBranchMetadata(subSubBranches, branchPath, level + 1);


    def save(self, outFileHandler):
        print('Saving metadata of Root file ... ')
        outFileHandler.write('File-Path=' + str(self.getName()) + '\n')
        outFileHandler.write('File-Size=' + str(self.getSize()) + '\n')
        outFileHandler.write('File-Branches=' + str(len(self.getBranches())) + '\n')
        for branch in self.getBranches():
            branch.save(outFileHandler)
        
        
                

    def restore(self, inputFileHandler):
        print('Restoring metadata of Root file ... ')
        line = inputFileHandler.readline()
        line = line.split('=')
        filePath = line[1]

        line = inputFileHandler.readline()
        line = line.split('=')
        fileSize = int(line[1])

        line = inputFileHandler.readline()
        line = line.split('=')
        fileBranches = int(line[1])

        branches = []

        for i in range(fileBranches):
            myBranch = MyBranch()
            myBranch.restore(inputFileHandler)
            branches.append(myBranch)
        
        self.setBranches(branches)
        self.setName(filePath)
        self.setSize(fileSize)




        

        # print(rootFileHandler.allkeys())
        # print(rootFileHandler.allitems())
        # print(rootFileHandler.iterkeys())


