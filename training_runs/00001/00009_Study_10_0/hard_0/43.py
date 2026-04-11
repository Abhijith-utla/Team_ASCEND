def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    answer = ''.join(filter(sat, '8181818181818181'))
    return answer

print(sol())

if __name__ == "__main__":
    assert sat(sol())
