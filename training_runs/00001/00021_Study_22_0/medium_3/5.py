def sat(s: str) -> bool:
    if len(s) < 5 or len(s) > 30:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = 'Python'  # Replace 'Python' with any Python string of length between 5 and 30
    assert sat(s)
    return s

# Testing
print(sol())

if __name__ == "__main__":
    assert sat(sol())
