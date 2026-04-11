def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            for o in range(10):
                                for p in range(10):
                                    str_num = str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + str(o) + str(p)
                                    if len(str_num) > 11 and str_num == str_num[::-1] and sat(str_num):
                                        return str_num
    return "No valid string found"

if __name__ == "__main__":
    assert sat(sol())
