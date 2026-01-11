from collections import namedtuple

def customJsonDecoder(jsonDict):
    return namedtuple('X', jsonDict.keys())(*jsonDict.values())