# Biome Traveler
### Nick Pleatsikas - [pleatsikas.me](http://pleatsikas.me)

#### Description:
This program lists the biomes that a Minecraft player has traveled to and what
biomes they have not. It is intended to help those with the "Adventure Time"
achievement.

#### Installation/Download:
To install, please refer to the [releases page.](https://github.com/MrFlynn/Minecraft-Biome-Traveler/releases)
From here, you can either download the source or an EXE for Windows 7+.

#### Dependencies:
If you wish to use Python script instead of the EXE, these are the dependencies:
- [Python 2.7.11](https://www.python.org/downloads/release/python-2711/)
- [PythonWX](http://www.wxpython.org/)
- Python JSON Module (included with Python 2.7.11)
- Python OS Module (included with Python 2.7.11)

#### How to use:
If you have the EXE, just double click the executable. No administrator
permissions needed. To run the Python script, navigate to the folder where the
script is, and run this command:

```bash
python main.py
```

If there are any errors, make sure you have all the dependencies installed.

From here, it should open a GUI with two empty lists. To load the biomes
traveled to and ones that have yet to be found select "File" -> "Open World Folder."
Navigate to the folder that contains the Minecraft save you wish to list biomes
for, select it, and click "Open Folder."

This is a list of where Minecraft Saves are located:
- Windows: %AppData%\\.minecraft\\saves
- OS X: ~/Library/Application Support/minecraft/saves/
- Linux: ~/.minecraft/saves

This should list the biomes that have been explored and those which have not
in their respective lists (image below shows this).

![Biome Traveler Window](http://i.imgur.com/loDSS1R.png)

#### Compatibility:
The program has only been tested with Minecraft version 1.8.9 and snapshot
15w51b. However, it should work with all snapshots and versions between 1.8.9
and snapshot 15w51b. It is unknown whether or not it will work with other
versions.

The compiled EXE should work with Windows 7+, however it has only been tested
with Windows 10 Build 10586.

#### License:
This program is under the MIT license. More details are in the LICENSE file.
