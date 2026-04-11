def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return len(min(ls)) == len(max(ls)) == str(len(ls))

# this is the test for the correct solution
assert sat([1,2,3,4,5])
# this is the test for the incorrect solution
assert not sat([1,2,3,5,4])

if __name__ == "__main__":
    assert sat(sol())
