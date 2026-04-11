def sat(li: List[int]):
    return all([i == li[j] + li[j+1] for i in range(len(li))])

def sol():
    def sat(li: List[int]):
        return all([i == li[j] + li[j+1] for j in range(len(li)-1)])

    answer = [i for i in range(10)]

    while not sat(answer):
        answer[0] += 1
        answer = [x % 10 for x in answer]

    return answer

if __name__ == "__main__":
    assert sat(sol())
