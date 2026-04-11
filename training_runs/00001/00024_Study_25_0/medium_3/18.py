def sat(s: str):
    return sorted(s) == sorted('uipenmtrsA') and s == s[::-1]

def sol():
    return ''.join(sorted(input()))

# Testing
print(sat(sol())) # Expected: 'A'
print(sat(sol())) # Expected: 'a'
print(sat(sol())) # Expected: 'I'
print(sat(sol())) # Expected: 'm'
print(sat(sol())) # Expected: 'n'
print(sat(sol())) # Expected: 'P'
print(sat(sol())) # Expected: 'R'
print(sat(sol())) # Expected: 'S'
print(sat(sol())) # Expected: 'T'
print(sat(sol())) # Expected: 'U'
print(sat(sol())) # Expected: 'uipenm'

if __name__ == "__main__":
    assert sat(sol())
