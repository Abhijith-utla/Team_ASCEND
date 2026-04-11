def sat(s: str):
    return set(s) <= set("1-*") and s.count("8") == 4 and s.count("1") == 1 and eval(s) == 197

def sol():
    return '8-1-1-*'

if __name__ == "__main__":
    assert sat(sol())
