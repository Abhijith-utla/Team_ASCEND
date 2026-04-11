def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and all(i in g for g in groups) == set(range(1, 15)) for groups in daygroups)
    assert all(len(g) == 4 for groups in daygroups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 48

def sol():
    return [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 1],
        [16, 17, 18, 19],
        [20, 21, 22, 23],
        [24, 25, 26, 27]
    ]

if __name__ == "__main__":
    assert sat(sol())
