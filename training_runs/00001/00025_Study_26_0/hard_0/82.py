def sat(ls: List[str]):
    return "".join(ls) == str(8 ** 88) and all(len(s) == 8 for s in ls)

def sol():
    return [str(i) for i in range(8 ** 88)]

# Testing the solution
def test_sol():
    assert sat(sol())

test_sol()

if __name__ == "__main__":
    assert sat(sol())
