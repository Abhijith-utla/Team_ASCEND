def sat(stamps):
    if len(stamps) > 0 and stamps[0] == 0:
        return False
    for s in stamps:
        assert s in [18, 1, 43, 81]
    return len(stamps) <= 3 and sum(stamps) == 3

def sol():
    return [18, 1, 43, 81]

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
