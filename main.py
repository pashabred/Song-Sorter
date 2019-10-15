import os
from mutagen.flac import FLAC
from mutagen.easymp4 import EasyMP4 as MP4
from mutagen.mp3 import EasyMP3 as MP3
from mutagen.oggvorbis import OggVorbis
from mutagen.apev2 import APEv2


def getTag(file, tag1, tag2, tag3):
    tag = ''
    if ".flac" in file:
        flacFile = FLAC(file)
        # tag - common one
        tag = flacFile[tag1][0]
    if ".mp3" in file:
        mp3File = MP3(file)
        # tag - common one
        tag = mp3File[tag1][0]
    if ".m4a" in file:
        m4aFile = MP4(file)
        # tag - common one
        tag = m4aFile[tag1][0]
    if ".ape" in file:
        apeFile = APEv2(file)
        # tag - starts with a capital
        tag = apeFile[tag2][0]
    if ".ogg" in file:
        oggFile = OggVorbis(file)
        # tag - CAPS
        tag = oggFile.tags[tag3][0]
    return tag


def initDir():
    os.chdir("/home/pashabred/Music")

    cwd = os.getcwd()

    # print the current directory
    print("Current working directory is:", cwd)

    return cwd


def createArtistFolders(cwd):
    listOfFiles = os.listdir()
    artists = []
    artist = ' '

    for file in listOfFiles:
        artist = getTag(file, "artist", "Artist", "ARTIST")
        if artist not in artists:
            artists.append(artist)
            os.mkdir(artist)
        os.rename(cwd + '/' + file, cwd + '/' + artist + '/' + file)


if __name__ == '__main__':

    cwd = initDir()
    createArtistFolders(cwd)