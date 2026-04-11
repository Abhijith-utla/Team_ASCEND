def sat(li: List[int]):
    return len(li) == 10 and max(li) == 12

def sol():
    li = [i for i in range(10)] + [12]
    return li

# Testing the function
def test_sol():
    assert sat(sol())

test_sol()

if __name__ == "__main__":
    assert sat(sol())
