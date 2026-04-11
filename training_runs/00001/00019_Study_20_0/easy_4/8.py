def sat(li: List[int]) -> bool:
    return len(li) == len(set(li))

def sol():
    return bool(set(input("Enter a list of numbers separated by space: ").split()))

# You can test the function with the following lines
# print(sol())
# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
