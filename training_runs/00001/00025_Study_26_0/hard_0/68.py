def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    result = []
    while True:
        s = "{:08b}".format(len(result))
        if len(s) == 8 and len(result) > 0 and "".join(result) != s:
            break
        result.append(s)
    return result

print("".join(sol()))

if __name__ == "__main__":
    assert sat(sol())
