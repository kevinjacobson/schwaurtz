#!/usr/bin/env python
#      
#   Copyright (c) 2009 Bryan Goldstein, Kevin Jacobson
#   All rights reserved.
#  
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#       * Redistributions of source code must retain the above copyright
#         notice, this list of conditions and the following disclaimer.
#       * Redistributions in binary form must reproduce the above copyright
#         notice, this list of conditions and the following disclaimer in the
#         documentation and/or other materials provided with the distribution.
#       * Neither the name of the Computer Science House at RIT nor the
#         names of its contributors may be used to endorse or promote products
#         derived from this software without specific prior written permission.
#  
#   THIS SOFTWARE IS PROVIDED BY Bryan Goldstein and Kevin Jacobson ''AS IS'' AND ANY
#   EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#   DISCLAIMED. IN NO EVENT SHALL BRYAN GOLDSTEIN and KEVIN JACOBSON BE LIABLE FOR ANY
#   DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

class Package:
    '''Represents an individual package in a pacman or AUR repository'''
    def __init__(self,name,repo,version,description,size,groups=None):
        '''Constructor for Package class'''
        self.__name = name
        self.__repo = repo
        self.__version = version
        self.__repoVersion = self.checkVersion()
        self.__description = description
        self.__size = size
        self.__groups = groups
        self.__installed = self.isInstalled()
    
    def __str__(self):
        '''Returns a String representing the package'''
        toString = self.getName()+" v."+self.getVersion()
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

    def isUpToDate(self):
        '''Checks if current version matches repository version'''
        return (self.__version==self.__repoVersion)
    
    def isInstalled(self):
        '''TODO: Checks if the current package is installed
Currently, returns only False'''
        return False

    def checkVersion(self):
        '''TODO: Check the version of the package in the repository.
For now returns current version'''
        return self.__version

    def getSize(self):
        '''Returns the size of the software'''
        return self.__size

    def getGroups(self):
        '''Returns a list of the groups the software is under'''
        return self.__groups
