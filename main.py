#!python2.7

"""
Biome Traveler - Nick Pleatsikas

Lists the biomes that a user has been to and which one's they have to go to
in order to complete the 'Adventuring Time' achievement in Minecraft.
"""

# Libraries:
import sys
import os
import wx
import json

# Global variables:

# List of biomes:
biome_list = ["Beach", "Birch Forest", "Birch Forest Hills", "Cold Beach",
                "Cold Taiga", "Cold Taiga Hills", "Deep Ocean", "Desert",
                "Desert Hills", "Extreme Hills", "Extreme Hills+", "Forest",
                "ForestHills", "FrozenRiver", "Ice Mountains", "Ice Plains",
                "Jungle", "Jungle Edge", "Jungle Hills", "Mega Taiga",
                "Mega Taiga Hills", "Mesa", "Mesa Plateau", "Mesa Plateau F",
                "Mushroom Island", "MushroomIslandShore", "Ocean", "Plains",
                "River", "Roofed Forest", "Savanna", "Savanna Plateau",
                "Stone Beach", "Swampland", "Taiga", "Taiga Hills"]

# Determine system platform:
os_ = sys.platform

# Get the the home directory of the current user:
home_dir = os.path.expanduser('~')

# Generates proper directory for .minecraft folder based on platform:
if os_ == 'linux2':
    start_path = "%s/.minecraft/saves" % (home_dir, )
elif os_ == 'win32':
    start_path = "%s\AppData\Roaming\.minecraft\saves" % (home_dir, )
elif os_ == 'darwin':
    start_path = ("%s/Library/Application Support/minecraft/saves" % (home_dir,))
else:
    home_dir


class Window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.init_ui()

    # Create startup UI.
    def init_ui(self):

        # Create Menu
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()

        # Open folder containing world statistics.
        omi = wx.MenuItem(file_menu, wx.ID_OPEN, '&Open World Folder\tCtrl+O')
        file_menu.AppendItem(omi)
        self.Bind(wx.EVT_MENU, self.on_open, omi)
        # Quit menu item with keyboard shortcut (ctrl + w).
        qmi = wx.MenuItem(file_menu, wx.ID_EXIT, '&Quit\tCtrl+W')
        file_menu.AppendItem(qmi)
        self.Bind(wx.EVT_MENU, self.on_quit, qmi)

        # Create menu_bar.
        menu_bar.Append(file_menu, '&File')
        self.SetMenuBar(menu_bar)

        # Create Panels.
        main_panel = wx.Panel(self)

        # Listbox for explored biomes.
        db_panel = wx.Panel(main_panel, -1, pos=(0,100))
        self.explored_biomes = wx.ListBox(db_panel, -1, size=(150,250), pos=(0,20))
        wx.StaticText(db_panel, id=-1, label="Discovered Biomes", style=wx.ALIGN_CENTER)

        # Listbox for unexplored biomes.
        udb_panel = wx.Panel(main_panel, -1, pos=(0,200))
        self.unexplored_biomes = wx.ListBox(udb_panel, -1, size=(150,250), pos=(0,20))
        wx.StaticText(udb_panel, id=-1, label="Undiscovered Biomes", style=wx.ALIGN_CENTER)

        # Set sizing for panels.
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(db_panel,0,wx.EXPAND|wx.ALL,border=10)
        sizer.Add(udb_panel,0,wx.EXPAND|wx.ALL,border=10)
        main_panel.SetSizer(sizer)

        # Set Window size, name, and show the window.
        self.SetSize((375, 350))
        self.SetTitle('Biome Traveler')
        self.Show(True)

    # Writes biomes to respective lists and clear them on reload.
    def write_to_page(self, inlist):
        # Clear listboxes to prevent duplicates.
        self.explored_biomes.Clear()
        self.unexplored_biomes.Clear()

        # Appends to explored biomes listbox.
        for item in inlist:
            self.explored_biomes.Append(item)

        # Appends to unexplored biomes listbox.
        for item in list(set(biome_list) - set(inlist)):
            self.unexplored_biomes.Append(item)

    # Opens 'select directory' dialog and then reads stats file for information.
    def on_open(self, e):
        # Opens 'select folder' dialog and outputs the chosen directory.
        dlg = wx.DirDialog(self, message="Choose the world folder.", defaultPath=start_path)
        if dlg.ShowModal() == wx.ID_OK:
            if os_ == 'win32':
                world_stats_dir = dlg.GetPath() + "\stats\\"
            else: # for linux, darwin, and other.
                world_stats_dir = dlg.GetPath() + "/stats/"
        dlg.Destroy()

        # Finds .json file with stats info. Outputs file name.
        for file in os.listdir(world_stats_dir):
            if file.endswith(".json"):
                stats_file_name = file

        # Opens stats file and extracts list of explored biomes.
        with open(world_stats_dir + stats_file_name, "r") as stats_file:
            explored_biomes = ((json.loads(stats_file.read()))
                                .get("achievement.exploreAllBiomes")
                                .get("progress"))
            encoded = [i.encode('utf-8') for i in explored_biomes]
        self.write_to_page(encoded)

    # Quits program.
    def on_quit(self, e):
        self.Close()

# Run the application:
if __name__ == '__main__':
    app = wx.App()
    Window(None, title='Size')
    app.MainLoop()
