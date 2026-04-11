def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    daygroups = [
        [[4, 7, 11, 13, 15]],
        [[2, 3, 6, 10, 12]],
        [[1, 5, 9, 14, 15]],
        [[10, 14, 15, 1, 3]],
        [[8, 11, 13, 14, 2]],
        [[1, 3, 5, 6, 7]],
        [[2, 4, 8, 9, 10]],
    ]
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

print(sol())

if __name__ == "__main__":
    assert sat(sol())
