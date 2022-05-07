# Helper class that abstracts away the file IO
# for communicating between talon and the web server.

import json;
import tempfile;
import os;

# API

# JSONObject GetExtensionJSONNode(string nodeName)
def GetExtensionJSONNode(nodeName: str):
    fullJSONPayload = GetFullFileJSON()

    if nodeName in fullJSONPayload:
        return fullJSONPayload[nodeName]
    
    return {}

# void SetExtensionJSONNode(string nodeName, JSONObject jsonPayload)
def SetExtensionJSONNode(nodeName: str, jsonPayload):
    fileJSON = GetFullFileJSON()
    fileJSON[nodeName] = jsonPayload
    WriteJSONToFile(fileJSON)

# "Private" helpers

# This path needs to match the path specified in TalonWebServer.py in the TalonWebServer repo
# This file is a hack around inter app communication or getting talon.exe to host the web server.
def GetExtensionJSONFilePath():
    return os.path.join(tempfile.gettempdir(), 'TalonExtensionCommunication.json')

def GetFullFileJSON():
    jsonPayload = {}
    jsonFilePath = GetExtensionJSONFilePath()

    if os.path.isdir(os.path.dirname(jsonFilePath)):
        if not os.path.exists(jsonFilePath):
            try:
                print('Web extension communication file does not exist, trying to create it.')
                file = open(jsonFilePath, 'a+')
                file.close()
                print('Created web extension communication file')
            except:
                print('Failed to create web extension communication file')
        else: # The file does exist
            try:
                filePayload = ''
                with open(jsonFilePath, 'r') as jsonFile:
                    filePayload = jsonFile.read()

                if (filePayload):
                    jsonPayload = json.loads(filePayload)
            except:
                print('Failed to read web extension communication file')
    else:
        print('The temp directory doesnt exist, cant access communication file')

    # Return a valid JSON object if we failed to get the file payload
    return jsonPayload

def WriteJSONToFile(jsonPayload):
    try:
        with open(GetExtensionJSONFilePath(), 'w') as jsonFile:
            jsonFile.write(json.dumps(jsonPayload))
    except:
        print('Failed to write the given JSON to the web extension communication file')
