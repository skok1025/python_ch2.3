import sys

x = object()
print(type(x))
print(sys.getrefcount(x))

y= x
print(sys.getrefcount(y))

# reference 값 줄이기
# del 은 심볼 테이블에서 이름을 삭제한다.
del x
print(sys.getrefcount(y))
print(globals())

