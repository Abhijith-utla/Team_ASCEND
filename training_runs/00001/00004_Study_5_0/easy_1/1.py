def sat(li: List[int]):
    return li.count(1) == 2 and li.count(2) == 2 and li.count(3) == 2 and li.count(4) == 2 and li.count(5) == 2 and li.count(6) == 2 and li.count(7) == 2 and li.count(8) == 2 and li.count(9) == 2

def sol():
    def is_valid(li: List[int]):
        count_dict = {}
        for num in li:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        for i in range(1, 10):
            if i not in count_dict:
                return False
        return True

    def generate():
        li = []
        while len(li) < 10:
            num = random.randint(1, 9)
            if num not in li:
                li.append(num)
        return li

    li = generate()
    while not is_valid(li):
        li = generate()
    return li

if __name__ == "__main__":
    assert sat(sol())
