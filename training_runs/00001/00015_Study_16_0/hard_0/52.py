def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return "2.7"

if __name__ == "__main__":
    assert sat(sol())
