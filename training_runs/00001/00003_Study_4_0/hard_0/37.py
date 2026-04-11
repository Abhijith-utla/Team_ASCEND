def sat(li: List[int]):
    return len(li) == 10 and li.count(li[3]) == 2

def sol():
    def sat(li: List[int]):
        return len(li) == 10 and li.count(li[3]) == 2

    answer = {}
    answer['valid'] = sat(list(range(10)))
    return answer

if __name__ == "__main__":
    assert sat(sol())
