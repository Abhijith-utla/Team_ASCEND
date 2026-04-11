def sat(s: str) -> bool:
    if len(s) != 10 or not s.isalpha():
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = input()
    if sat(s):
        return 'Valid'
    else:
        return 'Invalid'

# This checker will run: assert sat(sol())
!python -m doctest -v sol

if __name__ == "__main__":
    assert sat(sol())
