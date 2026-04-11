def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    return [
        [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [9, 10, 11],
            [12, 13, 14]
        ],
        [
            [0, 1, 3],
            [2, 4, 6],
            [5, 7, 9],
            [8, 10, 12],
            [11, 13, 15]
        ],
        [
            [1, 2, 4],
            [3, 5, 7],
            [6, 8, 10],
            [9, 11, 13],
            [14, 15, 14]
        ],
        [
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [9, 12, 15],

if __name__ == "__main__":
    assert sat(sol())
