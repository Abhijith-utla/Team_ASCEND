def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(999)) and len(li) == 1000

def sol():
    def sat(li: List[int]):
        return sorted(li) == list(range(999)) and all(li[i] != i for i in range(999)) and len(li) == 1000

    answer = [i for i in range(999) if not sat([i]*1000)]
    return answer[0]

if __name__ == "__main__":
    assert sat(sol())
