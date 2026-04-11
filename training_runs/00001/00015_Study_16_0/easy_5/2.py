def sat(s: str) -> bool:
    return s == '4.5abc' or s == '4.5abc. ' or s == ' 4.5abc.'

def sol():
    answer = '4.5abc'
    return answer

if __name__ == "__main__":
    assert sat(sol())
