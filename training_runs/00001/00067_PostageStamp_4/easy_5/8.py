def sat(stamps=[22]):
    return len(stamps) == 1 and stamps[0] == 22

def sol():
    return [22]

if __name__ == "__main__":
    assert sat(sol())
