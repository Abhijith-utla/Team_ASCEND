def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    return [
        [
            [5, 11, 14],
            [1, 12, 1],
            [3, 4, 13],
            [6, 7, 8],
            [9, 10, 11]
        ],
        [
            [0, 2, 5],
            [1, 3, 6],
            [4, 7, 9],
            [8, 11, 12],
            [10, 13, 14]
        ],
        [
            [1, 2, 4],
            [3, 5, 7],
            [6, 8, 9],
            [10, 11, 13],
            [12, 14, 15]
        ],
        [
            [0, 1, 4],
            [2, 3, 5],
            [6, 7, 8],
            [9, 11, 12],

if __name__ == "__main__":
    assert sat(sol())
