def sat(li: List[int]):
    return all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])

def sol():
    class Answer:
        def __init__(self, is_valid):
            self.is_valid = is_valid

    def sat(li: List[int]):
        if len(li) == 0:
            return Answer(True)
        unique_elements = set(li)
        for x in unique_elements:
            if li.index(x) < sum(li[:li.index(x)]):
                return Answer(False)
        return Answer(True)

    answer = sat(li)
    return answer.is_valid

if __name__ == "__main__":
    assert sat(sol())
