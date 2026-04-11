def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    def sat(li: List[int]):
        return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

    # Assuming there's a way to generate a list satisfying the 'sat' function.
    while True:
        answer = [i for i in range(10)]  # A list of 10 elements with 2 equal elements
        if sat(answer):
            return answer

if __name__ == "__main__":
    assert sat(sol())
