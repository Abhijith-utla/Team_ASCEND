def sat(s: str) -> bool:
    if len(s) != 10 or not s.isalpha():
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    answer = ''
    for i in range(5):
        answer += chr(97 + i)
    return answer

# Test case
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
