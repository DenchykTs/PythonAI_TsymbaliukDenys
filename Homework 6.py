result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
            return a / b
    except TypeError:
        print("'<' not supported between instances of 'str' and 'int'")

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}
except TypeError:
    print("unhashable type: 'list'")
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError:
        print("raise ValueError")

print(result)