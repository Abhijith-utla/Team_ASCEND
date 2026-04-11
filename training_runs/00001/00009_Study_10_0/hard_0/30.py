def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    for i in range(1, 12):
        for j in range(1, 12):
            for k in range(1, 12):
                for l in range(1, 12):
                    for m in range(1, 12):
                        for n in range(1, 12):
                            s = str(i ** 7 * j ** 3 * k ** 10 * l ** 2 * m ** 10 * n ** 10)
                            if sat(s):
                                return s
    return None

if __name__ == "__main__":
    assert sat(sol())
