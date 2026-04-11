def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            s = str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + str(8 ** 1818)
                            if sat(s):
                                return s
    return None

if __name__ == "__main__":
    assert sat(sol())
