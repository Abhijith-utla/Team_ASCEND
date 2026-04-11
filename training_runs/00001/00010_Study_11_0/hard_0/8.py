def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return str(len(ls))

# Testing
def test_sat():
    assert sat(["a", "b", "c"]) == True
    assert sat(["a", "b", "b"]) == False
    assert sat(["a"]) == True
    assert sat(["c", "b", "a"]) == True
    assert sat(["d", "d", "d", "d"]) == True
    assert sat(["1", "2", "3", "4"]) == True
    assert sat(["1"]) == True
    assert sat(["d", "e", "f", "g"]) == False

test_sat()

if __name__ == "__main__":
    assert sat(sol())
