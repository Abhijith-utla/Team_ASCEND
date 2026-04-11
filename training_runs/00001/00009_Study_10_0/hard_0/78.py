def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    result = []
    for i in range(1, 1000000):
        number = '8' * i + '8' * 1818
        reversed_number = number[::-1]
        if '8' * 1818 in number and reversed_number == number and len(number) > 11:
            result.append(number)
    return result

print(sol())

if __name__ == "__main__":
    assert sat(sol())
