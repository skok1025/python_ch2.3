
def f():
    l_a = 2
    l_b = '마이콜'
    print("f_local: ",locals())
class MyClass:
    x=10
    y=20

print(globals())
g_a = 1
g_b = "둘리"

# print(globals())

f()

# 1. 정의된 함수
f.k = 'hello'

print("--",f.__dict__)


# 2. 클래스 객체
MyClass.z = 10

# print(MyClass.__dict__)

# 내장 함수는 심볼 테이블이 없다 -> 확장 x
# print(print.__class__)

# 내장 클래스는 symbol table 은 있으나 확장금지
# str.z = 10
# print(str.__dict__)

# 내장클래스로 생성된 객체
# 심벌테이블 x -> 확장 x
# g_a.z = 10
# print(g_a.__dict__)

# 사용자 정의된 클래스로 생성된 객체
# 심볼 테이블 -> 확장
o = MyClass()
print(o.__dict__)
o.z = 10
print(o.__dict__)
print(globals())
