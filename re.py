import re

s = "snmp-server host 2603:5000:7:2B:142:1:0:220 vrf CPE-MGMT version 3 priv mgmtusr"
t = "jsfnfbdbf 2BF ewhwh whjew"
a = re.search(r'([0-9 A-F]:){7}', s)
if a:
    print "YES"
    print a
    print a.group()

b = re.search(r'[0-9 A-F]*', t)
if b:
    print "YES1"
    print b
    print b.group()
