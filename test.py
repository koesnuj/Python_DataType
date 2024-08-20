def test(a, b, op):
    try:
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b
        print(f"{type(a).__name__} {op} {type(b).__name__}: {type(result).__name__}")
    except Exception as e:
        print(f"{type(a).__name__} {op} {type(b).__name__}: 불가능 ({type(e).__name__})")

# 변수 정의
a = 10          # int
b = 10.0        # float
c = "text"      # str
d = [1, 2, 3]   # list
e = (1, 2, 3)   # tuple
f = {"key": "value"}  # dict

# 연산 수행
print("더하기 연산:")
test(a, b, '+')
test(a, c, '+')
test(a, d, '+')
test(b, c, '+')
test(b, d, '+')
test(c, d, '+')
test(c, e, '+')
test(d, e, '+')

print("\n빼기 연산:")
test(a, b, '-')
test(a, c, '-')
test(a, d, '-')
test(b, c, '-')
test(b, d, '-')
test(c, d, '-')
test(c, e, '-')
test(d, e, '-')

print("\n빼기 연산2:")
test(b, a, '-')
test(c, a, '-')
test(d, a, '-')
test(c, b, '-')
test(d, b, '-')
test(d, c, '-')
test(e, c, '-')
test(e, d, '-')

print("\n곱하기 연산:")
test(a, b, '*')
test(a, c, '*')
test(a, d, '*')
test(a, e, '*')
test(b, c, '*')
test(b, d, '*')
test(c, d, '*')
test(c, f, '*')

print("\n나누기 연산:")
test(b, a, '/')
test(c, a, '/')
test(d, a, '/')
test(c, b, '/')
test(d, b, '/')
test(d, c, '/')
test(e, c, '/')
test(e, d, '/')
