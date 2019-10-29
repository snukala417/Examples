import os
#print os.listdir('.')
print os.path.abspath('.')

a = [x for x in range(100) if x%2==0 ]
#print a

t = ('1', '2', [1, 2, 3])
#print t[1]
t[2].append(4)
#print t

l = [1, 2, 3, 1, 4]
s = set(l)
#print type(s)
#if isinstance(s,set):
#    print "YES"
t = set([3, 4, 5, 6])
#print s.intersection(t)
#print s.difference(t)
#print s.intersection_update(t)

