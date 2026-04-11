def sat(li: List[str]):
    return all(len(i) <= 5 for i in li) and all(i.isalpha() for i in li)

def sol():
    return "<answer>"

# Testing the function
assert sat(["Hello", "World"])
assert not sat(["Hello", "World1"])
assert not sat(["Hello1", "World"])
assert not sat(["Hello", "World12345"])
assert not sat(["Hello1", "World1"])

if __name__ == "__main__":
    assert sat(sol())
