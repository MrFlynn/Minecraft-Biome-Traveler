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
    start_path = home_dir


class Window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER, *args, **kwargs)

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
        eb_panel = wx.Panel(main_panel, -1, pos=(0,100))
        self.explored_biomes_panel = wx.ListBox(eb_panel, -1, size=(150,250), pos=(0,20))
        wx.StaticText(eb_panel, id=-1, label="Discovered Biomes", style=wx.ALIGN_CENTER)

        # Listbox for unexplored biomes.
        ueb_panel = wx.Panel(main_panel, -1, pos=(0,200))
        self.unexplored_biomes_panel = wx.ListBox(ueb_panel, -1, size=(150,250), pos=(0,20))
        wx.StaticText(ueb_panel, id=-1, label="Undiscovered Biomes", style=wx.ALIGN_CENTER)

        # Set sizing for panels.
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(eb_panel, 0, wx.EXPAND | wx.ALL, border=10)
        sizer.Add(ueb_panel, 0, wx.EXPAND | wx.ALL, border=10)
        main_panel.SetSizer(sizer)

        # Set Window size, name, icon, and show the window.
        self.SetIcon(wx.Icon(sys.executable, wx.BITMAP_TYPE_ICO))
        self.SetSize((346, 340))
        self.SetTitle('Biome Traveler')
        self.Show(True)

    # Writes biomes to respective lists and clear them on reload.
    def write_to_page(self, input_list):
        # Clear listboxes to prevent duplicates.
        self.explored_biomes_panel.Clear()
        self.unexplored_biomes_panel.Clear()

        # Appends to explored biomes listbox.
        for item in input_list:
            self.explored_biomes_panel.Append(item)

        # Appends to unexplored biomes listbox.
        for item in list(set(biome_list) - set(input_list)):
            self.unexplored_biomes_panel.Append(item)
            
    # Gets stats file, reads contents, and encodes the list.
    def get_stats_file(self, stats_dir):
        # Finds .json file with stats info and gets applicable stats.
        for file in os.listdir(stats_dir):
            if file.endswith(".json"):
                with open(stats_dir + file, "r") as stats:
                    explored_biomes = (json.loads(stats.read()).get("achievement.exploreAllBiomes").get("progress"))
                    encoded = [i.encode('utf-8') for i in explored_biomes]

        self.write_to_page(encoded)

    # Opens 'select directory' dialog and then reads stats file for information.
    def on_open(self, e):
        # Opens 'select folder' dialog and outputs the chosen directory.
        file_dialog = wx.DirDialog(self, message="Choose World", defaultPath=start_path)
        if file_dialog.ShowModal() == wx.ID_OK:
            if os_ == 'win32':
                self.get_stats_file(file_dialog.GetPath() + "\stats\\")
            elif os_ == 'linux2' or os_ == 'darwin':
               self.get_stats_file(file_dialog.GetPath() + "/stats/")
            else:
                self.get_stats_file(file_dialog.GetPath())
        file_dialog.Destroy()

    # Quits program.
    def on_quit(self, e):
        self.Close()

# Run the application:
if __name__ == '__main__':
    app = wx.App()
    Window(None, title='Size')
    app.MainLoop()
