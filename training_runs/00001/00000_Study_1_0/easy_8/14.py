def sat(s: str):
    return 'o' not in s and 'oo' not in s and s.count('o') == 1000

def sol():
    return 'Hello' if 'Hello' in 'Hello World' and 'World' not in 'Hello World' else 'World'
```

This function checks if the string 'Hello' is in the string 'Hello World' and 'World' is not in 'Hello World'. If both conditions are true, it returns 'Hello'. Otherwise, it returns 'World'. This is a simple example of how you can use multiple conditions in Python.

if __name__ == "__main__":
    assert sat(sol())
