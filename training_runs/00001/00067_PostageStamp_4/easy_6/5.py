def sat(stamps=[8]):
    return len(stamps) == 1 and stamps[0] == 8

def sol():
    return [8]

if __name__ == "__main__":
    assert sat(sol())
