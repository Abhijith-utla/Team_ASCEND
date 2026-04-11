def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    return [[[2, 1, 3], [4, 2, 5], [6, 3, 7]], [[8, 4, 6], [10, 5, 8], [12, 6, 9]], [[14, 7, 10], [16, 8, 11], [18, 9, 12]], [[20, 10, 14], [22, 11, 13], [24, 12, 14]], [[26, 14, 16], [28, 15, 17], [30, 16, 18]], [[32, 18, 20], [34, 19, 21], [36, 20, 22]]]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
