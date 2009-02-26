

class Package:
    '''Represents an individual package in a pacman or AUR repository'''
    def __init__(self,name,repo,version,description,size,groups=None):
        '''Constructor for Package class'''
        self.__name = name
        self.__repo = repo
        self.__version = version
        self.__description = description
        self.__size = size
        self.__groups = groups
        self.__installed = self.isInstalled()
    
    def __str__(self):
        '''Returns a String representing the package'''
        toString =  self.getName()+" v."+self.getVersion()
        if(self.isInstalled()):
            toString += " [Installed]"
        return toString
    
    def getName(self):
        '''Return a package name'''
        return self.__name
    
    def getRepository(self):
        '''Return repository containing the package'''
        return self.__repo
    
    def getRepo(self):
        '''Alias of getRepository, for lazy people'''
        return self.getRepository()
    
    def getVersion(self):
        '''Returns software version'''
        return self.__version
    
    def getDescription(self):
        '''Returns a description of the software'''
        return self.__description
    
    def getDesc(self):
        '''Alias of getDescription, for even lazier people'''
        return self.getDescription()
    
    def isInstalled(self):
        '''TODO: Checks if the current package is installed
        Currently, returns only False'''
        return False
    

