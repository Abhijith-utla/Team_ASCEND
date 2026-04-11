def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return min(str(x) for x in input("Enter your list of numbers separated by space: ").split(' '))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
