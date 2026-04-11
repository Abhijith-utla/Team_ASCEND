def sat(s: str):
    return str(int(8 ** 2888)).count(s) == 10 and len(s) == 3

def sol():
    return "1000000000000000000000000000000000000000000000000000000000000000"

# Test the solution
def test():
    assert sat(sol()) == True

# Run the test
test()

if __name__ == "__main__":
    assert sat(sol())
