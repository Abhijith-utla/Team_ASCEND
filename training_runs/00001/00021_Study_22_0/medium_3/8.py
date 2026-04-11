def sat(s: str) -> bool:
    if len(s) < 5 or len(s) > 30:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    answer = ''.join([s[i] for i in range(0, len(s), 2)])
    return answer

if __name__ == "__main__":
    assert sat(sol())
