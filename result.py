# 파이썬 자료형 테스트
# 같은 데이터 타입 

def python_study (data_type):
    results = {}
    try:
        _ = data_type + data_type
        results['+'] = True
    except TypeError:
        results['+'] = False

    try:
        _ = data_type - data_type
        results['-'] = True
    except TypeError:
        results['-'] = False

    try:
        _ = data_type * data_type
        results['*'] = True
    except TypeError:
        results['*'] = False

    try:
        _ = data_type / data_type
        results['/'] = True
    except TypeError:
        results['/'] = False

    return results

# 실행
data_types = [10, 10.0, "text", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {'a': 1, 'b': 2}]
data_type_names = ['int', 'float', 'str', 'list', 'tuple', 'set', 'dict']

for name, data in zip(data_type_names, data_types):
    print(f"{name}:")
    
    try:
        _ = data + data
        print("  + : True")
    except TypeError:
        print("  + : False")
    
    try:
        _ = data - data
        print("  - : True")
    except TypeError:
        print("  - : False")
    
    try:
        _ = data * data
        print("  * : True")
    except TypeError:
        print("  * : False")
    
    try:
        _ = data / data
        print("  / : True")
    except TypeError:
        print("  / : False")

    print()
