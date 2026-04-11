def sat(stamps, max_stamps=3):
    return len(stamps) == max_stamps and sum(stamps) == 43

def sol():
    return [1, 2, 3, 4, 5]

if __name__ == "__main__":
    assert sat(sol())
