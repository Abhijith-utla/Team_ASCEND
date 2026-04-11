def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    daygroups = [
        [[2, 5, 6], [1, 4, 7], [3, 8, 9], [10, 13, 14]],
        [[12, 15, 16], [11, 14, 17], [10, 13, 18], [9, 12, 15]],
        [[11, 16, 17], [12, 15, 18], [13, 16, 19], [14, 17, 20]],
        [[20, 23, 24], [19, 22, 25], [18, 21, 24], [17, 20, 23]],
        [[23, 26, 27], [22, 25, 28], [21, 24, 27], [20, 23, 26]],

if __name__ == "__main__":
    assert sat(sol())
