def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    def sat(li: List[int]):
        return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

    answer = [i for i in range(10)]
    while not sat(answer):
        answer[0] = (answer[0] + 1) % 10
    return answer

if __name__ == "__main__":
    assert sat(sol())
