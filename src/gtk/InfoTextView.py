#!/usr/bin/env python
#
#       InfoTextView.py
#       
#       Copyright 2009 Bryan Goldstein <bryan@bryan-laptop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.


import wx
import sys
sys.path.append("../")
import manager

class InfoTextView(wx.TextCtrl):

	def __init__(self, parent, id, text, style):
		wx.TextCtrl.__init__(self, parent, id, text, style=style)
		
	def SetPkgInfo(self,package):
		self.Remove(0,-1)
		self.WriteText(" "+package.getName()+" ("+package.getVersion()+")")
		f = self.GetFont()
		f.SetWeight(wx.BOLD)
		self.SetStyle(0, -1, wx.TextAttr(wx.NullColour, wx.NullColour, f))
		self.WriteText("\n\n ")
		self.WriteText(package.getDesc())
		self.WriteText("\n\n ")
		start = len(self.GetValue())
		if package.isInstalled():
			self.WriteText("Status: Installed\n ",wx.BOLD)
		else:
			self.WriteText("Status: Not installed\n ")
		self.SetStyle(start, start+7, wx.TextAttr(wx.NullColour, wx.NullColour, f))
		start = len(self.GetValue())
		self.WriteText("Version in the Repository:")
		self.SetStyle(start, start+26, wx.TextAttr(wx.NullColour, wx.NullColour, f))
