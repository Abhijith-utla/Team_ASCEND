def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    return [
        [[2, 5, 11], [14, 3, 8], [4, 13, 6], [7, 1, 10], [12, 15, 9]],
        [[4, 1, 13], [12, 7, 14], [3, 9, 2], [8, 11, 6], [5, 15, 0]],
        [[9, 6, 10], [13, 1, 14], [1, 7, 12], [5, 14, 3], [8, 0, 4]],
        [[7, 15, 8], [9, 3, 13], [14, 10, 2], [4, 5, 1], [11, 0, 12]],
        [[6, 9, 5], [8, 4, 1], [0, 2, 15], [14,

if __name__ == "__main__":
    assert sat(sol())
