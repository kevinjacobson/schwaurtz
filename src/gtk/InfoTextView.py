#!/usr/bin/env python
#
#   InfoTextView.py
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

class InfoTextView(wx.TextCtrl):

    def __init__(self, parent, id, text, style):
        wx.TextCtrl.__init__(self, parent, id, text, style=style)
        
    def SetPkgInfo(self,package):
        self.Remove(0,-1)
        self.WriteText(" "+package['Name']+" ("+package['Version']+")")
        f = self.GetFont()
        f.SetWeight(wx.BOLD)
        self.SetStyle(0, -1, wx.TextAttr(wx.NullColour, wx.NullColour, f))
        self.WriteText("\n\n ")
        if package.has_key('Description'):
            self.WriteText(package['Description'])
        else:
            self.WriteText("no description")
        self.WriteText("\n\n ")
        start = len(self.GetValue())
        if package.has_key('Install Reason'):
            self.WriteText("Status: Installed\n ")
        else:
            self.WriteText("Status: Not installed\n ")
        self.SetStyle(start, start+7, wx.TextAttr(wx.NullColour, wx.NullColour, f))
        start = len(self.GetValue())
        self.WriteText("Version in the Repository: ")
        self.SetStyle(start, -1, wx.TextAttr(wx.NullColour, wx.NullColour, f))
        if package.has_key('Update'):
            self.WriteText(package['Update']['Version'])
        else:
            self.WriteText(package['Version'])
