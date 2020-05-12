#!/usr/bin/python

import re
import json
import uuid
import time
from datetime import datetime
from time import mktime
import os
import sys

input_file_name = ""

def show_usage():
    global input_file_name
    arguments = len(sys.argv) - 1
    if arguments < 1:
        print("")
        print("ERROR! Please specify the exported Daygram file.")
        print("python convert.py PATH_TO_DAYGRAM_EXPORT_FILE")
        print("")
        exit(1)
    else:
        input_file_name = sys.argv[1]
        if (not os.path.exists(input_file_name)):
            print("")
            print("ERROR! Specified Daygram file does not exist!")
            print("")
            exit(1)

def createUuid():
    return uuid.uuid4().hex.upper()

def createEntry(dt, body):
    result = {
        "creationOSVersion" : "10.15.4",
        # "uuid" : "5D7B30EFF33641198E8A5C7F331A7668",
        # "timeZone" : "Pacific\/Auckland",
        "timeZone" : "Etc\/GMT",
        # "text" : "This is something happened in history even earlier.",
        "creationDeviceType" : "MacBook Pro",
        "duration" : 0,
        "starred" : False,
        "creationDeviceModel" : "MacBookPro12,1",
        # "creationDate" : "2020-05-03T00:00:00Z",
        # "modifiedDate" : "2020-05-09T21:13:47Z",
        "creationDevice" : "MacBook Pro",
        "editingTime" : 0,
        "creationOSName" : "macOS"
    }
    result["uuid"] = createUuid()
    result["creationDate"] = getDatetime(tag)
    result["modifiedDate"] = getDatetime(tag)
    result['text'] = body
    return result

def getDatetime(dt):
    # input format: December 15 Tuesday 2015 /
    # output intput: 2020-05-03T00:00:00Z
    time_obj = time.strptime(dt, '%B %d %A %Y /')
    dt_obj = datetime.fromtimestamp(mktime(time_obj))
    return dt_obj.strftime('%Y-%m-%dT%H:%M:%SZ')

show_usage()

output_json_obj = {
    "metadata" : {
        "version" : "1.0"
    },
    "entries" : []
}

pattern = r"(January|February|March|April|May|June|July|August|September|October|November|December|) [0-3][0-9] (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) 20[0-9][0-9] /"
tag_start = 0
tag_end = 0
body_start = 0
body = ""

with open(input_file_name, 'r') as myfile:
    data = myfile.read()

for match in re.finditer(pattern, data):
    tag_start = match.start()
    tag_end = match.end()
    value_watch = data[tag_start:tag_end]

    if tag_start != 0:
        body_end = tag_start
        body = data[body_start:body_end]
        entry = createEntry(tag, body)
        output_json_obj['entries'].append(entry)

    body_start = tag_end + 1
    tag = data[tag_start:tag_end]

if tag_start != 0:
    entry = createEntry(tag, data[tag_end+1:])
    output_json_obj['entries'].append(entry)

print json.dumps(output_json_obj, ensure_ascii=False, indent= 4)