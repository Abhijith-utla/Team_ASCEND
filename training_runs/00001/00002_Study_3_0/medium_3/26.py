def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)-1))

def sol():
    li = [i for i in range(999)]
    return sorted(li)

# This is the main function to test our solution
def main():
    assert sat(sol())

# Run the main function
if __name__ == "__main__":
    main()

if __name__ == "__main__":
    assert sat(sol())
