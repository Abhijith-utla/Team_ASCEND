def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return float(len(str(4.5))) + 4.5

print(sat(str(sol())))

if __name__ == "__main__":
    assert sat(sol())
