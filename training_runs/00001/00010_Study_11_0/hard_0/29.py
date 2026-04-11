def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    def sat(ls: List[str]):
        return min(ls) == max(ls) == str(len(ls))

    ls = ["test", "example", "python", "programming"]

    assert sat(ls)

    ls = ["a", "b", "c"]
    assert not sat(ls)

    ls = ["short", "medium", "long", "verylongstring"]
    assert not sat(ls)

    ls = []
    assert not sat(ls)

    ls = ["a"]
    assert sat(ls)

    print("All tests passed")

sol()

if __name__ == "__main__":
    assert sat(sol())
