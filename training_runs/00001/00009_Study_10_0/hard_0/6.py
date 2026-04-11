def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return "".join([str(i) for i in sorted(str(8 ** 1818), reverse=True) if i != "0"])[-11:-7:-1]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
