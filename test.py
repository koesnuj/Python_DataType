def test_operation(a, b, op):
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

# 요청된 연산 수행
print("덧셈 연산:")
test_operation(a, b, '+')
test_operation(a, c, '+')
test_operation(a, d, '+')
test_operation(b, c, '+')
test_operation(b, d, '+')
test_operation(c, d, '+')
test_operation(c, e, '+')
test_operation(d, e, '+')

print("\n뺄셈 연산:")
test_operation(a, b, '-')
test_operation(a, c, '-')
test_operation(a, d, '-')
test_operation(b, c, '-')
test_operation(b, d, '-')
test_operation(c, d, '-')
test_operation(c, e, '-')
test_operation(d, e, '-')

print("\n역방향 뺄셈 연산:")
test_operation(b, a, '-')
test_operation(c, a, '-')
test_operation(d, a, '-')
test_operation(c, b, '-')
test_operation(d, b, '-')
test_operation(d, c, '-')
test_operation(e, c, '-')
test_operation(e, d, '-')

print("\n곱셈 연산:")
test_operation(a, b, '*')
test_operation(a, c, '*')
test_operation(a, d, '*')
test_operation(a, e, '*')
test_operation(b, c, '*')
test_operation(b, d, '*')
test_operation(c, d, '*')
test_operation(c, f, '*')

print("\n나눗셈 연산:")
test_operation(b, a, '/')
test_operation(c, a, '/')
test_operation(d, a, '/')
test_operation(c, b, '/')
test_operation(d, b, '/')
test_operation(d, c, '/')
test_operation(e, c, '/')
test_operation(e, d, '/')