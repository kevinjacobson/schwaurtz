#!/usr/bin/python

__author__="bryan"
__date__ ="$Mar 20, 2009 9:09:29 PM$"

import sys
sys.path.append("../")
from manager import PacmanData
try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)

class Interface:
    """The interface for the Schwaurtz"""

    def packageDblClick(self, treeview, iter, tvc):
        model=treeview.get_model()
        iter = model.get_iter(iter)
        print model.get_value(iter, 1)

    def packageSelected(self, treeview):
        #Get package information
        selection = treeview.get_selection().get_selected()
        model = selection[0]
        iter = selection[1]
        name = model.get_value(iter, 1)
        repo = model.get_value(iter, 4)
        package = None
        for p in self.packages:
            if p['Name']==name and p['Repository']==repo:
                package = p
                break;
        #Set the description to the current package
        description = package['Name']+" ("+package['Version']+")\n\n"
        if package.has_key('Description'):
            description += package['Description']
        else:
            description += "no description"
        description += "\n\n"
        if package.has_key('Status'):
            description += "Status: Installed\n"
        else:
            description += "Status: Not installed\n"
        description += "Version in the Repository: "
        if package.has_key('Update'):
            description += package['Update']['Version']
        else:
            description += package['Version']

        textBuffer = self.descriptionView.get_buffer()
        tag = textBuffer.create_tag(scale=1.2)
        textBuffer.set_text(description)
        textBuffer.apply_tag(tag,textBuffer.get_start_iter(),textBuffer.get_end_iter())

    def populateFilterLists(self):
        repos = PacmanData.getValueSet(self.packages,"Repository")
        repos.insert(0,"all")
        for repo in repos:
            self.repoFilterList.append([repo])
        groups = PacmanData.getValueSet(self.packages,"Groups")
        groups.insert(0,"all")
        for group in groups:
            self.groupFilterList.append([group])
        status = ["All","Installed","Not Installed","Upgradable","In Queue"]
        for state in status:
            self.statusFilterList.append([state])
        
    def addPackages(self):
        self.packages = PacmanData.getPackageList()
        for package in self.packages:
            if package.has_key('Name') and package.has_key('Version') and package.has_key('Repository') and package.has_key('Groups'):
                info = []
                if package.has_key('Update'):
                    info.append("U")
                elif package.has_key('Status'):
                    info.append("X")
                else:
                    info.append("O")
                info.append(package['Name'])
                info.append(package['Version'])
                if package.has_key('Installed Size'):
                    info.append(package['Installed Size'])
                elif package.has_key('Download Size'):
                    info.append(package['Download Size'])
                else:
                    info.append(None)
                info.append(package['Repository'])
                info.append(package['Groups'])
                self.packageList.append(info)

    def addPackageListColumn(self, title, columnId):
        """Add columns to the package list"""
        column = gtk.TreeViewColumn(title, gtk.CellRendererText()
            , text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.packageView.append_column(column)
        
    def __init__(self):

		#Set Glade file
        self.gladefile = "main.glade"
        self.wTree = gtk.glade.XML(self.gladefile)

        #Get the Main Window, and connect the "destroy" event
        self.window = self.wTree.get_widget("mainwindow")
        if (self.window):
            self.window.connect("destroy", gtk.main_quit)

        #Create dictionay and connect it
        dic = { "on_packagelist_row_activated" : self.packageDblClick
        , "on_packagelist_cursor_changed" : self.packageSelected}
        self.wTree.signal_autoconnect(dic)


        #Column Identities
        self.cStatus = 0
        self.cName = 1
        self.cVersion = 2
        self.cSize = 3
        self.cRepo = 4
        self.cGroups = 5
        
        self.sStatus = " "
        self.sName = "Package"
        self.sVersion = "Version"
        self.sSize = "Size"
        self.sRepo = "Repository"
        self.sGroups = "Groups"

		#Get the treeView from the widget Tree
        self.packageView = self.wTree.get_widget("packagelist")
		#Add all of the List Columns to the packageList
        self.addPackageListColumn(self.sStatus, self.cStatus)
        self.addPackageListColumn(self.sName, self.cName)
        self.addPackageListColumn(self.sVersion, self.cVersion)
        self.addPackageListColumn(self.sSize, self.cSize)
        self.addPackageListColumn(self.sRepo, self.cRepo)
        self.addPackageListColumn(self.sGroups, self.cGroups)

		#Create the listStore Model to use with the packageList
        self.packageList = gtk.ListStore(str, str, str, str, str, str)

        #Populate the package list
        self.addPackages()

		#Attach the model to the treeView
        self.packageView.set_model(self.packageList)

         #Create the description text  view
        self.descriptionView = self.wTree.get_widget("descriptionview")

        #Create the filter lists
        self.repoFilterView = self.wTree.get_widget("repolist")
        self.groupFilterView = self.wTree.get_widget("grouplist")
        self.statusFilterView = self.wTree.get_widget("statuslist")
        column = gtk.TreeViewColumn("", gtk.CellRendererText(), text=0)
        self.repoFilterView.append_column(column)
        column = gtk.TreeViewColumn("", gtk.CellRendererText(), text=0)
        self.groupFilterView.append_column(column)
        column = gtk.TreeViewColumn("", gtk.CellRendererText(), text=0)
        self.statusFilterView.append_column(column)
        self.repoFilterList = gtk.ListStore(str)
        self.groupFilterList = gtk.ListStore(str)
        self.statusFilterList = gtk.ListStore(str)
        self.populateFilterLists()
        self.repoFilterView.set_model(self.repoFilterList)
        self.groupFilterView.set_model(self.groupFilterList)
        self.statusFilterView.set_model(self.statusFilterList)

        #Show the main window
        self.wTree.get_widget("mainwindow").show()

if __name__ == "__main__":
    interface = Interface()
    gtk.main()