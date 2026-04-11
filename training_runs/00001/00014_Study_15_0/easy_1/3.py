def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** x) - 1 for x in li)

def sol():
    def sat(li: List[int]):
        return all(x >= 0 and 2 ** x - 1 == (2 ** x) - 1 for x in li)
    answer = []
    for x in range(10):
        if sat([x]):
            answer.append(x)
    return answer

if __name__ == "__main__":
    assert sat(sol())
