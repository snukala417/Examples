def jumble(lst):
    d = {}
    l = []
    for s in lst:
        s = ''.join(sorted(s))
        if s in d.keys():
            d[s] = d[s] + 1
        else:
            d[s] = 1
        if d[s] == 2:
            l.append(s)
    return l

l1 = ['abc', 'def', '123', '234', '345', '321', '231', '234', 'acb', 'acd', 'cab', 'abd', 'dab', '123']
print jumble(l1)
