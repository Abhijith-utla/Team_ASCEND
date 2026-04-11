def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 5 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    return [
        [
            [2, 3, 5, 7, 11],
            [13, 17, 19, 23, 29],
            [31, 37, 41, 43, 47],
            [53, 59, 61, 67, 71],
            [73, 79, 83, 89, 97]
        ],
        [
            [12, 14, 15, 16, 18],
            [19, 20, 21, 22, 23],
            [24, 25, 26, 27, 28],
            [29, 30, 31, 32, 33],
            [34, 35, 36, 37, 38]
        ],
        [
            [3, 4, 5, 6, 7],

if __name__ == "__main__":
    assert sat(sol())
