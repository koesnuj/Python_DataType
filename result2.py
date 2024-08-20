# 파이썬 자료형 테스트
# 다른 데이터 타입

# 변수 생성
a = 10          # int
b = 10.0        # float
c = "text"      # str
d = [1, 2, 3]   # list
e = (1, 2, 3)   # tuple
f = {"key": "value"}  # dict

# 연산 결과를 확인

# int + float
try:
    result = a + b
    print("int + float:", type(result))
except:
    print("int + float: 불가능")

# int + str
try:
    result = a + c
    print("int + str:", type(result))
except:
    print("int + str: 불가능")

# int + list
try:
    result = a + d
    print("int + list:", type(result))
except:
    print("int + list: 불가능")

# float + str
try:
    result = b + c
    print("float + str:", type(result))
except:
    print("float + str: 불가능")

# float + list
try:
    result = b + d
    print("float + list:", type(result))
except:
    print("float + list: 불가능")

# str + list
try:
    result = c + d
    print("str + list:", type(result))
except:
    print("str + list: 불가능")

# str + tuple
try:
    result = c + e
    print("str + tuple:", type(result))
except:
    print("str + tuple: 불가능")

# list + tuple
try:
    result = d + e
    print("list + tuple:", type(result))
except:
    print("list + tuple: 불가능")

# int - float
try:
    result = a - b
    print("int - float:", type(result))
except:
    print("int - float: 불가능")

# int - str
try:
    result = a - c
    print("int - str:", type(result))
except:
    print("int - str: 불가능")

# int - list
try:
    result = a - d
    print("int - list:", type(result))
except:
    print("int - list: 불가능")

# float - str
try:
    result = b - c
    print("float - str:", type(result))
except:
    print("float - str: 불가능")

# float - list
try:
    result = b - d
    print("float - list:", type(result))
except:
    print("float - list: 불가능")

# str - list
try:
    result = c - d
    print("str - list:", type(result))
except:
    print("str - list: 불가능")

# str - tuple
try:
    result = c - e
    print("str - tuple:", type(result))
except:
    print("str - tuple: 불가능")

# list - tuple
try:
    result = d - e
    print("list - tuple:", type(result))
except:
    print("list - tuple: 불가능")

# float - int
try:
    result = b - a
    print("float - int:", type(result))
except:
    print("float - int: 불가능")

# str - int
try:
    result = c - a
    print("str - int:", type(result))
except:
    print("str - int: 불가능")

# list - int
try:
    result = d - a
    print("list - int:", type(result))
except:
    print("list - int: 불가능")

# str - float
try:
    result = c - b
    print("str - float:", type(result))
except:
    print("str - float: 불가능")

# list - float
try:
    result = d - b
    print("list - float:", type(result))
except:
    print("list - float: 불가능")

# list - str
try:
    result = d - c
    print("list - str:", type(result))
except:
    print("list - str: 불가능")

# tuple - str
try:
    result = e - c
    print("tuple - str:", type(result))
except:
    print("tuple - str: 불가능")

# tuple - list
try:
    result = e - d
    print("tuple - list:", type(result))
except:
    print("tuple - list: 불가능")

# int * float
try:
    result = a * b
    print("int * float:", type(result))
except:
    print("int * float: 불가능")

# int * str
try:
    result = a * c
    print("int * str:", type(result))
except:
    print("int * str: 불가능")

# int * list
try:
    result = a * d
    print("int * list:", type(result))
except:
    print("int * list: 불가능")

# int * tuple
try:
    result = a * e
    print("int * tuple:", type(result))
except:
    print("int * tuple: 불가능")

# float * str
try:
    result = b * c
    print("float * str:", type(result))
except:
    print("float * str: 불가능")

# float * list
try:
    result = b * d
    print("float * list:", type(result))
except:
    print("float * list: 불가능")

# str * list
try:
    result = c * d
    print("str * list:", type(result))
except:
    print("str * list: 불가능")

# str * dict
try:
    result = c * f
    print("str * dict:", type(result))
except:
    print("str * dict: 불가능")

# float / int
try:
    result = b / a
    print("float / int:", type(result))
except:
    print("float / int: 불가능")

# str / int
try:
    result = c / a
    print("str / int:", type(result))
except:
    print("str / int: 불가능")

# list / int
try:
    result = d / a
    print("list / int:", type(result))
except:
    print("list / int: 불가능")

# str / float
try:
    result = c / b
    print("str / float:", type(result))
except:
    print("str / float: 불가능")

# list / float
try:
    result = d / b
    print("list / float:", type(result))
except:
    print("list / float: 불가능")

# list / str
try:
    result = d / c
    print("list / str:", type(result))
except:
    print("list / str: 불가능")

# tuple / str
try:
    result = e / c
    print("tuple / str:", type(result))
except:
    print("tuple / str: 불가능")

# tuple / list
try:
    result = e / d
    print("tuple / list:", type(result))
except:
    print("tuple / list: 불가능")
