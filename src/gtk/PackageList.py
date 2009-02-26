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

class PackageList(wx.ListCtrl):

	def __init__(self, parent, id, style):
		wx.ListCtrl.__init__(self, parent, id, style=style)
		self.InsertColumn(0, "", width=20)
		self.InsertColumn(1, "Package Name", width=210)
		self.InsertColumn(2, "Version", width=wx.LIST_AUTOSIZE)
		self.InsertColumn(3, "Size", width=wx.LIST_AUTOSIZE)
		self.InsertColumn(4, "Repository", width=wx.LIST_AUTOSIZE)
		self.InsertColumn(5, "Groups", width=wx.LIST_AUTOSIZE)
		self.Bind(wx.EVT_LEFT_DCLICK, self.on_dbl_click)
		self.queue = []
		package1 = manager.Package("3ddesktop","extra","0.2.9-2","a 3d virtual desktop switcher (opengl/mesa)","66 KiB")
		package2 = manager.Package("6tunnel","community","0.11rc2-3","Tunnels IPv6 connections for IPv4-only applications","114 KiB")
		package3 = manager.Package("9base","community","2-3","Port of various original Plan9 tools to unix","5.69 MiB")
		package4 = manager.Package("a2ps","extra","4.13c1","a2ps is an Any to PostScript filter","690 KiB")
		package5 = manager.Package("a52dec","extra","0.7.4-4","liba52 is a free library for decoding ATSC A/52 streams.","60 KiB")
		package6 = manager.Package("libcompizconfig","community","0.7.8-2","Compiz configuration system library","114 KiB")
		self.set_packages([package1,package2,package3,package4,package5,package6])
		
	def OnGetItemText(self, item, col):
		package = self.packages[item]
		if col == 0 and package.isInstalled():
			return "X"
		elif col == 0 and not package.isInstalled():
			return "O"
		elif col == 1:
			return package.getName()
		elif col == 2:
			return package.getRepo()
		elif col == 3:
			return "%d KiB" % (item*100)
			#return package.__size
		elif col == 4:
			return package.getVersion()
		elif col == 5:
			return ""
			#return package.__groups

	def set_packages(self, packages):
		self.SetItemCount(len(packages))
		#self.DeleteAllItems()
		self.packages = packages
		#i = 0

		#for package in packages:
		#	if package.isInstalled():
		#		self.InsertStringItem(0,"X")
		#	else:
		#		self.InsertStringItem(0,"O")
		#	self.SetStringItem(0,1,package.getName())
		#	self.SetStringItem(0,2,package.getRepo())
		#	#self.SetStringItem(0,3,package.getSize())
		#	self.SetStringItem(0,4,package.getVersion())
		#	#self.SetStringItem(0,5,package.getGroups())

		#	i = i + 1

			
	def on_click(self, event):
		self.currentItem = event.m_itemIndex

	def on_dbl_click(self, event):
		print "double click"
		#if self.[self.currentItem]:
		#	self.SetStringItem(self.currentItem,0,"X")
		#else:
		#	self.SetStringItem(self.currentItem,0,"O")
