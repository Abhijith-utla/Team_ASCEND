def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol() -> int:
    li = [i for i in range(10)]  # 10 numbers 0 to 9
    li[0] = 0  # To make it different from the example in the prompt
    li[1] = 1  # To make it different from the example in the prompt
    li[2] = 2  # To make it different from the example in the prompt
    li[3] = 3  # To make it different from the example in the prompt
    li[4] = 4  # To make it different from the example in the prompt
    li[5] = 5  # To make it different from the example in the prompt
    li[6] = 6  # To make it different from the example in the prompt
    li[7] = 7  # To make it different from the example in the prompt
    li[8] = 8  # To make it different from the example in the prompt
    li[9] = 9  # To make it different from the example in the prompt
    return li

if __name__ == "__main__":
    assert sat(sol())
