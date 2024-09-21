
import itertools
a = [1,2,3]
b = [4,5,6]
li = list(itertools.chain(a,b))
li2 = list(itertools.chain(a,li))


print(li2)