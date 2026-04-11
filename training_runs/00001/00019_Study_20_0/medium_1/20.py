def sat(li: List[int]):
    return all((j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128])))

def sol():
    def sat(li: List[int]):
        return all((j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128])))

    # This is a helper function to convert a list into a string representation
    def lst_to_str(lst: List[int]):
        return ', '.join(map(str, lst))

    # We start by generating a list of random integers
    li = [random.randint(0, 100) for _ in range(10)]

    # We convert the list to a string
    str_li = lst_to_str(li)

    # We now provide the list to the sat function
    result = sat(li)

    # We print the result
    print(f"The list {str_li} satisfies the condition: {result}")

    # We return the result
    return result

if __name__ == "__main__":
    assert sat(sol())
