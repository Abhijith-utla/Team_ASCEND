def sat(nums: List[int]):
    return [sorted([int(s) for s in str(n * n)]) for n in set(nums)] == [list(range(10))] * 174

def sol():
    return []

# To check the solution
def main():
    assert sat(sol())

main()

if __name__ == "__main__":
    assert sat(sol())
