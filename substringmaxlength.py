def fun(s):
    sub = ''
    i = 0
    l = 0
    max_len = 0
    cur_len = 0
    while i < len(s):
        if s[i] not in sub:
            sub = sub + s[i]
            print 'SUB', sub
            cur_len = len(sub)
            print cur_len
        else:
            ind = sub.index(s[i])
            # print "IND", ind
            sub = sub[(ind + 1):] + s[i]
            print "SUB!", sub
        if cur_len > max_len:
            max_len = cur_len
            cur_len = len(sub)
        i += 1
    return max_len


print fun("ABDEAFGABEFGHIJKLA1234567890A")
