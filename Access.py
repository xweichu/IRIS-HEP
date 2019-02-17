from RootFile import RootFile


class Access:

    def __init__(self, rootFile = RootFile(), serverInfo = '', userInfo = '', appInfo = '', taskId = '', taskName = '', jobId = '', reads = [], branchesAccessed = [], bytesReadDup = 0, bytesReadUniq = 0):
        self._rootFile = rootFile
        self._serverInfo = serverInfo
        self._userInfo = userInfo
        self._appInfo = appInfo
        self._taskId = taskId
        self._taskName = taskName
        self._jobId = jobId
        self._reads = reads
        self._branchesAccessed = branchesAccessed
        self._bytesReadDup = bytesReadDup
        self._bytesReadUniq = bytesReadUniq

    def getRootFile(self):
        return self._rootFile
    
    def setRootFile(self, rootFile):
        self._rootFile = rootFile
    
    


    def __eq__(self, other):
        pass


