def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    result = ""
    for _ in range(8 ** 2888):
        result += "8"
    return result.count("888") > 8 and len(result) == 3

if __name__ == "__main__":
    assert sat(sol())
