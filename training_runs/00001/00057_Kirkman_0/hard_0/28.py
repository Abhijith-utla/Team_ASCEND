def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    return [
        [
            [2, 5, 9],
            [0, 3, 7],
            [1, 6, 8],
            [4, 11, 14],
            [12, 15, 10]
        ],
        [
            [1, 4, 8],
            [3, 5, 11],
            [2, 7, 10],
            [6, 9, 14],
            [12, 15, 13]
        ],
        [
            [0, 3, 9],
            [1, 4, 11],
            [2, 5, 14],
            [7, 10, 15],
            [12, 13, 15]
        ],
        [
            [0, 1, 8],
            [2, 3, 11],
            [5, 6, 14],
            [9, 12,

if __name__ == "__main__":
    assert sat(sol())
