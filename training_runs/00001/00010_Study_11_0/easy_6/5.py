def sat(ls: List[str]):
    if len(ls) == 0:
        return False
    else:
        return all(len(i) < len(ls[0]) for i in ls)

def sol():
    return [i for i in range(10)]

# Test the function
def test_sol():
    assert sat(sol())

test_sol()

if __name__ == "__main__":
    assert sat(sol())
