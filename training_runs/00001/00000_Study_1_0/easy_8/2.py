def sat(s: str):
    if s.count('oo') != 0:
        return False
    return True

def sol():
    s = "oo"
    return s

# Test
print(sol())  # should return: "oo"

if __name__ == "__main__":
    assert sat(sol())
