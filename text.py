# open a file stream to the location of the gerber file
readFile = open("FILE PATH TO GERBER FILE", "r")

# open a file stream to the location of the write file
writeFile = open("FILE PATH PATH TO THE NEW GERBER FILE", "w")

prevY = list()    # hold the previous y-position
prevX = list()    # hold the previous x-position
command = list()  # hold the entire command

for lines in readFile.readlines():
    # if the command isn't X or Y coords, export it to the new file
    if lines[0] != 'Y' and lines[0] != 'X':
        writeFile.write(lines)
    # find the output of the data if it's the first command
    elif len(prevY) == 0:
        prevX = lines[lines.find('X'):lines.find('Y')]
        prevY = lines[lines.find('Y'):]
        writeFile.write(prevX+prevY)
    # print the data if both the X and Y coords are given
    elif lines.find('X') != -1 and lines.find('Y') != -1:
        prevX = lines[lines.find('X'):lines.find('Y')]
        prevY = lines[lines.find('Y'):]
        writeFile.write(prevX+prevY)
    # print the coords if only the Y is given
    elif lines.find('X') == -1:
        prevY = lines[lines.find('Y'):]
        writeFile.write(prevX+prevY)
    # print the coords if only the X is given
    elif lines.find('Y') == -1:
        prevX = lines[lines.find('X'): len(lines)-1]
        writeFile.write(prevX+prevY)

# close the file stream
readFile.close()
writeFile.close()
