def sat(s: str) -> bool:
    return str(8 ** int(2888)).count(s) > 8 and len(s) == 3

def sol() -> str:
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i**3 + j**3 + k**3 == 2888:
                    return str(i) + str(j) + str(k)
    return ""

if __name__ == "__main__":
    assert sat(sol())
