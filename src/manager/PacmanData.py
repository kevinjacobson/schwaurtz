
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

def checkLocalList(packages):
    p = sub.Popen(["pacman","-Q"],stdout=sub.PIPE).stdout
    output = []
    data = dict([ ((x['Name'],x['Version']), x) for x in packages ]) # decorate
    for line in p.readlines():
        keyAndObject = line.split(" ")
        if len(keyAndObject)==2:
            if (keyAndObject[0].strip(),keyAndObject[1].strip()) in data.keys():
                data[(keyAndObject[0].strip(),keyAndObject[1].strip())]["Status"] = "Installed"
                data[(keyAndObject[0].strip(),keyAndObject[1].strip())]["Installed Version"] = keyAndObject[0].strip()
            else:
                q = sub.Popen(["pacman","-Qi",keyAndObject[0].strip()],stdout=sub.PIPE).stdout
                package = {}
                for qline in q.readlines():
                    kAndO = qline.split(" : ")
                    if len(kAndO)==2:
                        currentKey = kAndO[0].strip()
                        package[currentKey] = kAndO[1].strip()
                    elif qline.strip()=="" and package.has_key('Name'):
                        package["Status"] = "Installed"
                        package['Repository'] = "local"
                        output.append(package)
                    else:
                        package[currentKey] += " "+kAndO[0].strip()
    for x in data.keys():
        output.append(data[x]) # undecorate
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
    packages = checkLocalList(packages)
    data = [ (x['Name'], x) for x in packages ] # decorate
    data.sort()
    packages = [ x[1] for x in data ] # undecorate
    return packages

def getValueSet(packageList,key):
    set = []
    for p in packageList:
        values = p[key].split(" ")
        for value in values:
            value = value.strip()
            if (not value in set) and not value == "":
                set.append(value)
    return set
