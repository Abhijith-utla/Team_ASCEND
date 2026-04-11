def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 3 and s.count("1") == 1 and eval(s) == 63

def sol():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                s = str(i) + str(j) + str(k) + str(8) + str(1) + str(j) + str(k) + str(8)
                if set(s) <= set("18-+*/") and s.count("8") == 3 and s.count("1") == 1 and eval(s) == 63:
                    return s
    return None

if __name__ == "__main__":
    assert sat(sol())
