def sat(s: str) -> bool:
    if len(s) != 10 or not s.isalpha():
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    return 'aabbbcccdd'

# Test cases
assert sat(sol())
assert not sat('abcdefg')
assert not sat('12345678')
assert not sat('abcdwxyz')

# The final checker will run: assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
