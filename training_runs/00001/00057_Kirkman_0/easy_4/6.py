def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and all(i in range(15) for i in (g for groups in daygroups for g in groups)) for groups in daygroups)
    assert all(len(g) == 4 for groups in daygroups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    return [
        [7, 13, 14, 15, 1],
        [6, 11, 12, 13, 2],
        [5, 8, 9, 10, 3],
        [4, 7, 14, 15, 4],
        [3, 6, 13, 14, 5],
        [2, 5, 8, 9, 6],
        [1, 4, 7, 10, 13]
    ]

if __name__ == "__main__":
    assert sat(sol())
