def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    return ''.join(s[i]*2 if i % 2 == 0 else s[i] for i in range(0,20,2)) + ''.join(s[i]*2 if i % 2 == 1 else s[i] for i in range(1,20,2))

if __name__ == "__main__":
    assert sat(sol())
