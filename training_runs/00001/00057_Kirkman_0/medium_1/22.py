def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    return [
        [0, 1, 2, 3, 5],
        [4, 3, 5, 6, 7],
        [8, 7, 6, 5, 4],
        [9, 8, 7, 6, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24]
    ]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
