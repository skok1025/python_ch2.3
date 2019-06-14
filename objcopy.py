# 레퍼런스 복사
import copy

a = 1
b = a


a = [1,2,3]
b = [4,5,6]
x = [a,b,100]
y = x

print(x)
print(y)
print(x is y)

# swallow copy (얕은 복사)
a = [1,2,3]
b = [4,5,6]
x = [a,b,100]
y = copy.copy(x)

print(x)
print(y)
print(x is y)
print(x[0] is y[0])

# deep copy(깊은 복사)
a = [1,2,3]
b = [4,5,6]
x = [a,b,100]
y = copy.deepcopy(x)

print(x)
print(y)
print(x is y)
print(x[0] is y[0])
print(x[0][0] is y[0][0])

# 복합 객체가 한개만 있는 경우엔
# 얕은 복사, 깊은 복사는 차이가 없다.

a=['hello','world']
b = copy.copy(a)
print(a is b)
print(a[0] is b[0])

a=['hello','world']
b = copy.deepcopy(a)
print(a is b)
print(a[0] is b[0])


