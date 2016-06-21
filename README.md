# Biome Traveler
### Nick Pleatsikas - [pleatsikas.me](http://pleatsikas.me)

#### Description:
This program lists the biomes that a Minecraft player has traveled to and what
biomes they have not. It is intended to help those with the "Adventuring Time"
achievement.

#### Download:
To download the program, please refer to the [releases page.](https://github.com/MrFlynn/Minecraft-Biome-Traveler/releases)
From here, you can either download the source or an EXE for Windows 7 and above.

#### Dependencies:
If you wish to use Python script instead of the EXE, these are the dependencies:
- [Python 2.7](https://www.python.org/downloads/release/python-2711/)
- [PythonWX](http://www.wxpython.org/)
- Python JSON Module (included with Python)
- Python OS Module (included with Python)

In order to ensure that you have all the correct packages installed, run:
```bash
$ sudo apt-get install python-wxgtk2.8
```

#### How to use:
If you have the EXE, just double click the executable. No administrator
permissions needed. To run the Python script, navigate to the folder where the
script is, and run this command:

```bash
$ python main.py
```

If there are any errors, make sure you have all the dependencies installed.

From here, it should open a GUI with two empty lists. To load the biomes
traveled to and ones that have yet to be found select "File" -> "Open World Folder."
(1) This will open a window with all of your Minecraft saves. Select the one you
wish to see stats on and then click "Open" or "Open Folder." You should see a
list of biomes you have explored and which ones you need to explore in order
to complete the Adventuring Time achievement.

**NOTE**: This program doesn't auto-reload the biome lists. The above process
from (1) has to be redone in order to reload the biome lists.

![Biome Traveler Window](http://i.imgur.com/loDSS1R.png)

#### Compatibility:
The program has only been tested with Minecraft version 1.8.9 and snapshot
16w02a. However, it should work with all snapshots and versions between 1.8.9
and snapshot 16w02a. It is unknown whether or not it will work with other
versions.

The compiled EXE should work with Windows 7+, however it has only been tested
with Windows 10 Build 10586.

The Linux executable should work on most distributions (Debian, RHEL, SLES,
SUSE, etc. based). It has only been tested in Ubuntu 15.10.

#### License:
This program is under the MIT license. More details are in the LICENSE file.
