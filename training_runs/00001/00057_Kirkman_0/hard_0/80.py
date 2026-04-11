def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    return [
        [[5, 11, 13], [14, 3, 8], [10, 2, 7], [4, 6, 1], [0, 9, 12]],
        [[14, 1, 11], [6, 13, 7], [3, 10, 15], [9, 4, 2], [0, 8, 12]],
        [[13, 9, 11], [8, 7, 6], [15, 5, 5], [2, 4, 1], [10, 0, 3]],
        [[10, 3, 14], [7, 4, 12], [5, 1, 13], [6, 9, 2], [0, 15, 8]],
        [[2, 15, 7], [14, 5, 9], [3, 13, 1], [10,

if __name__ == "__main__":
    assert sat(sol())
