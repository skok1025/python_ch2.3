import sys

i1 = 10
i2 = 10
print(hex(id(i1)),hex(id(i2)))

i1 = 11
i2 = 10 + 1
print(hex(id(i1)),hex(id(i2)))

l1 = [1,2,3]
l2 = [1,2,3]

print(hex(id(l1)),hex(id(l2)))

# is (동일 레퍼런스 비교)
print(i1 is i2)
print(l1 is l2)

# ?
t1 = (1,2,3)
t2 = (1,2,3)
print(sys.getrefcount(t1),sys.getrefcount(t2))
print(t1 is t2)

t3 = tuple(range(1,4))
print(sys.getrefcount(t3))












