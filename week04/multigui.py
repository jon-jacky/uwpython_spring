#!/usr/bin/env python

# Copyright 2006, 2008 Jonathan Jacky
# 
# This file works with GNU Radio, available from http://gnuradio.org/trac
#
# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
# 
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

'''A simple wx gui for GNU Radio applications, that supports multiple frames'''

import wx
import sys
from gnuradio import gr



class multiapp (wx.App):
    def __init__ (self, flow_graph_maker, title="GNU Radio", nstatus=2,
                  titles=None,  # titles for other panels
                  ulc_x = 20, dx = 20, ulc_y = 30, dy = 200): # frame positions
        self.flow_graph_maker = flow_graph_maker
        self.title = title
        self._nstatus = nstatus
        self.titles = titles
        self.ulc_x = 20; self.dx = 20; self.ulc_y = 30; self.dy = 200
        # All our initialization must come before calling wx.App.__init__.
        # OnInit is called from somewhere in the guts of __init__.
        wx.App.__init__ (self, redirect=False)

    def OnInit (self):
        titles = [ self.title ]
        if self.titles: titles += self.titles
        frames = [ multiframe(titles[i], self._nstatus, # creates panels too
                              pos=(self.ulc_x+i*self.dx,self.ulc_y+i*self.dy))
                   for i in range(len(titles)) ] # use i to calc frame pos
        panel_info = [ (f.title, f.panel, f.panel.vbox) for f in frames ] 
        fg_frame = frames[0]
        fg_frame.frames = frames # so we can delete them all later
        for f in frames:
            if f != fg_frame: f.controller = fg_frame
        if self.titles:
            fg_frame.panel.fg = self.flow_graph_maker(fg_frame, fg_frame.panel,
                                                      fg_frame.panel.vbox,
                                                      sys.argv, panel_info)
        else: # backward compatible, must omit panel_info argument
            fg_frame.panel.fg = self.flow_graph_maker(fg_frame, fg_frame.panel,
                                                      fg_frame.panel.vbox,
                                                      sys.argv)
        for i in range(1,len(frames)+1): # index backwards to stack frames
            frames[-i].panel.Layout();frames[-i].Layout();frames[-i].Show(True)
        self.SetTopWindow (fg_frame) # this doesn't seem to work
        fg_frame.panel.fg.start()
        return True

class multiframe (wx.Frame):
    def __init__ (self, title="GNU Radio", nstatus=2, pos=(0,0)):
        # print "multiframe.__init__"
        wx.Frame.__init__(self, None, -1, title, pos)
        self.title = title
        self.frames = None     # list of controlled frames, if any
        self.controller = None # controller frame, if any 
        self.CreateStatusBar (nstatus)
        mainmenu = wx.MenuBar ()
        menu = wx.Menu ()
        item = menu.Append (200, 'E&xit', 'Exit')
        self.Bind (wx.EVT_MENU, self.OnCloseWindow, item)
        mainmenu.Append (menu, "&File")
        self.SetMenuBar (mainmenu)
        self.Bind (wx.EVT_CLOSE, self.OnCloseWindow)
        self.panel = multipanel(self, self)
        
    def Layout(self):
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(self.vbox)
        self.SetAutoLayout(True)
        self.vbox.Fit(self)

    def OnCloseWindow (self, event):
        if self.panel.fg: self.panel.fg.stop()
        if self.controller:
            self.controller.frames = [ f for f in self.controller.frames
                                       if f != self ]
        if self.frames:
            for f in self.frames:
                if f != self: f.OnCloseWindow(event)
        self.Destroy ()
    
class multipanel (wx.Panel):
    def __init__ (self, parent, frame):
        # print "multipanel.__init__"
        wx.Panel.__init__ (self, parent, -1)
        self.frame = frame
        self.vbox = wx.BoxSizer (wx.VERTICAL)
        self.fg = None # flow graph, if any
        
    def Layout(self):
        self.SetSizer (self.vbox)
        self.SetAutoLayout (True)
        self.vbox.Fit (self)

# No gui_flow_graph here, use the one in stdgui
