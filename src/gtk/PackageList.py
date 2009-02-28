#!/usr/bin/env python
#
#   PackageList.py
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



import wx
import sys
sys.path.append("../")
import manager
import  wx.lib.mixins.listctrl  as  listmix

class PackageList(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin):

    def __init__(self, parent, id, style):
        wx.ListCtrl.__init__(self, parent, id, style=style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.InsertColumn(0, "", width=20)
        self.InsertColumn(1, "Package Name", width=200)
        self.InsertColumn(2, "Version", width=wx.LIST_AUTOSIZE)
        self.InsertColumn(3, "Size", width=wx.LIST_AUTOSIZE)
        self.InsertColumn(4, "Repository", width=wx.LIST_AUTOSIZE)
        self.InsertColumn(5, "Groups", width=wx.LIST_AUTOSIZE)
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnDblClick)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick)
        
    def OnGetItemText(self, item, col):
        package = self.packages[item]
        if col == 0 and package.isInstalled():
            return "X"
        elif col == 0 and not package.isInstalled():
            return "O"
        elif col == 1:
            return package.getName()
        elif col == 2:
            return package.getVersion()
        elif col == 3:
            return package.getSize()
        elif col == 4:
            return package.getRepo()
        elif col == 5:
            return package.getGroups()

    def SetPackages(self, packages):
        self.SetItemCount(len(packages))
        self.packages = packages
        self.filteredPackages = []
        self.sortedColumn = [1,1]
        self.packages.sort(key=manager.Package.getName)

    def OnDblClick(self, event):
        print "double click"
        #if self.[self.currentItem]:
        #   self.SetStringItem(self.currentItem,0,"X")
        #else:
        #   self.SetStringItem(self.currentItem,0,"O")

    def SortColumn(self,col):
        if (col==0):
            self.packages.sort(key=manager.Package.isInstalled)
        elif (col==1):
            self.packages.sort(key=manager.Package.getName)
        elif (col==2):
            self.packages.sort(key=manager.Package.getVersion)
        elif (col==3):
            self.packages.sort(key=manager.Package.getSize)
        elif (col==4):
            self.packages.sort(key=manager.Package.getRepository)
        elif (col==5):
            self.packages.sort(key=manager.Package.getGroups)
        i = 1
        if (col==self.sortedColumn[0] and self.sortedColumn[1]):
            self.packages.reverse()
            i = 0
        self.sortedColumn = [col,i]
        
    def OnColClick(self,event):
        col = event.GetColumn()
        self.SortColumn(col)

    def SetFilter(self, filter):
        for package in self.filteredPackages:
            self.packages.append(package)
        self.filteredPackages = []
        if filter[1]!="all":
            for package in self.packages:
                if filter[0]==4 and package.getRepository()!=filter[1]:
                    self.filteredPackages.append(package)
                elif filter[0]==5 and (package.getGroups()==None or not (filter[1] in package.getGroups())):
                    self.filteredPackages.append(package)
                elif filter[0]==0:
                    if filter[1]=="Installed" and not package.isInstalled():
                        self.filteredPackages.append(package)
                    elif filter[1]=="Upgradable" and package.isUpToDate():
                        self.filteredPackages.append(package)
                    elif filter[1]=="Not Installed" and package.isInstalled():
                        self.filteredPackages.append(package)
        for package in self.filteredPackages:
            self.packages.remove(package)
        self.SetItemCount(len(self.packages))
        self.sortedColumn[1] = abs(self.sortedColumn[1]-1)
        self.SortColumn(self.sortedColumn[0])
