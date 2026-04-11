def sat(s: str):
    return s.count('z') == 100 and s.count('zo') == 101 and s.count('zz') == 98

def sol():
    s = "z"*100 + "zo"*101 + "z"*98
    return s

print(sol())

if __name__ == "__main__":
    assert sat(sol())
