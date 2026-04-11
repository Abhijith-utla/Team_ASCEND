def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 5 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    return [
        [2, 3, 4, 5, 1],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 1],
        [1, 2, 3, 1, 5],
        [2, 3, 4, 1, 1],
        [1, 2, 1, 2, 3],
        [1, 1, 2, 3, 4]
    ]

if __name__ == "__main__":
    assert sat(sol())
