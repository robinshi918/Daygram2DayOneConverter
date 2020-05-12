import re
import json
import uuid
import time
from datetime import datetime
from time import mktime

def createUuid():
    return uuid.uuid4().hex.upper()

json_obj = {
    "metadata" : {
        "version" : "1.0"
    },
    "entries" : []
}

def createEntry(dt, body):
    result = {
        "creationOSVersion" : "10.15.4",
        # "uuid" : "5D7B30EFF33641198E8A5C7F331A7668",
        "timeZone" : "Pacific\/Auckland",
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
    result["creationDevice"] = getDatetime(tag)
    result["modifiedDate"] = getDatetime(tag)
    result['text'] = getBody(body)
    return result

def getDatetime(dt):
    # input: December 15 Tuesday 2015 /
    # 2020-05-03T00:00:00Z
    time_obj = time.strptime(dt, '%B %d %A %Y /')
    dt_obj = datetime.fromtimestamp(mktime(time_obj))
    dt_obj = dt_obj.replace(hour = 15)   # arbitrarily set the hour to 3pm
    return dt_obj.strftime('%Y-%m-%dT%H:%M:%SZ')

def getBody(text):
    result = text #.replace("\n", '\\n')
    return result

pattern = r"(January|February|March|April|May|June|July|August|September|October|November|December|) [0-3][0-9] (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) 20[0-9][0-9] /"
tag_start = 0
tag_end = 0
body_start = 0
body = ""

with open('data2.txt', 'r') as myfile:
    data = myfile.read()

for match in re.finditer(pattern, data):
    tag_start = match.start()
    tag_end = match.end()
    value_watch = data[tag_start:tag_end]
    # print '"%s" at %d:%d' % (data[s:e], tag_start, tag_end)

    if tag_start != 0:
        body_end = tag_start
        body = data[body_start:body_end]
        # print(getDatetime(tag))
        # print("body:\n" + body)
        # print(getBody(body))
        entry = createEntry(tag, body)
        json_obj['entries'].append(entry)

    body_start = tag_end + 1
    tag = data[tag_start:tag_end]

# the last match
if tag_start != 0:
    # print("last match content")
    # print(getDatetime(tag))
    # print("body:\n" + data[tag_end+1:])
    # print(getBody(data[tag_end+1:]))
    entry = createEntry(tag, data[tag_end+1:])
    json_obj['entries'].append(entry)


print json.dumps(json_obj, ensure_ascii=False)