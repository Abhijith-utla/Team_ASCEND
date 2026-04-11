def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):
                    for m in range(0, 10):
                        for n in range(0, 10):
                            for o in range(0, 10):
                                for p in range(0, 10):
                                    s = str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + str(o) + str(p)
                                    if sat(s):
                                        return s
    return None

if __name__ == "__main__":
    assert sat(sol())
