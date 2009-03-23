
#!/usr/bin/env python
#
#   PacmanData.py
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


import subprocess as sub

def checkPackageStatus():
    p = sub.Popen(["pacman","-Qi"],stdout=sub.PIPE).stdout
    output = []
    package = {}
    for line in p.readlines():
        keyAndObject = line.split(" : ")
        if len(keyAndObject)==2:
            package[keyAndObject[0].strip()] = keyAndObject[1].strip()
        elif line.strip()=="" and package.has_key('Name'):
            if not package.has_key('Repository'):
                package['Repository'] = "local"
                package['Install Reason'] = "Unknown"
            output.append(package)
            package = {}

    return output

def addRemotePackages():
    p = sub.Popen(["pacman","--sync","--info"],stdout=sub.PIPE).stdout
    output = []
    package = {}
    currentKey = None
    for line in p.readlines():
        keyAndObject = line.split(" : ")
        if len(keyAndObject)==2:
            currentKey = keyAndObject[0].strip()
            package[currentKey] = keyAndObject[1].strip()
        elif line.strip()=="" and package.has_key('Name'):
            output.append(package)
            package = {}
        else:
            package[currentKey] += " "+keyAndObject[0].strip()
    return output
    
def getPackageList():
    #dict = addRemotePackages(getInstalledPackageList())
    #list = []
    #for k in dict.keys():
    #    list.append(dict[k])
    packages = addRemotePackages()
    data = [ (x['Name'], x) for x in packages ] # decorate
    data.sort()
    packages = [ x[1] for x in data ] # undecorate
    return packages

def getValueSet(packageList,key):
    set = []
    for p in packageList:
        if not p[key] in set:
            set.append(p[key])
    return set
