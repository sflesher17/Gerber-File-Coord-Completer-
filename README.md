# Gerber-File-Coord-Completer-
Completes the X/Y coordinate pairs for a Gerber file.

In electrical engineering, a gerber file (file type .NCD) is used to tell a circuit etching machine how to move in order to etch as circuit design into a board. The standard gerber file reader allows only one X or Y coordinate to be given if the other coordinate stays the same. For example: 
if the cordinates go from X+10000Y-3000 to X+10000Y-31000 the second pair of coordinates can be listed as Y-31000 because the X coordinate doesn't change. There are some circuit board producers that prefer to have two pairs of coordinates per line, even if the second line isn't given. The Gerber File coord completer takes a gerber text file and produces a new file that contains two pairs of coordinates per line, even if an X or Y coordinate stays the same. 

NOTE: This first version of the gerber correcter is very rudimentary and requires the user to type the file path directly into the program. A more user friendly interface is currently in production. 
