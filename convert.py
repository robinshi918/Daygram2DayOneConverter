import re
import json

def createJson():
    jjj = {
        "key1": {
            "key2": [1,2,3],
            "key3": [4,5,6]
        }
    }
    print(json.dumps(jjj, indent=4))


createJson()

# December 15 Tuesday 2015 /

with open('data2.txt', 'r') as myfile:
    data = myfile.read()

pattern = r"(January|February|March|April|May|June|July|August|September|October|November|December|) [0-3][0-9] (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) 20[0-9][0-9] /"
tag_start = 0
tag_end = 0
body_start = 0
body = ""

for match in re.finditer(pattern, data):
    tag_start = match.start()
    tag_end = match.end()
    value_watch = data[tag_start:tag_end]
    # print '"%s" at %d:%d' % (data[s:e], tag_start, tag_end)

    if tag_start != 0:
        body_end = tag_start
        body = data[body_start:body_end]
        print("tag:" + tag)
        print("body:\n" + body)

    body_start = tag_end + 1
    tag = data[tag_start:tag_end]

# the last match
if tag_start != 0:
    print("last match content")
    print("tag:" + tag)
    print("body:\n" + data[tag_end+1:])



