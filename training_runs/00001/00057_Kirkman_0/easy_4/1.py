def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and all(i in range(15) for i in (g for groups in daygroups for g in groups)) for groups in daygroups)
    assert all(len(g) == 4 for groups in daygroups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    daygroups = [[2, 3, 5, 6, 7], [1, 2, 3, 4, 5], [10, 11, 12, 13, 14], [8, 9, 10, 11, 12], [7, 8, 9, 10, 11], [6, 7, 8, 9, 10], [5, 6, 7, 8, 9]]
    return daygroups

if __name__ == "__main__":
    assert sat(sol())
