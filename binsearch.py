def binsearch(list1, item):
    i=0
    j=len(list1)-1
    f=False
    while i<=j and not f:
        m = (i+j)/2
        if list1[m] == item:
            f = True
            print m
        else:
            if item>list1[m]:
                i = m+1
                #print i
            else:
                j = m-1
                #print j
    return f

l = [1, 2, 4, 5, 18, 29, 47, 104, 189, 234, 245, 276, 333, 376, 487, 512, 636]
print binsearch(l,512)
