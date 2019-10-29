import json

d = {"a":1, "b":2}

j = json.dumps(d)
k=json.loads(j)
print k
print type(k)
print k["a"]
print j
print type(j)