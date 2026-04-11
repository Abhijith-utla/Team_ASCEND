def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    return 'oo' in 'oooooooooooo' and 'oo' in 'oooooooooooo' and 'oo' in 'oooooooooooo'

# The output must be valid Python code only.
print("assert sol()")
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
