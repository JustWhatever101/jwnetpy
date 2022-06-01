from asyncio.windows_events import NULL
from gettext import NullTranslations


readLock = "aDSeSDKK992"


def fsr(filename):
    openFile = open(filename, "r")
    return openFile


def getFileContents(fsr):
    return fsr.read()


def getFileLine(fsr):
    return fsr.readline()