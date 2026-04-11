def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]]

def sol():
    def index_of_non_unique(l: List[int]):
        non_unique_indices = []
        for i in range(len(l)):
            if l[i] != l[i + 1]:
                non_unique_indices.append(i)
        return non_unique_indices

    def index_of_equality(l: List[int]):
        equality_indices = []
        for i in range(len(l) - 1):
            if l[i] == l[i + 1]:
                equality_indices.append(i)
        return equality_indices

    li = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

    non_unique_indices = index_of_non_unique(li)
    equality_indices = index_of_equality(li)

    for i in non_unique_indices:
        li[i] = li[i + 1]

    for i in

if __name__ == "__main__":
    assert sat(sol())
