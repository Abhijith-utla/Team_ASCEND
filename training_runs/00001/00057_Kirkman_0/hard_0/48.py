def sat(daygroups: List[List[List[int]]]):
    assert len(daygroups) == 7
    assert all(len(groups) == 5 and {i for g in groups for i in g} == set(range(15)) for groups in daygroups)
    assert all(len(g) == 3 for groups in daygroups for g in groups)
    return len({(i, j) for groups in daygroups for g in groups for i in g for j in g}) == 15 * 15

def sol():
    daygroups = [[[1, 2, 3], [5, 6, 7], [9, 10, 11], [13, 14, 15]] for _ in range(7)]
    return daygroups

print(sol())

if __name__ == "__main__":
    assert sat(sol())
