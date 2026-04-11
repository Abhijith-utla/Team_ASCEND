def sat(daygroups):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 5 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 16

def sol():
    return [[(i, j) for i in range(15) for j in range(15) if (i, j) not in {(i, j) for groups in daygroups for g in groups for i in g for j in g}] for daygroups in [[(1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15)], [(1, 2, 3, 4, 6), (5, 7, 8, 9, 10), (11, 12, 13, 14, 15)], [(1, 2, 3, 4, 5), (6, 7, 8, 9, 11), (12, 13, 14, 15, 16)], [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (

if __name__ == "__main__":
    assert sat(sol())
