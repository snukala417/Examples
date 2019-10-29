
import re
import sys

try:
    f = open("1.cfg", "r")
    raise ValueError
except IOError as e:
    print e
    sys.exit()
    #print "Error while opening file"
finally:
    print "FINALLY"

print "SRINI"




