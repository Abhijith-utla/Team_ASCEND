def sat(stamps=[25]):
    return len(stamps) == 1 and stamps[0] == 25

def sol():
    return [25]

if __name__ == "__main__":
    assert sat(sol())
