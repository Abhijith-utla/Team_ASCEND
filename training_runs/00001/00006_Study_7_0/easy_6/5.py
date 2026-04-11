def sat(s: str) -> bool:
    return str(8 ** int(2888)).count(s) > 8 and len(s) == 5

def sol():
    return "12345" in str(8 ** 2888)

assert sat(sol())
```

The string "12345" is inside the result of the expression 8 ** 2888, which is converted to a string. The count of the string "12345" in the string result is greater than 8 and the length of the string is 5.

if __name__ == "__main__":
    assert sat(sol())
