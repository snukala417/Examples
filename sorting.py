
def sort1(l):
  l1 = len(l)
  i = 0
  while i < (len(l)-1):
    j = i+1
    while j < len(l):
      if l[i] < l [j]:
         l[i],l[j] = l[j],l[i]
      j = j+1
    i = i+1
  print l

c = [12,10,15,13,18, 20, 19, 38, 27, 56, 48, 34, 18, 20 ,18]
sort1(c)