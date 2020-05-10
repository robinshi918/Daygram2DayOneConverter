
import re

# December 15 Tuesday 2015 /
month = ['January', 'February', 'March', 'April',
'May', 'June', 'July' ,'August', 'September', 'October', 'November' ,'December']
week_day = ['Monday', 'Tuesday', 'Wednesday', "Thursday", "Friday", 'Saturday', "Sunday"]
print(month)
print(week_day)


s1 = 'December 15 Tuesday 2015 /'
pattern = '[January|February|December]'
for match in re.finditer(pattern, s1):
    s = match.start()
    e = match.end()
    print 'String match "%s" at %d:%d' % (s1[s:e], s, e)

