#!python2.7

"""
Biome Traveler - Nick Pleatsikas

Lists the biomes that a user has been to and which one's they have to go to
in order to complete the 'Adventure Time' achievement in Minecraft.
"""

# Libraries:
import wx
import os
import json

# Global variables:
biome_list = ["Beach", "Birch Forest", "Birch Forest Hills", "Cold Beach", "Cold Taiga", "Cold Taiga Hills",
              "Deep Ocean", "Desert", "Desert Hills", "Extreme Hills", "Extreme Hills+", "Forest", "ForestHills",
              "FrozenRiver", "Ice Mountains", "Ice Plains", "Jungle", "Jungle Edge", "Jungle Hills", "Mega Taiga",
              "Mega Taiga Hills", "Mesa", "Mesa Plateau", "Mesa Plateau F", "Mushroom Island", "MushroomIslandShore",
              "Ocean", "Plains", "River", "Roofed Forest", "Savanna", "Savanna Plateau", "Stone Beach",
              "Swampland", "Taiga", "Taiga Hills"]

class Window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        # Initialize UI.
        self.InitUI()

    # Create startup UI.
    def InitUI(self):

        # Create Menu
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        # - Open folder containing world statistics.
        omi = wx.MenuItem(fileMenu, wx.ID_OPEN, '&Open World Folder\tCtrl+O')
        fileMenu.AppendItem(omi)
        self.Bind(wx.EVT_MENU, self.OnOpen, omi)
        # - Quit menu item with keybord shortcut (ctrl + w).
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        # Create menubar.
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        # Create Panels.
        MainPanel = wx.Panel(self)

        # Listbox for explored biomes.
        panel1 = wx.Panel(MainPanel, -1, pos=(0,100))
        self.explored_biomes = wx.ListBox(panel1, -1, size=(150,250), pos=(0,20))
        wx.StaticText(panel1, id=-1, label="Discovered Biomes",style=wx.ALIGN_CENTER, name="")
        # Listbox for unexplored biomes.
        panel2 = wx.Panel(MainPanel, -1,pos=(0,200))
        self.unexplored_biomes = wx.ListBox(panel2, -1, size=(150,250), pos=(0,20))
        wx.StaticText(panel2, id=-1, label="Undiscovered Biomes",style=wx.ALIGN_CENTER, name="")

        # Set sizing for panels.
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(panel1,0,wx.EXPAND|wx.ALL,border=10)
        sizer.Add(panel2,0,wx.EXPAND|wx.ALL,border=10)
        MainPanel.SetSizer(sizer)

        # Set Window size, name, and show the window.
        self.SetSize((375, 350))
        self.SetTitle('Biome Traveler')
        self.Show(True)

    def WriteToPage(self, inlist):
        # Clear listboxes to prevent duplicates.
        self.explored_biomes.Clear()
        self.unexplored_biomes.Clear()

        # Appends to explored biomes listbox.
        for item in inlist:
            self.explored_biomes.Append(item)

        # Appends to unexplored biomes listbox.
        for item in list(set(biome_list) - set(inlist)):
            self.unexplored_biomes.Append(item)

    # Open file.
    def OnOpen(self, e):
        # Opens 'select folder' dialog and outputs the chosen directory.
        dlg = wx.DirDialog(self, "Choose the world folder.")
        if dlg.ShowModal() == wx.ID_OK:
            world_stats_dir = dlg.GetPath() + "\stats\\"
        dlg.Destroy()

        # Finds .json file with stats info. Outputs file name.
        for file in os.listdir(world_stats_dir):
            if file.endswith(".json"):
                stats_file_name = file

        # Opens stats file and extracts list of explored biomes.
        stats_file = open(world_stats_dir + stats_file_name, "r")
        explored_biomes = (json.loads(stats_file.read())).get("achievement.exploreAllBiomes").get("progress")
        encoded = [i.encode('utf-8') for i in explored_biomes]
        self.WriteToPage(encoded)

    # Quit command.
    def OnQuit(self, e):
        self.Close()

# Run the application:
if __name__ == '__main__':
    app = wx.App()
    Window(None, title='Size')
    app.MainLoop()
