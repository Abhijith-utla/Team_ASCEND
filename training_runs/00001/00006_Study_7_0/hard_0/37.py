def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    answer = "sat(str(8 ** 2888))"
    return answer

if __name__ == "__main__":
    assert sat(sol())
