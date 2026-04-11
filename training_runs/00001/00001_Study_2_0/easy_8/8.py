def sat(s: str):
    return s.count('s') == 300 and s.count('ss') == 301 and s.count('sss') == 298

def sol():
    s = 's' * 300 + 'ss' * 301 + 'sss' * 298
    return s

print(sol())  # Output: 'ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss

if __name__ == "__main__":
    assert sat(sol())
