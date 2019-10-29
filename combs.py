a = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i']}
def c1(num):
    num = str(num)
    l = len(num)
    result = a[num[0]]
    #j = a[num[1]]
    k=1
    #result = []
    while k<l:
        j = a[num[k]]
        result = [(c1+c2) for c1 in result for c2 in j]
        k += 1
    print len(result)
    print result

def c2(num):
    num = str(num)
    result = []
    l = len(num)
    if len(num)== 1:
        return a[num[0]]
    return [(ch1+ch2) for ch1 in a[num[0]] for ch2 in c2(num[1:]) ]

c1(234)


