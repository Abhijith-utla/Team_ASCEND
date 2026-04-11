def sat(quine):
    return eval(quine[::-1]) == quine

def sol():
    return ""

# Testing the function
def test_sol():
    assert sat(sol())
    assert not sat("a" * 1000)
    assert not sat("abc")
    assert not sat("123")
    assert sat("racecar")
    assert not sat("Madam")
    assert sat("Able was I ere I saw Elba")
    assert not sat("101")
    assert not sat("Was it a car or a cat I saw?")
    print("All tests passed.")

test_sol()

if __name__ == "__main__":
    assert sat(sol())
