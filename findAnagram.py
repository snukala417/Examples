def findAnagram(A):
    strdict = {}
    output = []
    for str in A:
        sortedStr = ''.join(sorted(str))
        if sortedStr not in strdict.keys():
            strdict[sortedStr] = [str]
        else:
            if len(strdict[sortedStr]) == 1:
                output.append(strdict[sortedStr][0])
            strdict[sortedStr].append(str)
    return output


A = ['cba', 'isa', 'aab', 'abcd', 'cab', 'asi', 'asic']
result = findAnagram(A)
print(result)


def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]


print rreverse('jfjsjfhwuei')


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print fib(10)

my_set = {1, 2, 3}
print(my_set)