# Biome Traveler
### Nick Pleatsikas - [pleatsikas.me](http://pleatsikas.me)

# THIS PROJECT IS NO LONGER MAINTAINED!
I haven't really had time to work on this project over the past year or so. It still works (save for some weird UI issues on macOS), but things may break in the future.

This program was always a super inelegant solution to the problem of tracking your progress for the "Adventuring Time" achievement, so I was never super satisfied with it (not to mention Python GUI frameworks are pretty awful). A more elegant solution (that is in-game, too!) can be found [here](https://www.reddit.com/r/Minecraft/comments/62l543/i_recreated_the_adventuring_time_achievement/).

## Description:
One of the final achievements in Minecraft is to explore "all" (in reality, you only 
you only have to explore 95% of the biomes in the game). However, Mojang doesn't 
provide a way to track your progress. This applications helps you track your progress 
with that achievement.

## Running the Program:

### Windows:
I have compiled the program for Windows 7, 8, 8.1, and 10. Go to the [releases page](https://github.com/MrFlynn/Minecraft-Biome-Traveler/releases) to download the .exe for Windows.

If you run into an error R6034, you have to download [Visual Studio Redistributable 2008](https://www.microsoft.com/en-us/download/details.aspx?id=29).

### Linux and macOS:
Since I have compiled the application for Windows, the process is a little 
more involved on Linux and macOS.

To run the program, download the source code zip on the releases page. Then 
refer to the dependencies below to install.

#### Linux Dependencies:
To install the proper dependencies, run this command:
```bash
$ sudo apt-get install python python-wxgtk2.8
```

#### macOS Dependencies:
I would recommend installing [homebrew](http://brew.sh/) before continuing.

Once you have homebrew installed, open the terminal and run these commands 
to install the proper dependencies:
```bash
$ brew install python
$ brew install pythonwx
```

#### Run the Application:
Unzip the source, change into the source directory, and run the application with 
the python interpreter.
```bash
$ python main.py
```

## How to Use the Application:
1. When the application opens, click *File* and then *Open World Folder*
2. Using the folder selection dialog select the folder where your save resides.
3. The application should now display the biomes which you have explored and those you have 
not.

Since the application doesn't (yet) have a mechanism for updating as you 
explore, you will have to periodically reopen the world starting at step 
1. as listed above.

## License:
This application is listed under the MIT license. Essentially the program is 
provided as-is and I, as the developer, am under no obligation to support it. However, 
you are free to tinker and modify it as you please. If you redistribute the 
code I would request that you credit me.

