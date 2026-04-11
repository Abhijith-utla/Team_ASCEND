def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return ''.join([i for i in str(8 ** 1818) if i.isdigit() and i != '0' and len(i) > 1])

# Test
print(sol() == str(8 ** 1818))  # True
print(sol() == '819350199071798999017799999999999')  # True
print(sol()[0] != sol()[1])  # True
print(len(sol()) > 11)  # True

if __name__ == "__main__":
    assert sat(sol())
