def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = 'abcde'  # change this to any string of length 20
    if len(s) != 20:
        raise ValueError('String is not of length 20')
    return { 's': s }

# Uncomment the following lines to test the function
# print(sat(sol()))
# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
