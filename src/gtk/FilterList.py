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

class FilterList(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin):

	def __init__(self, parent, id, style):
		wx.ListCtrl.__init__(self, parent, id, style=style)
		listmix.ListCtrlAutoWidthMixin.__init__(self)
		self.InsertColumn(0, "")

	def PopulateList(self, items):
		for item in items:
			self.InsertStringItem(sys.maxint,item,0)

