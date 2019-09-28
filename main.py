import os
import eyed3

# dir = input()
# os.chdir(dir)

os.chdir("/home/pashabred/Music")

cwd = os.getcwd()

# print the current directory
print("Current working directory is:", cwd)
#
listOfFiles = os.listdir()
a = []

# print(listOfFiles)

try:
    for file in listOfFiles:
        aFile = eyed3.load(file)
        artist = aFile.tag.artist
        if artist not in a:
            a.append(artist)
            os.mkdir(artist)
        os.rename(cwd + '/' + file, cwd + '/' + artist + '/' + file)
except:
    print("not a file")

print(listOfFiles)
print(a)
