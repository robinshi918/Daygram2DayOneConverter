
import re

# December 15 Tuesday 2015 /

s1 = 'December 15 Tuesday 2015 /   December 17 Monday 2015 /  January 15 Wednesday 2016 /'
pattern = r"(January|February|December) [0-3][0-9] (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) 20[0-9][0-9] /"
for match in re.finditer(pattern, s1):
    s = match.start()
    e = match.end()
    print '"%s" at %d:%d' % (s1[s:e], s, e)

