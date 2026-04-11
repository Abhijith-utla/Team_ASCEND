def sat(s: str):
    return s.count('a') == 200 and s.count('aa') == 201 and s.count('aaa') == 198

def sol():
    s = 'aaaaaaaaaaaaaaaaaaa' * 1000  # Repeating 'a' 200 times
    s += 'aaa'  # Adding 'aaa' 201 times
    s += 'a'  # Adding 'a' 198 times
    return s

if __name__ == "__main__":
    assert sat(sol())
