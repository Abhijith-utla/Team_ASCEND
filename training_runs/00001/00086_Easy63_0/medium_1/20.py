def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 3 and s.count("1") == 1 and eval(s) == 99

def sol():
    return "888"

print(eval(sol()))

if __name__ == "__main__":
    assert sat(sol())
