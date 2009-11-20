#!/usr/bin/env python
#
#   FilterList.py
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
import  wx.lib.mixins.listctrl  as  listmix

class FilterList(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin):

    def __init__(self, parent, id, style):
        wx.ListCtrl.__init__(self, parent, id, style=style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.InsertColumn(0, "")

    def PopulateList(self, items):
        for item in items:
            self.InsertStringItem(sys.maxint,item,0)

