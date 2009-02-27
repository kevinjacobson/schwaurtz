#!/usr/bin/env python
#
#	   PackageList.py
#	   
#	   Copyright 2009 Bryan Goldstein <bryan@bryan-laptop>
#	   
#	   This program is free software; you can redistribute it and/or modify
#	   it under the terms of the GNU General Public License as published by
#	   the Free Software Foundation; either version 2 of the License, or
#	   (at your option) any later version.
#	   
#	   This program is distributed in the hope that it will be useful,
#	   but WITHOUT ANY WARRANTY; without even the implied warranty of
#	   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	   GNU General Public License for more details.
#	   
#	   You should have received a copy of the GNU General Public License
#	   along with this program; if not, write to the Free Software
#	   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#	   MA 02110-1301, USA.

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
			return "%d KiB" % (item*100)
			#return package.__size
		elif col == 4:
			return package.getRepo()
		elif col == 5:
			return ""
			#return package.__groups

	def SetPackages(self, packages):
		self.SetItemCount(len(packages))
		self.packages = packages
		self.filteredPackages = []
		self.sortedColumn = [1,1]
		self.packages.sort(key=manager.Package.getName)

	def OnDblClick(self, event):
		print "double click"
		#if self.[self.currentItem]:
		#	self.SetStringItem(self.currentItem,0,"X")
		#else:
		#	self.SetStringItem(self.currentItem,0,"O")

	def SortColumn(self,col):
		if (col==0):
			self.packages.sort(key=manager.Package.isInstalled)
		elif (col==1):
			self.packages.sort(key=manager.Package.getName)
		elif (col==2):
			self.packages.sort(key=manager.Package.getVersion)
		elif (col==3):
			self.packages.sort(key=manager.Package.getName)
		elif (col==4):
			self.packages.sort(key=manager.Package.getRepository)
		elif (col==5):
			self.packages.sort(key=manager.Package.getName)
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
		for package in self.filteredPackages:
			self.packages.remove(package)
		self.SetItemCount(len(self.packages))
		self.sortedColumn[1] = abs(self.sortedColumn[1]-1)
		self.SortColumn(self.sortedColumn[0])
