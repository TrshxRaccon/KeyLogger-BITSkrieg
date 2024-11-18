# KeyLogger-BITSkrieg

Pynput and Pyperclip were found from a google search and Pynput usage was learnt from a youtube video. Special permissions had to be given to the program to run in the background on MacOS otherwise the SysLogs.txt would save "This process is not trusted! Input event monitoring will not be possible until it is added to accessibility clients."
When the program is allowed to monitor input and record the screen including private windows, it was able to capture screenshots no matter the window open and record keystrokes globally.
After the program was ready, it was obfuscated using Pyobfuscator and then PyInstaller was used to convert the obfuscated source code into a .exe file. The .exe is 314.3MB so I can't upload it on github but I will include attatchments showing the .exe file running.
